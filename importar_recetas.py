"""Script completo para actualizar e importar las 28 recetas JSON a:
1. PostgreSQL local 'Lyra' (eliminando catálogo anterior)
2. SQLite local 'lyra.db'
3. Android assets 'app/src/main/assets/recetas_json'
4. Módulo de semillas 'app/seed/recetas_data.py' (para Railway)
"""

import asyncio
import json
import logging
import pprint
import re
import shutil
import sqlite3
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
APP_JSON_DIR = Path(r"c:\Users\urien\OneDrive\Desktop\Proyectos Universidad\IHM\LYRA\app\src\main\assets\recetas_json")
ASSETS_IMG_DIR = Path(r"c:\Users\urien\OneDrive\Desktop\Proyectos Universidad\IHM\LYRA\app\src\main\assets\recetas")
STATIC_IMG_DIR = Path(r"c:\Users\urien\OneDrive\Desktop\Proyectos Universidad\IHM\LYRA\backend\static\recetas")
SQLITE_DB = Path(r"c:\Users\urien\OneDrive\Desktop\Proyectos Universidad\IHM\LYRA\backend\lyra.db")
RECETAS_DATA_FILE = Path(r"c:\Users\urien\OneDrive\Desktop\Proyectos Universidad\IHM\LYRA\backend\app\seed\recetas_data.py")


def categorizar_ingrediente(grupo: str) -> str:
    g = grupo.lower().strip()
    if any(k in g for k in ["salsa", "caldillo", "caldo", "sabor", "sazonador"]):
        return "salsa"
    if any(k in g for k in ["servir", "acompa", "complemento", "para agregar", "servicio", "decor"]):
        return "servicio"
    return "base"


