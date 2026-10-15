"""Esquemas Pydantic (contratos de la API REST)."""

from datetime import datetime
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, StringConstraints

DispositivoId = Annotated[
    str, StringConstraints(strip_whitespace=True, min_length=4, max_length=128, pattern=r"^[A-Za-z0-9_\-]+$")
]
TextoCorto = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=300)]


# ---------- Recetas ----------
class RecetaResumen(BaseModel):
    slug: str
    titulo: str
    descripcion: str
    porciones: int
    tiempo_total_min: int
    dificultad: str
    imagen_url: str | None = None


class IngredienteOut(BaseModel):
    nombre: str
    cantidad: str
    grupo: str = ""
    categoria: str = ""


class IngredientesAgrupados(BaseModel):
    base: list[IngredienteOut] = []
    salsa: list[IngredienteOut] = []
    servicio: list[IngredienteOut] = []


class PasoOut(BaseModel):
    orden: int
    texto: str = ""  # Interoperabilidad con Android (@SerialName("texto") val textoCompleto)
    resumen: str | None = None  # Interoperabilidad con Android (@SerialName("resumen") val resumenVisual)
    resumen_visual: str = ""
    detalle_hablado: str = ""
    alertas_seguridad: list[str] = []
    nota_seguridad: str | None = None
    temporizador_segundos: int | None = None
    temporizador_nombre: str | None = None
    estufa: str | None = None
    imagen: str | None = None
    imagen_url: str | None = None
    audio_url: str | None = None


class RecetaDetalle(RecetaResumen):
    ingredientes: IngredientesAgrupados
    pasos: list[PasoOut]


# ---------- Conversación ----------
class ConversacionPeticion(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    dispositivo_id: str | None = Field(default=None, alias="androidId")
    pregunta: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=1000)]
    receta_titulo: Annotated[str, StringConstraints(max_length=200)] | None = Field(default=None, alias="recetaTitulo")
    paso_texto: Annotated[str, StringConstraints(max_length=2000)] | None = Field(default=None, alias="pasoTexto")
    con_voz: bool = Field(default=False, description="Si es true, se genera audio con ElevenLabs")


class ContactoEmergencia(BaseModel):
    nombre: str | None = None
    telefono: str | None = None


class ConversacionRespuesta(BaseModel):
    respuesta: str
    hecho_nuevo: str | None = None  # Interoperabilidad con Android (@SerialName("hecho_nuevo") val hechoNuevo)
    hecho_guardado: str | None = None
    alerta_emergencia: bool = False
    contacto_emergencia: ContactoEmergencia | None = None
    audio_url: str | None = None
    fuente: Literal["gemini", "respaldo"] = "gemini"


# ---------- Perfil ----------
class HechoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    categoria: str
    texto: str
    origen: str
    creado_en: datetime


class PerfilOut(BaseModel):
    dispositivo_id: str
    androidId: str | None = None  # Interoperabilidad con Android (PerfilUsuario)
    nombre: str | None
    tratamiento: str
    contacto_nombre: str | None
    contacto_telefono: str | None
    preferencias: dict
    alergias: list[HechoOut]
    condiciones_salud: list[HechoOut]
    recuerdos: list[HechoOut]
    creado_en: datetime


class PerfilActualizar(BaseModel):
    """Actualización parcial: sólo se modifican los campos enviados."""

    model_config = ConfigDict(populate_by_name=True)

    dispositivo_id: str | None = Field(default=None, alias="androidId")
    nombre: Annotated[str, StringConstraints(strip_whitespace=True, max_length=80)] | None = None
    tratamiento: Literal["usted", "tú", "tu"] | None = None
    contacto_nombre: Annotated[str, StringConstraints(strip_whitespace=True, max_length=80)] | None = None
    contacto_telefono: Annotated[str, StringConstraints(strip_whitespace=True, max_length=30)] | None = None
    preferencias: dict | None = None
    # Si se envían, REEMPLAZAN la lista completa de esa categoría
    alergias: list[TextoCorto] | None = Field(default=None, max_length=30)
    condiciones_salud: list[TextoCorto] | None = Field(default=None, max_length=30)


# ---------- Voz ----------
class VozPeticion(BaseModel):
    texto: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=1000)]
    persistente: bool = Field(
        default=False, description="true para frases estáticas/frecuentes (nunca se podan del caché)"
    )


class Salud(BaseModel):
    estado: Literal["ok", "degradado"]
    base_datos: Literal["ok", "error"]
    motor: str
    gemini: bool
    elevenlabs: bool
    version: str
