"""Conversación con Lyra: Gemini + memoria afectiva + voz opcional."""

import logging

from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import get_settings
from app.database import get_session
from app.deps import get_gemini, get_voz
from app.schemas import ContactoEmergencia, ConversacionPeticion, ConversacionRespuesta
from app.services import memoria
from app.services.gemini import ClienteGemini, ErrorGemini
from app.services.prompts import construir_instruccion_sistema, respuesta_respaldo
from app.services.texto import detectar_emergencia
from app.services.voz import ErrorVoz, ServicioVoz

log = logging.getLogger(__name__)
router = APIRouter(prefix="/api", tags=["conversacion"])
settings = get_settings()


@router.post("/conversacion", response_model=ConversacionRespuesta)
async def conversar(
    req: ConversacionPeticion,
    request: Request,
    session: AsyncSession = Depends(get_session),
    gemini: ClienteGemini = Depends(get_gemini),
    voz: ServicioVoz = Depends(get_voz),
):
    dispositivo_id = (
        req.dispositivo_id
        or request.headers.get("X-Dispositivo-Id")
        or request.headers.get("X-Android-Id")
        or "dispositivo_default"
    )
    disp = await memoria.obtener_o_crear_dispositivo(session, dispositivo_id)
    hechos = await memoria.listar_hechos(session, disp.id, settings.hechos_max_contexto)
    historial = await memoria.historial_reciente(session, disp.id, settings.historial_max_mensajes)
    emergencia = detectar_emergencia(req.pregunta)

    sistema = construir_instruccion_sistema(
        disp, hechos, req.receta_titulo, req.paso_texto, emergencia
    )

    fuente = "gemini"
    hecho_guardado: str | None = None
    try:
        resultado = await gemini.generar(sistema, historial, req.pregunta)
        respuesta = resultado.respuesta
        if resultado.hecho_nuevo:
            hecho = await memoria.guardar_hecho(
                session, disp.id, resultado.hecho_nuevo, resultado.categoria_hecho or "personal"
            )
            hecho_guardado = hecho.texto if hecho else None
    except ErrorGemini as e:
        log.warning("Gemini no disponible, se usa respaldo: %s", e)
        respuesta = respuesta_respaldo(disp, emergencia)
        fuente = "respaldo"

    memoria.guardar_intercambio(
        session, disp.id, req.pregunta, respuesta, req.receta_titulo, req.paso_texto
    )
    await session.commit()

    audio_url = None
    if req.con_voz and voz.disponible:
        try:
            ruta, _ = await voz.sintetizar(respuesta, persistente=False)
            audio_url = str(request.url_for("audio_cache", nombre=ruta.name))
        except ErrorVoz as e:
            log.warning("No se generó audio: %s", e)

    contacto = None
    if emergencia:
        contacto = ContactoEmergencia(nombre=disp.contacto_nombre, telefono=disp.contacto_telefono)

    return ConversacionRespuesta(
        respuesta=respuesta,
        hecho_nuevo=hecho_guardado,
        hecho_guardado=hecho_guardado,
        alerta_emergencia=emergencia,
        contacto_emergencia=contacto,
        audio_url=audio_url,
        fuente=fuente,
    )
