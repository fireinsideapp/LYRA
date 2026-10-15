"""Catálogo de recetas e imágenes estáticas de los pasos."""

from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import FileResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.config import get_settings
from app.database import get_session
from app.deps import get_voz
from app.models import Paso, Receta
from app.schemas import (
    IngredienteOut,
    IngredientesAgrupados,
    PasoOut,
    RecetaDetalle,
    RecetaResumen,
)
from app.services.voz import ErrorVoz, ServicioVoz

router = APIRouter(tags=["recetas"])
settings = get_settings()

EXTENSIONES_IMAGEN = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg"}


def _ruta_imagen(archivo: str) -> Path | None:
    """Resuelve el archivo dentro de static/recetas impidiendo path traversal."""
    base = Path(settings.static_recetas_dir).resolve()
    try:
        ruta = (base / archivo).resolve()
    except (OSError, ValueError):
        return None
    if not ruta.is_relative_to(base) or ruta.suffix.lower() not in EXTENSIONES_IMAGEN:
        return None
    return ruta if ruta.is_file() else None


def _url_imagen(request: Request, archivo: str | None) -> str | None:
    if not archivo or not _ruta_imagen(archivo):
        return None
    return str(request.url_for("imagen_receta", archivo=archivo))


def _resumen(request: Request, r: Receta) -> RecetaResumen:
    return RecetaResumen(
        slug=r.slug, titulo=r.titulo, descripcion=r.descripcion, porciones=r.porciones,
        tiempo_total_min=r.tiempo_total_min, dificultad=r.dificultad,
        imagen_url=_url_imagen(request, r.imagen),
    )


@router.get("/api/recetas", response_model=list[RecetaResumen])
async def listar_recetas(request: Request, session: AsyncSession = Depends(get_session)):
    recetas = await session.scalars(select(Receta).order_by(Receta.titulo))
    return [_resumen(request, r) for r in recetas]


@router.get("/api/recetas/{slug}", response_model=RecetaDetalle)
async def detalle_receta(
    slug: str,
    request: Request,
    session: AsyncSession = Depends(get_session),
    voz: ServicioVoz = Depends(get_voz),
):
    receta = await session.scalar(
        select(Receta)
        .where(Receta.slug == slug)
        .options(selectinload(Receta.ingredientes), selectinload(Receta.pasos))
    )
    if not receta:
        raise HTTPException(404, "Receta no encontrada")

    grupos: dict[str, list[IngredienteOut]] = {"base": [], "salsa": [], "servicio": []}
    for ing in receta.ingredientes:
        grupos.setdefault(ing.categoria, []).append(
            IngredienteOut(
                nombre=ing.nombre,
                cantidad=ing.cantidad,
                grupo=ing.categoria.capitalize(),
                categoria=ing.categoria,
            )
        )

    pasos = [
        PasoOut(
            orden=p.orden,
            texto=p.detalle_hablado or p.resumen_visual,
            resumen=p.resumen_visual,
            resumen_visual=p.resumen_visual,
            detalle_hablado=p.detalle_hablado,
            alertas_seguridad=p.alertas_seguridad or [],
            nota_seguridad=p.nota_seguridad,
            temporizador_segundos=p.temporizador_segundos,
            imagen=p.imagen,
            imagen_url=_url_imagen(request, p.imagen),
            audio_url=(
                str(request.url_for("audio_paso", slug=receta.slug, orden=p.orden))
                if voz.disponible else None
            ),
        )
        for p in receta.pasos
    ]
    return RecetaDetalle(
        **_resumen(request, receta).model_dump(),
        ingredientes=IngredientesAgrupados(**grupos),
        pasos=pasos,
    )


@router.get("/api/recetas/{slug}/pasos/{orden}/audio", name="audio_paso",
            responses={200: {"content": {"audio/mpeg": {}}}})
async def audio_paso(
    slug: str,
    orden: int,
    session: AsyncSession = Depends(get_session),
    voz: ServicioVoz = Depends(get_voz),
):
    """Audio del ``detalle_hablado`` de un paso. Se guarda en caché permanente."""
    paso = await session.scalar(
        select(Paso).join(Receta).where(Receta.slug == slug, Paso.orden == orden)
    )
    if not paso:
        raise HTTPException(404, "Paso no encontrado")
    texto = paso.detalle_hablado
    if paso.nota_seguridad:
        texto = f"{texto} {paso.nota_seguridad}"
    try:
        ruta, hit = await voz.sintetizar(texto, persistente=True)
    except ErrorVoz as e:
        raise HTTPException(e.status, str(e)) from e
    return FileResponse(ruta, media_type="audio/mpeg",
                        headers={"X-Audio-Cache": "HIT" if hit else "MISS",
                                 "Cache-Control": "public, max-age=604800"})


@router.get("/recetas/{archivo:path}", name="imagen_receta", include_in_schema=True)
async def imagen_receta(archivo: str):
    """Sirve imágenes estáticas de recetas y pasos (static/recetas)."""
    ruta = _ruta_imagen(archivo)
    if not ruta:
        raise HTTPException(404, "Imagen no encontrada")
    return FileResponse(ruta, headers={"Cache-Control": "public, max-age=86400"})
