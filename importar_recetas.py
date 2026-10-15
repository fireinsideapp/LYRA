"""Script para importar las 28 recetas JSON a la base de datos PostgreSQL local 'Lyra'."""

import asyncio
import json
import logging
import re
import shutil
from pathlib import Path
import asyncpg

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
log = logging.getLogger("importador")

from app.config import get_settings

settings = get_settings()
_raw_url = settings.database_url
if "+asyncpg" in _raw_url:
    DB_URL = _raw_url.replace("+asyncpg", "")
elif _raw_url.startswith("sqlite"):
    DB_URL = "postgresql://postgres:root@127.0.0.1:5432/Lyra"
else:
    DB_URL = _raw_url

JSON_DIR = Path(r"c:\Users\urien\OneDrive\Desktop\Proyectos Universidad\IHM\Verdadero_asistente_cocina\Lira\backend\datos_iniciales\recetas")
ASSETS_IMG_DIR = Path(r"c:\Users\urien\OneDrive\Desktop\Proyectos Universidad\IHM\LYRA\app\src\main\assets\recetas")
STATIC_IMG_DIR = Path(r"c:\Users\urien\OneDrive\Desktop\Proyectos Universidad\IHM\LYRA\backend\static\recetas")


def categorizar_ingrediente(grupo: str) -> str:
    g = grupo.lower().strip()
    if any(k in g for k in ["salsa", "caldillo", "caldo", "sabor", "sazonador"]):
        return "salsa"
    if any(k in g for k in ["servir", "acompañamiento", "complemento", "para agregar", "servicio", "decoración"]):
        return "servicio"
    return "base"


def extraer_resumen(texto: str) -> str:
    # Primera frase
    frases = re.split(r"(?<=[.!?])\s+", texto.strip())
    primera = frases[0] if frases else texto
    if len(primera) > 100:
        return primera[:97].strip() + "..."
    return primera.strip()


def extraer_alertas(paso: dict) -> list[str]:
    alertas = set()
    texto = (paso.get("texto", "") + " " + (paso.get("nota_seguridad") or "")).lower()
    estufa = (paso.get("estufa") or "").lower()

    if estufa in ["encendida", "apagar"] or "estufa" in texto or "lumbre" in texto or "fuego" in texto:
        alertas.add("estufa")
    if "aceite" in texto or "freír" in texto or "fríelo" in texto:
        alertas.add("aceite")
    if "cuchillo" in texto or "pica" in texto or "corta" in texto or "reban" in texto:
        alertas.add("cuchillo")
    if "licuadora" in texto or "licúa" in texto or "licua" in texto:
        alertas.add("licuadora")
    if "agua caliente" in texto or "hirviendo" in texto or "hervir" in texto or "salpicar" in texto:
        alertas.add("agua_caliente")
    if "vapor" in texto:
        alertas.add("vapor")
    if "horno" in texto:
        alertas.add("horno")

    return sorted(list(alertas))


def limpiar_nombre_imagen(img_path: str | None) -> str | None:
    if not img_path:
        return None
    return img_path.strip().split("/")[-1]


