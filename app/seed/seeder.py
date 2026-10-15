"""Siembra idempotente del catálogo de recetas."""

import logging

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Ingrediente, Paso, Receta
from app.seed.recetas_data import RECETAS

log = logging.getLogger(__name__)


async def sembrar_recetas(session: AsyncSession) -> int:
    """Inserta las recetas base sólo si la tabla está vacía. Devuelve cuántas insertó."""
    total = await session.scalar(select(func.count(Receta.id)))
    if total:
        log.info("Catálogo ya presente (%s recetas); no se siembra.", total)
        return 0

    for datos in RECETAS:
        slug = datos["slug"]
        receta = Receta(
            slug=slug,
            titulo=datos["titulo"],
            descripcion=datos["descripcion"],
            porciones=datos["porciones"],
            tiempo_total_min=datos["tiempo_total_min"],
            dificultad=datos["dificultad"],
            imagen=f"{slug}.jpg",
        )
        orden = 0
        for categoria in ("base", "salsa", "servicio"):
            for nombre, cantidad in datos["ingredientes"].get(categoria, []):
                orden += 1
                receta.ingredientes.append(
                    Ingrediente(categoria=categoria, nombre=nombre, cantidad=cantidad, orden=orden)
                )
        for i, paso in enumerate(datos["pasos"], start=1):
            paso_copia = dict(paso)
            img = paso_copia.pop("imagen", None) or f"{slug}-{i}.jpg"
            receta.pasos.append(Paso(orden=i, imagen=img, **paso_copia))
        session.add(receta)

    await session.commit()
    log.info("Sembradas %s recetas base.", len(RECETAS))
    return len(RECETAS)
