"""Cliente de Google Gemini (REST) con salida JSON estructurada."""

import asyncio
import json
import logging
import re
from dataclasses import dataclass

import httpx

from app.config import Settings
from app.models import CATEGORIAS_HECHO, Mensaje
from app.services.texto import limitar_frases

log = logging.getLogger(__name__)

URL_GEMINI = "https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent"

ESQUEMA_RESPUESTA = {
    "type": "OBJECT",
    "properties": {
        "respuesta": {"type": "STRING"},
        "hecho_nuevo": {"type": "STRING", "nullable": True},
        "categoria_hecho": {"type": "STRING", "enum": list(CATEGORIAS_HECHO), "nullable": True},
        "cancelar_receta": {"type": "BOOLEAN"},
        "receta_recomendada": {"type": "STRING", "nullable": True},
    },
    "required": ["respuesta"],
}

_VALORES_NULOS = {"", "null", "none", "ninguno", "ninguna", "n/a", "no"}


class ErrorGemini(Exception):
    pass


@dataclass
class ResultadoIA:
    respuesta: str
    hecho_nuevo: str | None = None
    categoria_hecho: str | None = None
    cancelar_receta: bool = False
    receta_recomendada: str | None = None


class ClienteGemini:
    def __init__(self, settings: Settings, http: httpx.AsyncClient):
        self.s = settings
        self.http = http

    @property
    def disponible(self) -> bool:
        return self.s.gemini_disponible

    def _payload(self, sistema: str, historial: list[Mensaje], pregunta: str) -> dict:
        contents: list[dict] = []
        for m in historial:
            rol = "user" if m.rol == "usuario" else "model"
            contents.append({"role": rol, "parts": [{"text": m.contenido}]})
        while contents and contents[0]["role"] != "user":
            contents.pop(0)  # Gemini exige que la conversación empiece con el usuario
        contents.append({"role": "user", "parts": [{"text": pregunta}]})

        config: dict = {
            "responseMimeType": "application/json",
            "responseSchema": ESQUEMA_RESPUESTA,
            "temperature": self.s.gemini_temperatura,
            "maxOutputTokens": 512,
        }
        if "2.5-flash" in self.s.gemini_model:
            # Respuestas conversacionales: sin "pensamiento" = menor latencia y costo
            config["thinkingConfig"] = {"thinkingBudget": 0}

        return {
            "systemInstruction": {"parts": [{"text": sistema}]},
            "contents": contents,
            "generationConfig": config,
        }

    async def generar(self, sistema: str, historial: list[Mensaje], pregunta: str) -> ResultadoIA:
        if not self.disponible:
            raise ErrorGemini("GEMINI_API_KEY no configurada")

        url = URL_GEMINI.format(modelo=self.s.gemini_model)
        payload = self._payload(sistema, historial, pregunta)
        headers = {"x-goog-api-key": self.s.gemini_api_key or ""}
        ultimo_error: str = "desconocido"

        for intento in range(2):
            try:
                r = await self.http.post(url, json=payload, headers=headers, timeout=self.s.gemini_timeout_s)
            except httpx.HTTPError as e:
                ultimo_error = f"red: {e!r}"
                log.warning("Gemini intento %s falló: %s", intento + 1, ultimo_error)
                await asyncio.sleep(0.8)
                continue
            if r.status_code in (429, 500, 502, 503, 504) and intento == 0:
                ultimo_error = f"HTTP {r.status_code}"
                await asyncio.sleep(1.0)
                continue
            if r.status_code != 200:
                raise ErrorGemini(f"HTTP {r.status_code}: {r.text[:300]}")
            return self._interpretar(r.json())

        raise ErrorGemini(ultimo_error)

    @staticmethod
    def _interpretar(data: dict) -> ResultadoIA:
        candidatos = data.get("candidates") or []
        if not candidatos:
            motivo = (data.get("promptFeedback") or {}).get("blockReason", "sin candidatos")
            raise ErrorGemini(f"Respuesta vacía: {motivo}")
        partes = (candidatos[0].get("content") or {}).get("parts") or []
        texto = "".join(p.get("text", "") for p in partes if not p.get("thought")).strip()
        if not texto:
            raise ErrorGemini(f"Sin texto (finishReason={candidatos[0].get('finishReason')})")

        texto = re.sub(r"^```(?:json)?\s*|\s*```$", "", texto)
        try:
            obj = json.loads(texto)
        except json.JSONDecodeError:
            log.warning("Gemini no devolvió JSON válido; se usa el texto plano.")
            return ResultadoIA(respuesta=limitar_frases(texto))

        respuesta = str(obj.get("respuesta") or "").strip()
        if not respuesta:
            raise ErrorGemini("JSON sin 'respuesta'")

        # Desempaquetar si Gemini anidó un JSON dentro del campo string 'respuesta'
        if respuesta.startswith("{") and "respuesta" in respuesta:
            try:
                sub_obj = json.loads(respuesta)
                if isinstance(sub_obj, dict) and "respuesta" in sub_obj:
                    respuesta = str(sub_obj.get("respuesta") or "").strip()
                    if not obj.get("hecho_nuevo") and sub_obj.get("hecho_nuevo"):
                        obj["hecho_nuevo"] = sub_obj.get("hecho_nuevo")
                    if "cancelar_receta" in sub_obj:
                        obj["cancelar_receta"] = sub_obj.get("cancelar_receta")
                    if "receta_recomendada" in sub_obj:
                        obj["receta_recomendada"] = sub_obj.get("receta_recomendada")
            except Exception:
                pass

        hecho = obj.get("hecho_nuevo")
        hecho = str(hecho).strip() if hecho is not None else None
        if hecho and hecho.lower() in _VALORES_NULOS:
            hecho = None
        categoria = obj.get("categoria_hecho")
        if categoria not in CATEGORIAS_HECHO:
            categoria = "personal" if hecho else None

        cancelar = bool(obj.get("cancelar_receta", False))
        receta_rec = obj.get("receta_recomendada")
        receta_rec = str(receta_rec).strip() if receta_rec else None

        return ResultadoIA(
            respuesta=limitar_frases(respuesta, 3),
            hecho_nuevo=hecho[:300] if hecho else None,
            categoria_hecho=categoria,
            cancelar_receta=cancelar,
            receta_recomendada=receta_rec,
        )
