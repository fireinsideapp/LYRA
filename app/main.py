"""Punto de entrada de la API de Lyra."""

import logging
from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.database import ES_POSTGRES, SessionLocal, crear_tablas, engine
from app.routers import conversacion, perfil, recetas, sistema
from app.seed.seeder import sembrar_recetas
from app.services.gemini import ClienteGemini
from app.services.voz import ServicioVoz

settings = get_settings()
logging.basicConfig(
    level=settings.log_level.upper(),
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
)
log = logging.getLogger("lyra")


@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info("Iniciando Lyra (%s) con %s", settings.entorno, "PostgreSQL" if ES_POSTGRES else "SQLite")
    settings.static_recetas_dir.mkdir(parents=True, exist_ok=True)

    await crear_tablas()
    async with SessionLocal() as session:
        await sembrar_recetas(session)

    app.state.http = httpx.AsyncClient(
        timeout=httpx.Timeout(30.0, connect=5.0),
        limits=httpx.Limits(max_connections=20, max_keepalive_connections=10),
    )
    app.state.gemini = ClienteGemini(settings, app.state.http)
    app.state.voz = ServicioVoz(settings, app.state.http)

    if not settings.gemini_disponible:
        log.warning("GEMINI_API_KEY no configurada: /api/conversacion usará respuestas de respaldo.")
    if not settings.elevenlabs_disponible:
        log.warning("ElevenLabs no configurado: los endpoints de voz responderán 503.")

    yield

    await app.state.http.aclose()
    await engine.dispose()


app = FastAPI(
    title=settings.app_nombre,
    version=settings.app_version,
    description="Backend de Lyra: asistente de cocina humana y accesible para personas de la tercera edad.",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_lista,
    allow_credentials=False,  # Sin cookies: la identidad es el dispositivo_id
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Audio-Cache", "X-Audio-Url"],
)

app.include_router(sistema.router)
app.include_router(recetas.router)
app.include_router(conversacion.router)
app.include_router(perfil.router)


@app.get("/", include_in_schema=False)
async def raiz():
    return {"servicio": "Lyra API", "docs": "/docs", "salud": "/api/salud"}
