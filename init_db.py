"""Script CLI para inicializar la base de datos y cargar las 20 recetas base.

Uso:
    python init_db.py
"""

import asyncio
import logging
import sys

from app.config import get_settings
from app.database import ES_POSTGRES, SessionLocal, crear_tablas, engine
from app.seed.seeder import sembrar_recetas

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
log = logging.getLogger("init_db")


async def main() -> None:
    settings = get_settings()
    motor = "PostgreSQL" if ES_POSTGRES else "SQLite"
    log.info("Conectando a base de datos (%s)...", motor)

    try:
        log.info("Creando tablas si no existen...")
        await crear_tablas()
        log.info("✓ Tablas verificadas y listas.")

        log.info("Comprobando catálogo de recetas base...")
        async with SessionLocal() as session:
            insertadas = await sembrar_recetas(session)
            if insertadas > 0:
                log.info("✓ Se sembraron exitosamente %s recetas mexicanas tradicionales.", insertadas)
            else:
                log.info("✓ El catálogo ya cuenta con recetas. No se requirió siembra.")

    except Exception as e:
        log.error("Error al inicializar la base de datos: %s", e)
        sys.exit(1)
    finally:
        await engine.dispose()

    log.info("¡Base de datos lista para operar con Lyra!")


if __name__ == "__main__":
    asyncio.run(main())
