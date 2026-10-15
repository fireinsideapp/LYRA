"""Motor asíncrono de SQLAlchemy con soporte PostgreSQL (Railway) y SQLite (local)."""

from collections.abc import AsyncIterator
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from app.config import get_settings


class Base(DeclarativeBase):
    pass


def normalizar_url(url: str) -> tuple[str, dict]:
    """Convierte la DATABASE_URL de Railway al dialecto asíncrono correcto.

    Railway entrega ``postgresql://`` (o el legado ``postgres://``); SQLAlchemy
    async necesita ``postgresql+asyncpg://``. asyncpg tampoco acepta el parámetro
    ``sslmode`` en la URL, así que se traslada a ``connect_args``.
    """
    connect_args: dict = {}
    if url.startswith("postgres://"):
        url = "postgresql://" + url[len("postgres://"):]
    if url.startswith("postgresql://"):
        url = "postgresql+asyncpg://" + url[len("postgresql://"):]

    if url.startswith("postgresql+asyncpg://"):
        partes = urlsplit(url)
        query = dict(parse_qsl(partes.query))
        sslmode = query.pop("sslmode", None)
        if sslmode and sslmode != "disable":
            connect_args["ssl"] = sslmode
        url = urlunsplit(partes._replace(query=urlencode(query)))
    elif url.startswith("sqlite"):
        if "+aiosqlite" not in url:
            url = url.replace("sqlite://", "sqlite+aiosqlite://", 1)
    return url, connect_args


_settings = get_settings()
DATABASE_URL, _connect_args = normalizar_url(_settings.database_url)
ES_POSTGRES = DATABASE_URL.startswith("postgresql")

_engine_kwargs: dict = {"pool_pre_ping": True, "connect_args": _connect_args}
if ES_POSTGRES:
    _engine_kwargs.update(pool_size=5, max_overflow=5, pool_recycle=1800)

engine = create_async_engine(DATABASE_URL, **_engine_kwargs)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def crear_tablas() -> None:
    # Importación tardía para registrar los modelos en Base.metadata
    from app import models  # noqa: F401

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncIterator[AsyncSession]:
    async with SessionLocal() as session:
        yield session