def extraer_resumen(texto: str) -> str:
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
    recetas_archivos = sorted(list(JSON_DIR.glob("*.json")))
    log.info("Cargando %d recetas desde %s", len(recetas_archivos), JSON_DIR)

    # 1. Copiar imágenes a backend/static/recetas si existen
    STATIC_IMG_DIR.mkdir(parents=True, exist_ok=True)
    if ASSETS_IMG_DIR.exists():
        copiadas = 0
        for img in ASSETS_IMG_DIR.glob("*.*"):
            dest = STATIC_IMG_DIR / img.name
            if not dest.exists():
                shutil.copy2(img, dest)
                copiadas += 1
        if copiadas > 0:
            log.info("Imágenes sincronizadas a static/recetas: %d copiadas", copiadas)

    # 2. Copiar archivos JSON a assets de Android para fallback offline
    if APP_JSON_DIR.exists():
        for f in recetas_archivos:
            # Mantener nombres de archivo limpios y seguros
            safe_name = f.name.replace("", "n").replace("ñ", "n")
            dest = APP_JSON_DIR / safe_name
            shutil.copy2(f, dest)
            if dest.name != f.name:
                shutil.copy2(f, APP_JSON_DIR / f.name)
        log.info("Copiadas recetas actualizadas a Android assets: %s", APP_JSON_DIR)

    # 3. Parsear todas las recetas a estructuras normalizadas
    recetas_parseadas = []
    semillas_recetas = []

    for f in recetas_archivos:
        data = json.loads(f.read_text(encoding="utf-8"))
        slug = data["slug"]
        titulo = data["titulo"]
        descripcion = data.get("descripcion", "")
        porciones_raw = data.get("porciones")
        porciones = int(porciones_raw) if porciones_raw is not None else 2

        timers_seg = [p.get("temporizador_segundos") for p in data.get("pasos", []) if p.get("temporizador_segundos")]
        tiempo_total_min = (sum(timers_seg) // 60) + 12
        if tiempo_total_min < 15:
            tiempo_total_min = 15

        dificultad = "media" if tiempo_total_min > 40 or len(data.get("pasos", [])) > 15 else "fácil"

        imagen_portada = None
        for p in data.get("pasos", []):
            if p.get("imagen"):
                imagen_portada = limpiar_nombre_imagen(p.get("imagen"))
                break

        ingredientes_db = []
        ingredientes_semilla = {"base": [], "salsa": [], "servicio": []}
        for idx, ing in enumerate(data.get("ingredientes", []), start=1):
            cat = categorizar_ingrediente(ing.get("grupo", "Base"))
            nombre = ing.get("nombre", "").strip()
            cantidad = ing.get("cantidad", "").strip() or "al gusto"
            ingredientes_db.append((cat, nombre, cantidad, idx))
            ingredientes_semilla[cat].append((nombre, cantidad))

        pasos_db = []
        pasos_semilla = []
        for idx, paso in enumerate(data.get("pasos", []), start=1):
            orden = int(paso.get("orden", idx))
            detalle_hablado = paso.get("texto", "").strip()
            resumen_visual = paso.get("resumen") or extraer_resumen(detalle_hablado)
            alertas = extraer_alertas(paso)
            nota_seguridad = paso.get("nota_seguridad")
            temporizador_segundos = paso.get("temporizador_segundos")
            imagen_paso = limpiar_nombre_imagen(paso.get("imagen"))

            pasos_db.append((
                orden, resumen_visual, detalle_hablado, alertas,
                nota_seguridad, temporizador_segundos, imagen_paso
            ))
            pasos_semilla.append({
                "resumen_visual": resumen_visual,
                "detalle_hablado": detalle_hablado,
                "alertas_seguridad": alertas,
                "nota_seguridad": nota_seguridad,
                "temporizador_segundos": temporizador_segundos,
                "imagen": imagen_paso,
            })

        recetas_parseadas.append({
            "slug": slug,
            "titulo": titulo,
            "descripcion": descripcion,
            "porciones": porciones,
            "tiempo_total_min": tiempo_total_min,
            "dificultad": dificultad,
            "imagen": imagen_portada,
            "ingredientes": ingredientes_db,
            "pasos": pasos_db,
        })

        semillas_recetas.append({
            "slug": slug,
            "titulo": titulo,
            "descripcion": descripcion,
            "porciones": porciones,
            "tiempo_total_min": tiempo_total_min,
            "dificultad": dificultad,
            "imagen": imagen_portada,
            "ingredientes": ingredientes_semilla,
            "pasos": pasos_semilla,
        })

    # 4. Actualizar módulo de semillas recetas_data.py
    contenido_semillas = (
        '"""Catálogo base: 28 recetas mexicanas tradicionales adaptadas para adultos mayores."""\n\n'
        f"RECETAS: list[dict] = {pprint.pformat(semillas_recetas, indent=4, width=120)}\n"
    )
    RECETAS_DATA_FILE.write_text(contenido_semillas, encoding="utf-8")
    log.info("Archivo de semillas actualizado: %s", RECETAS_DATA_FILE)

    # 5. Insertar en PostgreSQL local
    log.info("Conectando a PostgreSQL: %s", DB_URL)
    conn_pg = await asyncpg.connect(DB_URL)
    async with conn_pg.transaction():
        # Borrar registros previos
        await conn_pg.execute("DELETE FROM pasos;")
        await conn_pg.execute("DELETE FROM ingredientes;")
        await conn_pg.execute("DELETE FROM recetas;")
        log.info("Tablas de recetas en PostgreSQL limpiadas.")

        total_ing = 0
        total_pasos = 0
        for r in recetas_parseadas:
            r_id = await conn_pg.fetchval(
                """
                INSERT INTO recetas (slug, titulo, descripcion, porciones, tiempo_total_min, dificultad, imagen)
                VALUES ($1, $2, $3, $4, $5, $6, $7)
                RETURNING id;
                """,
                r["slug"], r["titulo"], r["descripcion"], r["porciones"],
                r["tiempo_total_min"], r["dificultad"], r["imagen"]
            )
            for cat, nom, cant, idx in r["ingredientes"]:
                await conn_pg.execute(
                    """
                    INSERT INTO ingredientes (receta_id, categoria, nombre, cantidad, orden)
                    VALUES ($1, $2, $3, $4, $5);
                    """,
                    r_id, cat, nom, cant, idx
                )
                total_ing += 1

            for orden, res, det, alertas, nota, t_seg, img in r["pasos"]:
                await conn_pg.execute(
                    """
                    INSERT INTO pasos (receta_id, orden, resumen_visual, detalle_hablado, alertas_seguridad, nota_seguridad, temporizador_segundos, imagen)
                    VALUES ($1, $2, $3, $4, $5::jsonb, $6, $7, $8);
                    """,
                    r_id, orden, res, det, json.dumps(alertas), nota, t_seg, img
                )
                total_pasos += 1

        log.info("PostgreSQL: %d recetas, %d ingredientes, %d pasos insertados.", len(recetas_parseadas), total_ing, total_pasos)
    await conn_pg.close()

    # 6. Actualizar SQLite local (lyra.db)
    if SQLITE_DB.exists():
        sq_conn = sqlite3.connect(str(SQLITE_DB))
        with sq_conn:
            sq_conn.execute("DELETE FROM pasos;")
            sq_conn.execute("DELETE FROM ingredientes;")
            sq_conn.execute("DELETE FROM recetas;")
            for r in recetas_parseadas:
                cur = sq_conn.execute(
                    """
                    INSERT INTO recetas (slug, titulo, descripcion, porciones, tiempo_total_min, dificultad, imagen)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    (r["slug"], r["titulo"], r["descripcion"], r["porciones"], r["tiempo_total_min"], r["dificultad"], r["imagen"])
                )
                r_id = cur.lastrowid
                for cat, nom, cant, idx in r["ingredientes"]:
                    sq_conn.execute(
                        """
                        INSERT INTO ingredientes (receta_id, categoria, nombre, cantidad, orden)
                        VALUES (?, ?, ?, ?, ?);
                        """,
                        (r_id, cat, nom, cant, idx)
                    )
                for orden, res, det, alertas, nota, t_seg, img in r["pasos"]:
                    sq_conn.execute(
                        """
                        INSERT INTO pasos (receta_id, orden, resumen_visual, detalle_hablado, alertas_seguridad, nota_seguridad, temporizador_segundos, imagen)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
                        """,
                        (r_id, orden, res, det, json.dumps(alertas), nota, t_seg, img)
                    )
        sq_conn.close()
        log.info("SQLite (%s): Catálogo actualizado exitosamente.", SQLITE_DB.name)

    log.info("=====================================================")
    log.info("¡ACTUALIZACIÓN COMPLETA FINALIZADA CON ÉXITO!")
    log.info("Recetas:      %d", len(recetas_parseadas))
    log.info("Ingredientes: %d", total_ing)
    log.info("Pasos:        %d", total_pasos)
    log.info("=====================================================")


if __name__ == "__main__":
    asyncio.run(importar())
