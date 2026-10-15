"""Síntesis de voz con ElevenLabs y caché de audio en disco.

Estructura del caché:
  audio_cache/fijo/      -> frases estáticas y pasos de recetas (nunca se podan)
  audio_cache/dinamico/  -> respuestas conversacionales (se podan por tamaño, LRU)

El nombre del archivo es el SHA-256 de (texto normalizado + voz + modelo + ajustes),
así que cambiar de voz o de ajustes invalida el caché automáticamente.
"""

import asyncio
import hashlib
import json
import logging
import os
import re
import time
from pathlib import Path

import httpx

from app.config import Settings

log = logging.getLogger(__name__)

URL_TTS = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
NOMBRE_VALIDO = re.compile(r"^[a-f0-9]{64}\.mp3$")


class ErrorVoz(Exception):
    def __init__(self, mensaje: str, status: int = 502):
        super().__init__(mensaje)
        self.status = status


class ServicioVoz:
    def __init__(self, settings: Settings, http: httpx.AsyncClient):
        self.s = settings
        self.http = http
        self.dir_fijo = Path(settings.audio_cache_dir) / "fijo"
        self.dir_dinamico = Path(settings.audio_cache_dir) / "dinamico"
        self.dir_fijo.mkdir(parents=True, exist_ok=True)
        self.dir_dinamico.mkdir(parents=True, exist_ok=True)
        self._locks: dict[str, asyncio.Lock] = {}

    @property
    def disponible(self) -> bool:
        return self.s.elevenlabs_disponible

    def _voice_settings(self) -> dict:
        return {
            "stability": self.s.elevenlabs_stability,
            "similarity_boost": self.s.elevenlabs_similarity,
            "style": self.s.elevenlabs_style,
            "use_speaker_boost": True,
            "speed": self.s.elevenlabs_speed,
        }

    def clave(self, texto: str) -> str:
        base = json.dumps(
            {
                "t": " ".join(texto.split()),
                "v": self.s.elevenlabs_voice_id,
                "m": self.s.elevenlabs_model_id,
                "f": self.s.elevenlabs_output_format,
                "s": self._voice_settings(),
            },
            sort_keys=True,
            ensure_ascii=False,
        )
        return hashlib.sha256(base.encode("utf-8")).hexdigest()

    def buscar(self, nombre: str) -> Path | None:
        if not NOMBRE_VALIDO.match(nombre):
            return None
        for d in (self.dir_fijo, self.dir_dinamico):
            ruta = d / nombre
            if ruta.is_file():
                return ruta
        return None

    async def sintetizar(self, texto: str, persistente: bool = False) -> tuple[Path, bool]:
        """Devuelve (ruta_mp3, desde_cache)."""
        texto = " ".join(texto.split())
        if not texto:
            raise ErrorVoz("El texto está vacío", 422)
        if not self.disponible:
            raise ErrorVoz("ElevenLabs no está configurado (ELEVENLABS_API_KEY / ELEVENLABS_VOICE_ID)", 503)

        clave = self.clave(texto)
        nombre = f"{clave}.mp3"
        existente = self._hit(nombre, persistente)
        if existente:
            return existente, True

        lock = self._locks.setdefault(clave, asyncio.Lock())
        async with lock:
            existente = self._hit(nombre, persistente)
            if existente:
                return existente, True
            audio = await self._llamar_api(texto)
            destino = (self.dir_fijo if persistente else self.dir_dinamico) / nombre
            await asyncio.to_thread(self._escribir_atomico, destino, audio)
        self._locks.pop(clave, None)

        if not persistente:
            await asyncio.to_thread(self._podar)
        return destino, False

    def _hit(self, nombre: str, persistente: bool) -> Path | None:
        ruta = self.buscar(nombre)
        if not ruta:
            return None
        if persistente and ruta.parent == self.dir_dinamico:
            nueva = self.dir_fijo / nombre
            os.replace(ruta, nueva)  # Se "promueve" a fijo
            return nueva
        try:
            os.utime(ruta)  # Marca de uso reciente para la poda LRU
        except OSError:
            pass
        return ruta

    async def _llamar_api(self, texto: str) -> bytes:
        url = URL_TTS.format(voice_id=self.s.elevenlabs_voice_id)
        headers = {"xi-api-key": self.s.elevenlabs_api_key or "", "Accept": "audio/mpeg"}
        cuerpo = {
            "text": texto,
            "model_id": self.s.elevenlabs_model_id,
            "voice_settings": self._voice_settings(),
        }
        params = {"output_format": self.s.elevenlabs_output_format}

        for intento in range(2):
            try:
                r = await self.http.post(url, params=params, headers=headers, json=cuerpo,
                                         timeout=self.s.elevenlabs_timeout_s)
            except httpx.HTTPError as e:
                if intento == 0:
                    await asyncio.sleep(0.8)
                    continue
                raise ErrorVoz(f"No se pudo contactar a ElevenLabs: {e!r}", 502) from e
            if r.status_code == 200:
                return r.content
            if r.status_code in (429, 500, 502, 503) and intento == 0:
                await asyncio.sleep(1.0)
                continue
            log.error("ElevenLabs HTTP %s: %s", r.status_code, r.text[:300])
            if r.status_code == 401:
                raise ErrorVoz("Clave de ElevenLabs inválida", 502)
            if r.status_code == 429:
                raise ErrorVoz("Cuota de ElevenLabs agotada o límite de velocidad", 503)
            raise ErrorVoz(f"ElevenLabs respondió {r.status_code}", 502)
        raise ErrorVoz("ElevenLabs no respondió", 502)

    @staticmethod
    def _escribir_atomico(destino: Path, datos: bytes) -> None:
        tmp = destino.with_suffix(f".{os.getpid()}.{time.monotonic_ns()}.tmp")
        tmp.write_bytes(datos)
        os.replace(tmp, destino)

    def _podar(self) -> None:
        limite = self.s.audio_cache_max_mb * 1024 * 1024
        archivos = [(p, p.stat()) for p in self.dir_dinamico.glob("*.mp3")]
        total = sum(st.st_size for _, st in archivos)
        if total <= limite:
            return
        objetivo = int(limite * 0.8)
        for ruta, st in sorted(archivos, key=lambda x: x[1].st_mtime):
            if total <= objetivo:
                break
            try:
                ruta.unlink()
                total -= st.st_size
            except OSError:
                pass
        log.info("Caché de audio podado a %.1f MB", total / 1024 / 1024)
