"""Utilidades de texto y detección de posibles emergencias."""

import re
import unicodedata


def quitar_acentos(texto: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn"
    )


def normalizar(texto: str) -> str:
    """Minúsculas, sin acentos, sin puntuación y con espacios colapsados (para deduplicar)."""
    t = quitar_acentos(texto.lower())
    t = re.sub(r"[^\w\s]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


# Respaldo determinista: Gemini ya está instruido, pero la app necesita una
# bandera fiable para mostrar el botón de "Llamar a un familiar".
_PATRONES_EMERGENCIA = [
    r"\bme cai\b", r"\bme caigo\b", r"\bcaida\b", r"\bme resbale\b",
    r"\bme duele\b", r"\bdolor\b", r"\bme queme\b", r"\bquemadura\b", r"\bme corte\b",
    r"\bsangr", r"\bmareo\b", r"\bmaread[oa]\b", r"\bme desmay", r"\bno puedo respirar\b",
    r"\bme ahogo\b", r"\bpecho\b", r"\bemergencia\b", r"\bauxilio\b", r"\bayudenme\b",
    r"\bhuele a gas\b", r"\bfuga de gas\b", r"\bincendio\b", r"\bse prendio fuego\b",
]
_REGEX_EMERGENCIA = re.compile("|".join(_PATRONES_EMERGENCIA))


def detectar_emergencia(texto: str) -> bool:
    return bool(_REGEX_EMERGENCIA.search(normalizar(texto)))


def limitar_frases(texto: str, maximo: int = 3) -> str:
    """Recorta la respuesta hablada a ``maximo`` frases (regla de 2-3 frases)."""
    texto = re.sub(r"\s+", " ", texto).strip()
    frases = re.split(r"(?<=[.!?…])\s+", texto)
    return " ".join(frases[:maximo]).strip()
