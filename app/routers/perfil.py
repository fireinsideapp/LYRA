"""Perfil del dispositivo: datos personales, alergias y memoria afectiva."""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models import Dispositivo, HechoMemoria
from app.schemas import HechoOut, PerfilActualizar, PerfilOut
from app.services import memoria

router = APIRouter(prefix="/api/perfil", tags=["perfil"])

DispositivoQuery = Annotated[
    str, Query(min_length=4, max_length=128, pattern=r"^[A-Za-z0-9_\-]+$", description="ANDROID_ID")
]


async def _perfil(session: AsyncSession, disp: Dispositivo) -> PerfilOut:
    hechos = await memoria.listar_hechos(session, disp.id)
    por_cat = lambda *cats: [HechoOut.model_validate(h) for h in hechos if h.categoria in cats]  # noqa: E731
    return PerfilOut(
        dispositivo_id=disp.dispositivo_id,
        androidId=disp.dispositivo_id,
        nombre=disp.nombre,
        tratamiento=disp.tratamiento,
        contacto_nombre=disp.contacto_nombre,
        contacto_telefono=disp.contacto_telefono,
        preferencias=disp.preferencias or {},
        alergias=por_cat("alergia"),
        condiciones_salud=por_cat("salud"),
        recuerdos=por_cat("personal", "preferencia"),
        creado_en=disp.creado_en,
    )


@router.get("", response_model=PerfilOut)
async def obtener_perfil(
    dispositivo_id: DispositivoQuery,
    session: AsyncSession = Depends(get_session),
):
    """Devuelve el perfil; si el dispositivo es nuevo lo registra (primer arranque de la app)."""
    disp = await memoria.obtener_o_crear_dispositivo(session, dispositivo_id)
    await session.commit()
    return await _perfil(session, disp)


@router.put("", response_model=PerfilOut)
@router.post("", response_model=PerfilOut)
async def actualizar_perfil(datos: PerfilActualizar, session: AsyncSession = Depends(get_session)):
    dispositivo_id = datos.dispositivo_id or "dispositivo_default"
    disp = await memoria.obtener_o_crear_dispositivo(session, dispositivo_id)
    campos = datos.model_dump(exclude_unset=True)

    for campo in ("nombre", "contacto_nombre", "contacto_telefono"):
        if campo in campos:
            setattr(disp, campo, campos[campo] or None)
    if datos.tratamiento:
        disp.tratamiento = "tú" if datos.tratamiento in ("tú", "tu") else "usted"
    if datos.preferencias is not None:
        disp.preferencias = {**(disp.preferencias or {}), **datos.preferencias}
    if datos.alergias is not None:
        await memoria.reemplazar_categoria(session, disp.id, "alergia", datos.alergias)
    if datos.condiciones_salud is not None:
        await memoria.reemplazar_categoria(session, disp.id, "salud", datos.condiciones_salud)

    await session.commit()
    return await _perfil(session, disp)


@router.delete("/hechos/{hecho_id}", status_code=204)
async def olvidar_hecho(
    hecho_id: int,
    dispositivo_id: DispositivoQuery,
    session: AsyncSession = Depends(get_session),
):
    """Permite a la persona o a su familia pedir a Lyra que "olvide" un dato."""
    hecho = await session.scalar(
        select(HechoMemoria)
        .join(Dispositivo)
        .where(HechoMemoria.id == hecho_id, Dispositivo.dispositivo_id == dispositivo_id)
    )
    if not hecho:
        raise HTTPException(404, "Hecho no encontrado")
    hecho.activo = False
    await session.commit()
