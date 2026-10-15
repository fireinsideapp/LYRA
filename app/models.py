"""Modelos ORM de Lyra."""

from datetime import datetime, timezone

from sqlalchemy import JSON, Boolean, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


def ahora() -> datetime:
    return datetime.now(timezone.utc)


# Categorías válidas de ingredientes y de hechos de memoria
CATEGORIAS_INGREDIENTE = ("base", "salsa", "servicio")
CATEGORIAS_HECHO = ("personal", "salud", "alergia", "preferencia")


class Dispositivo(Base):
    """Perfil de la persona, identificado sólo por el ANDROID_ID (sin contraseñas)."""

    __tablename__ = "dispositivos"

    id: Mapped[int] = mapped_column(primary_key=True)
    dispositivo_id: Mapped[str] = mapped_column(String(128), unique=True, index=True)
    nombre: Mapped[str | None] = mapped_column(String(80))
    tratamiento: Mapped[str] = mapped_column(String(10), default="usted")  # "usted" | "tú"
    contacto_nombre: Mapped[str | None] = mapped_column(String(80))
    contacto_telefono: Mapped[str | None] = mapped_column(String(30))
    preferencias: Mapped[dict] = mapped_column(JSON, default=dict)
    creado_en: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=ahora)
    actualizado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=ahora, onupdate=ahora
    )

    hechos: Mapped[list["HechoMemoria"]] = relationship(
        back_populates="dispositivo", cascade="all, delete-orphan", lazy="raise"
    )
    mensajes: Mapped[list["Mensaje"]] = relationship(
        back_populates="dispositivo", cascade="all, delete-orphan", lazy="raise"
    )


class Receta(Base):
    __tablename__ = "recetas"

    id: Mapped[int] = mapped_column(primary_key=True)
    slug: Mapped[str] = mapped_column(String(120), unique=True, index=True)
    titulo: Mapped[str] = mapped_column(String(200))
    descripcion: Mapped[str] = mapped_column(Text)
    porciones: Mapped[int] = mapped_column(Integer)
    tiempo_total_min: Mapped[int] = mapped_column(Integer)
    dificultad: Mapped[str] = mapped_column(String(20), default="fácil")
    imagen: Mapped[str | None] = mapped_column(String(200))

    ingredientes: Mapped[list["Ingrediente"]] = relationship(
        back_populates="receta",
        cascade="all, delete-orphan",
        order_by="Ingrediente.orden",
        lazy="raise",
    )
    pasos: Mapped[list["Paso"]] = relationship(
        back_populates="receta",
        cascade="all, delete-orphan",
        order_by="Paso.orden",
        lazy="raise",
    )


class Ingrediente(Base):
    __tablename__ = "ingredientes"

    id: Mapped[int] = mapped_column(primary_key=True)
    receta_id: Mapped[int] = mapped_column(ForeignKey("recetas.id", ondelete="CASCADE"), index=True)
    categoria: Mapped[str] = mapped_column(String(20))  # base | salsa | servicio
    nombre: Mapped[str] = mapped_column(String(120))
    cantidad: Mapped[str] = mapped_column(String(80))
    orden: Mapped[int] = mapped_column(Integer, default=0)

    receta: Mapped[Receta] = relationship(back_populates="ingredientes", lazy="raise")


class Paso(Base):
    __tablename__ = "pasos"

    id: Mapped[int] = mapped_column(primary_key=True)
    receta_id: Mapped[int] = mapped_column(ForeignKey("recetas.id", ondelete="CASCADE"), index=True)
    orden: Mapped[int] = mapped_column(Integer)
    resumen_visual: Mapped[str] = mapped_column(String(200))
    detalle_hablado: Mapped[str] = mapped_column(Text)
    # Etiquetas: estufa, aceite, cuchillo, agua_caliente, licuadora, horno, vapor
    alertas_seguridad: Mapped[list] = mapped_column(JSON, default=list)
    nota_seguridad: Mapped[str | None] = mapped_column(Text)
    temporizador_segundos: Mapped[int | None] = mapped_column(Integer)
    imagen: Mapped[str | None] = mapped_column(String(200))

    receta: Mapped[Receta] = relationship(back_populates="pasos", lazy="raise")


class HechoMemoria(Base):
    """Memoria afectiva: recuerdos personales y condiciones de salud/alergias."""

    __tablename__ = "hechos_memoria"

    id: Mapped[int] = mapped_column(primary_key=True)
    dispositivo_pk: Mapped[int] = mapped_column(
        ForeignKey("dispositivos.id", ondelete="CASCADE"), index=True
    )
    categoria: Mapped[str] = mapped_column(String(20), default="personal")
    texto: Mapped[str] = mapped_column(String(500))
    texto_normalizado: Mapped[str] = mapped_column(String(500), index=True)
    origen: Mapped[str] = mapped_column(String(20), default="conversacion")  # conversacion | perfil
    activo: Mapped[bool] = mapped_column(Boolean, default=True)
    creado_en: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=ahora)

    dispositivo: Mapped[Dispositivo] = relationship(back_populates="hechos", lazy="raise")


class Mensaje(Base):
    __tablename__ = "mensajes"

    id: Mapped[int] = mapped_column(primary_key=True)
    dispositivo_pk: Mapped[int] = mapped_column(
        ForeignKey("dispositivos.id", ondelete="CASCADE"), index=True
    )
    rol: Mapped[str] = mapped_column(String(10))  # usuario | lyra
    contenido: Mapped[str] = mapped_column(Text)
    receta_titulo: Mapped[str | None] = mapped_column(String(200))
    paso_texto: Mapped[str | None] = mapped_column(Text)
    creado_en: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=ahora, index=True)

    dispositivo: Mapped[Dispositivo] = relationship(back_populates="mensajes", lazy="raise")