async def importar():
    log.info("Conectando a PostgreSQL: %s", DB_URL)
    conn = await asyncpg.connect(DB_URL)

    # 1. Copiar imágenes a backend/static/recetas si existen
    STATIC_IMG_DIR.mkdir(parents=True, exist_ok=True)
    if ASSETS_IMG_DIR.exists():
        copiadas = 0
        for img in ASSETS_IMG_DIR.glob("*.*"):
            dest = STATIC_IMG_DIR / img.name
            if not dest.exists():
                shutil.copy2(img, dest)
                copiadas += 1
        log.info("Imágenes sincronizadas a static/recetas: %d copiadas", copiadas)

    # 2. Limpiar recetas previas para inserción fresca o reemplazo
    recetas_archivos = sorted(list(JSON_DIR.glob("*.json")))
    log.info("Encontradas %d recetas para importar en %s", len(recetas_archivos), JSON_DIR)

    # Transacción para consistencia total
    async with conn.transaction():
        # Borrar registros previos para asegurar catálogo limpio y actualizado
        await conn.execute("DELETE FROM recetas;")
        log.info("Tabla recetas reiniciada (cascade a ingredientes y pasos).")

        total_ingredientes = 0
        total_pasos = 0

        for f in recetas_archivos:
            data = json.loads(f.read_text(encoding="utf-8"))
            slug = data["slug"]
            titulo = data["titulo"]
            descripcion = data.get("descripcion", "")
            porciones_raw = data.get("porciones")
            porciones = int(porciones_raw) if porciones_raw is not None else 2

            # Calcular tiempo total en minutos
            timers_seg = [p.get("temporizador_segundos") for p in data.get("pasos", []) if p.get("temporizador_segundos")]
            tiempo_total_min = (sum(timers_seg) // 60) + 12
            if tiempo_total_min < 15:
                tiempo_total_min = 15

            dificultad = "media" if tiempo_total_min > 40 or len(data.get("pasos", [])) > 15 else "fácil"

            # Imagen de portada (primer paso con imagen)
            imagen_portada = None
            for p in data.get("pasos", []):
                if p.get("imagen"):
                    imagen_portada = limpiar_nombre_imagen(p.get("imagen"))
                    break

            # Insertar receta
            receta_id = await conn.fetchval(
                """
                INSERT INTO recetas (slug, titulo, descripcion, porciones, tiempo_total_min, dificultad, imagen)
                VALUES ($1, $2, $3, $4, $5, $6, $7)
                RETURNING id;
                """,
                slug, titulo, descripcion, porciones, tiempo_total_min, dificultad, imagen_portada
            )

            # Insertar ingredientes
            for idx, ing in enumerate(data.get("ingredientes", []), start=1):
                cat = categorizar_ingrediente(ing.get("grupo", "Base"))
                nombre = ing.get("nombre", "").strip()
                cantidad = ing.get("cantidad", "").strip() or "al gusto"
                await conn.execute(
                    """
                    INSERT INTO ingredientes (receta_id, categoria, nombre, cantidad, orden)
                    VALUES ($1, $2, $3, $4, $5);
                    """,
                    receta_id, cat, nombre, cantidad, idx
                )
                total_ingredientes += 1

            # Insertar pasos
            for idx, paso in enumerate(data.get("pasos", []), start=1):
                orden = int(paso.get("orden", idx))
                detalle_hablado = paso.get("texto", "").strip()
                resumen_visual = paso.get("resumen") or extraer_resumen(detalle_hablado)
                alertas = extraer_alertas(paso)
                nota_seguridad = paso.get("nota_seguridad")
                temporizador_segundos = paso.get("temporizador_segundos")
                imagen_paso = limpiar_nombre_imagen(paso.get("imagen"))

                await conn.execute(
                    """
                    INSERT INTO pasos (receta_id, orden, resumen_visual, detalle_hablado, alertas_seguridad, nota_seguridad, temporizador_segundos, imagen)
                    VALUES ($1, $2, $3, $4, $5::jsonb, $6, $7, $8);
                    """,
                    receta_id, orden, resumen_visual, detalle_hablado, json.dumps(alertas), nota_seguridad, temporizador_segundos, imagen_paso
                )
                total_pasos += 1

            log.info("✓ Insertada: %-30s (%d ing, %d pasos)", slug, len(data.get("ingredientes", [])), len(data.get("pasos", [])))

    log.info("=====================================================")
    log.info("¡IMPORTACIÓN COMPLETADA CON ÉXITO!")
    log.info("Recetas importadas:    %d", len(recetas_archivos))
    log.info("Ingredientes creados: %d", total_ingredientes)
    log.info("Pasos creados:        %d", total_pasos)
    log.info("=====================================================")

    await conn.close()


if __name__ == "__main__":
    asyncio.run(importar())
