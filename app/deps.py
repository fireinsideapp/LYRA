"""Dependencias compartidas de FastAPI."""

from fastapi import Request

from app.services.gemini import ClienteGemini
from app.services.voz import ServicioVoz


def get_gemini(request: Request) -> ClienteGemini:
    return request.app.state.gemini


def get_voz(request: Request) -> ServicioVoz:
    return request.app.state.voz
