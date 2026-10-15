"""Acceso a perfil, memoria afectiva (hechos) e historial de mensajes."""

import logging

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CATEGORIAS_HECHO, Dispositivo, HechoMemoria, Mensaje
from app.services.texto import normalizar

log = logging.getLogger(__name__)


async def obtener_dispositivo(session: AsyncSession, dispositivo_id: str) -> Dispositivo | None:
    return await session.scalar(
        select(Dispositivo).where(Dispositivo.dispositivo_id == dispositivo_id)
    )


async def obtener_o_crear_dispositivo(session: AsyncSession, dispositivo_id: str) -> Dispositivo:
    disp = await obtener_dispositivo(session, dispositivo_id)
    if disp:
        return disp
    try:
        async with session.begin_nested():
            disp = Dispositivo(dispositivo_id=dispositivo_id, tratamiento="usted", preferencias={})
            session.add(disp)
    except IntegrityError:
        # Otra petición concurrente lo creó primero
        disp = await obtener_dispositivo(session, dispositivo_id)
        assert disp is not None
    return disp


async def listar_hechos(
    session: AsyncSession, dispositivo_pk: int, limite: int | None = None
) -> list[HechoMemoria]:
    consulta = (
        select(HechoMemoria)
        .where(HechoMemoria.dispositivo_pk == dispositivo_pk, HechoMemoria.activo.is_(True))
        .order_by(HechoMemoria.creado_en.desc(), HechoMemoria.id.desc())
    )
    if limite:
        consulta = consulta.limit(limite)
    return list((await session.scalars(consulta)).all())


async def guardar_hecho(
    session: AsyncSession,
    dispositivo_pk: int,
    texto: str,
    categoria: str = "personal",
    origen: str = "conversacion",
) -> HechoMemoria | None:
    """Guarda un hecho evitando duplicados. Devuelve None si ya existía."""
    texto = " ".join(texto.split())[:500]
    if not texto:
        return None
    if categoria not in CATEGORIAS_HECHO:
        categoria = "personal"
    norm = normalizar(texto)[:500]
    existente = await session.scalar(
        select(HechoMemoria.id).where(
            HechoMemoria.dispositivo_pk == dispositivo_pk,
            HechoMemoria.texto_normalizado == norm,
            HechoMemoria.activo.is_(True),
        )
    )
    if existente:
        return None
    hecho = HechoMemoria(
        dispositivo_pk=dispositivo_pk,
        categoria=categoria,
        texto=texto,
        texto_normalizado=norm,
        origen=origen,
    )
    session.add(hecho)
    await session.flush()
    log.info("Nuevo hecho [%s] para dispositivo %s", categoria, dispositivo_pk)
    return hecho


async def reemplazar_categoria(
    session: AsyncSession, dispositivo_pk: int, categoria: str, textos: list[str]
) -> None:
    """Sustituye todos los hechos activos de una categoría (alergias, salud) por ``textos``."""
    actuales = await session.scalars(
        select(HechoMemoria).where(
            HechoMemoria.dispositivo_pk == dispositivo_pk,
            HechoMemoria.categoria == categoria,
            HechoMemoria.activo.is_(True),
        )
    )
    for h in actuales:
        h.activo = False
    await session.flush()
    for t in textos:
        await guardar_hecho(session, dispositivo_pk, t, categoria, origen="perfil")


async def historial_reciente(
    session: AsyncSession, dispositivo_pk: int, limite: int
) -> list[Mensaje]:
    filas = await session.scalars(
        select(Mensaje)
        .where(Mensaje.dispositivo_pk == dispositivo_pk)
        .order_by(Mensaje.creado_en.desc(), Mensaje.id.desc())
        .limit(limite)
    )
    return list(reversed(filas.all()))


def guardar_intercambio(
    session: AsyncSession,
    dispositivo_pk: int,
    pregunta: str,
    respuesta: str,
    receta_titulo: str | None,
    paso_texto: str | None,
) -> None:
    session.add_all(
        [
            Mensaje(dispositivo_pk=dispositivo_pk, rol="usuario", contenido=pregunta,
                    receta_titulo=receta_titulo, paso_texto=paso_texto),
            Mensaje(dispositivo_pk=dispositivo_pk, rol="lyra", contenido=respuesta,
                    receta_titulo=receta_titulo, paso_texto=paso_texto),
        ]
    )
