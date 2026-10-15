"""Configuración central de Lyra (variables de entorno / .env)."""

from functools import lru_cache
from pathlib import Path

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    # --- Aplicación ---
    app_nombre: str = "Lyra API"
    app_version: str = "1.0.0"
    entorno: str = "desarrollo"
    log_level: str = "INFO"
    cors_origins: str = "*"  # Lista separada por comas, o "*"

    # --- Base de datos ---
    # Railway inyecta DATABASE_URL (postgresql://...). Sin ella se usa SQLite local.
    database_url: str = f"sqlite+aiosqlite:///{(BASE_DIR / 'lyra.db').as_posix()}"

    @field_validator("database_url", mode="before")
    @classmethod
    def _url_por_defecto(cls, v: str | None) -> str:
        if not v or not str(v).strip():
            return f"sqlite+aiosqlite:///{(BASE_DIR / 'lyra.db').as_posix()}"
        return str(v).strip()

    # --- Google Gemini ---
    gemini_api_key: str | None = None
    # gemini-1.5-flash fue retirado por Google; se usa su sucesor directo.
    # Puede sobreescribirse con GEMINI_MODEL=gemini-1.5-flash si su cuenta aún lo tiene.
    gemini_model: str = "gemini-2.5-flash"
    gemini_timeout_s: float = 20.0
    gemini_temperatura: float = 0.7
    historial_max_mensajes: int = 10
    hechos_max_contexto: int = 40

    # --- ElevenLabs ---
    elevenlabs_api_key: str | None = None
    elevenlabs_voice_id: str | None = None
    elevenlabs_model_id: str = "eleven_multilingual_v2"
    elevenlabs_output_format: str = "mp3_44100_128"
    elevenlabs_stability: float = 0.55
    elevenlabs_similarity: float = 0.80
    elevenlabs_style: float = 0.25
    elevenlabs_speed: float = 0.90  # Un poco más lenta: mejor comprensión para personas mayores
    elevenlabs_timeout_s: float = 30.0

    # --- Archivos ---
    audio_cache_dir: Path = BASE_DIR / "audio_cache"
    audio_cache_max_mb: int = 300  # Límite para audios dinámicos (los fijos no se podan)
    static_recetas_dir: Path = BASE_DIR / "static" / "recetas"

    @property
    def cors_lista(self) -> list[str]:
        valor = self.cors_origins.strip()
        if valor == "*" or not valor:
            return ["*"]
        return [o.strip() for o in valor.split(",") if o.strip()]

    @property
    def gemini_disponible(self) -> bool:
        return bool(self.gemini_api_key)

    @property
    def elevenlabs_disponible(self) -> bool:
        return bool(self.elevenlabs_api_key and self.elevenlabs_voice_id)


@lru_cache
def get_settings() -> Settings:
    return Settings()
