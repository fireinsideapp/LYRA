"""Síntesis de voz (ElevenLabs) y salud del servicio."""

from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.responses import FileResponse, JSONResponse
from sqlalchemy import text

from app.config import get_settings
from app.database import ES_POSTGRES, SessionLocal
from app.deps import get_voz
from app.schemas import Salud, VozPeticion
from app.services.prompts import FRASES_FRECUENTES
from app.services.voz import ErrorVoz, ServicioVoz

router = APIRouter(prefix="/api")
settings = get_settings()


@router.post("/voz", tags=["voz"], responses={200: {"content": {"audio/mpeg": {}}}})
async def sintetizar_voz(req: VozPeticion, request: Request, voz: ServicioVoz = Depends(get_voz)):
    """Convierte texto a voz. Responde el MP3; la URL reutilizable va en ``X-Audio-Url``."""
    try:
        ruta, hit = await voz.sintetizar(req.texto, persistente=req.persistente)
    except ErrorVoz as e:
        raise HTTPException(e.status, str(e)) from e
    return FileResponse(
        ruta,
        media_type="audio/mpeg",
        headers={
            "X-Audio-Cache": "HIT" if hit else "MISS",
            "X-Audio-Url": str(request.url_for("audio_cache", nombre=ruta.name)),
        },
    )


@router.get("/voz/audio/{nombre}", name="audio_cache", tags=["voz"],
            responses={200: {"content": {"audio/mpeg": {}}}})
async def audio_cacheado(nombre: str, voz: ServicioVoz = Depends(get_voz)):
    ruta = voz.buscar(nombre)
    if not ruta:
        raise HTTPException(404, "Audio no encontrado")
    return FileResponse(ruta, media_type="audio/mpeg",
                        headers={"Cache-Control": "public, max-age=604800, immutable"})


@router.post("/voz/precalentar", tags=["voz"])
async def precalentar_frases(voz: ServicioVoz = Depends(get_voz)):
    """Genera en caché permanente las frases frecuentes de Lyra (llamar una vez tras desplegar)."""
    generadas, en_cache, errores = 0, 0, []
    for frase in FRASES_FRECUENTES:
        try:
            _, hit = await voz.sintetizar(frase, persistente=True)
            en_cache += hit
            generadas += not hit
        except ErrorVoz as e:
            errores.append(f"{frase}: {e}")
            if e.status == 503:
                break
    return {"generadas": generadas, "ya_en_cache": en_cache, "errores": errores}


@router.get("/salud", response_model=Salud, tags=["salud"])
async def salud(response: Response):
    """Healthcheck para Railway."""
    try:
        async with SessionLocal() as s:
            await s.execute(text("SELECT 1"))
        db_ok = True
    except Exception:  # noqa: BLE001
        db_ok = False
    cuerpo = Salud(
        estado="ok" if db_ok else "degradado",
        base_datos="ok" if db_ok else "error",
        motor="postgresql" if ES_POSTGRES else "sqlite",
        gemini=settings.gemini_disponible,
        elevenlabs=settings.elevenlabs_disponible,
        version=settings.app_version,
    )
    if not db_ok:
        return JSONResponse(cuerpo.model_dump(), status_code=503)
    return cuerpo
