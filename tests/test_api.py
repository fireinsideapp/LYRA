"""Pruebas de integración con SQLite temporal y Gemini/ElevenLabs simulados."""

import os
import tempfile
from pathlib import Path

_tmp = Path(tempfile.mkdtemp(prefix="lyra_test_"))
os.environ["DATABASE_URL"] = f"sqlite+aiosqlite:///{(_tmp / 'test.db').as_posix()}"
os.environ["AUDIO_CACHE_DIR"] = str(_tmp / "audio")
os.environ["GEMINI_API_KEY"] = ""
os.environ["ELEVENLABS_API_KEY"] = ""
os.environ["ELEVENLABS_VOICE_ID"] = ""

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from app.main import app  # noqa: E402
from app.services.gemini import ClienteGemini, ResultadoIA  # noqa: E402
from app.services.texto import detectar_emergencia  # noqa: E402

DID = "test-android-0001"


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


def test_salud(client):
    r = client.get("/api/salud")
    assert r.status_code == 200
    assert r.json()["base_datos"] == "ok"


def test_listado_recetas(client):
    r = client.get("/api/recetas")
    assert r.status_code == 200
    assert len(r.json()) >= 20


def test_detalle_receta(client):
    r = client.get("/api/recetas/huevos-a-la-mexicana")
    assert r.status_code == 200
    d = r.json()
    assert d["ingredientes"]["base"] and d["ingredientes"]["salsa"]
    assert any("estufa" in p["alertas_seguridad"] for p in d["pasos"])
    assert client.get("/api/recetas/no-existe").status_code == 404


def test_imagen_path_traversal(client):
    assert client.get("/recetas/..%2F..%2Fapp%2Fconfig.py").status_code == 404
    assert client.get("/recetas/no-existe.jpg").status_code == 404


def test_perfil_alergias(client):
    r = client.put("/api/perfil", json={
        "dispositivo_id": DID, "nombre": "Doña Carmen", "tratamiento": "usted",
        "contacto_nombre": "Roberto", "contacto_telefono": "5551234567",
        "alergias": ["Alérgica a la nuez"], "condiciones_salud": ["Hipertensa: evitar exceso de sal"],
    })
    assert r.status_code == 200, r.text
    p = r.json()
    assert p["nombre"] == "Doña Carmen"
    assert [h["texto"] for h in p["alergias"]] == ["Alérgica a la nuez"]
    # Reemplazo de la lista
    r = client.put("/api/perfil", json={"dispositivo_id": DID, "alergias": ["Alérgica al cacahuate"]})
    assert [h["texto"] for h in r.json()["alergias"]] == ["Alérgica al cacahuate"]
    assert r.json()["nombre"] == "Doña Carmen"  # actualización parcial


def test_conversacion_respaldo_sin_gemini(client):
    r = client.post("/api/conversacion", json={"dispositivo_id": DID, "pregunta": "¿Cuánta sal le pongo?"})
    assert r.status_code == 200
    assert r.json()["fuente"] == "respaldo"


def test_conversacion_emergencia(client):
    r = client.post("/api/conversacion", json={"dispositivo_id": DID, "pregunta": "Ay, me caí en la cocina"})
    d = r.json()
    assert d["alerta_emergencia"] is True
    assert d["contacto_emergencia"]["nombre"] == "Roberto"
    assert "Roberto" in d["respuesta"]


def test_conversacion_guarda_hecho(client, monkeypatch):
    capturado = {}

    async def falso(self, sistema, historial, pregunta):
        capturado["sistema"] = sistema
        capturado["historial"] = historial
        return ResultadoIA("¡Qué bonito! Roberto va a disfrutar mucho sus chilaquiles.",
                           "Su hijo Roberto la visita los domingos", "personal")

    monkeypatch.setattr(ClienteGemini, "generar", falso)
    cuerpo = {"dispositivo_id": DID, "receta_titulo": "Chilaquiles verdes",
              "paso_texto": "Licuar la salsa", "pregunta": "Mi hijo Roberto viene el domingo"}
    d = client.post("/api/conversacion", json=cuerpo).json()
    assert d["fuente"] == "gemini"
    assert d["hecho_guardado"] == "Su hijo Roberto la visita los domingos"
    assert "Alérgica al cacahuate" in capturado["sistema"]
    assert "Chilaquiles verdes" in capturado["sistema"]
    assert capturado["historial"], "debe incluir historial previo"

    # No se duplica
    d2 = client.post("/api/conversacion", json=cuerpo).json()
    assert d2["hecho_guardado"] is None
    recuerdos = client.get("/api/perfil", params={"dispositivo_id": DID}).json()["recuerdos"]
    assert len(recuerdos) == 1

    # Olvidar
    hid = recuerdos[0]["id"]
    assert client.delete(f"/api/perfil/hechos/{hid}", params={"dispositivo_id": DID}).status_code == 204
    assert client.get("/api/perfil", params={"dispositivo_id": DID}).json()["recuerdos"] == []


def test_voz_sin_configurar(client):
    assert client.post("/api/voz", json={"texto": "Hola"}).status_code == 503
    assert client.get("/api/voz/audio/../../x.mp3").status_code == 404


def test_flujo_voz_completo_con_mock(client, monkeypatch):
    voz = app.state.voz
    # Simular configuración válida de ElevenLabs
    monkeypatch.setattr(voz.s, "elevenlabs_api_key", "test_key")
    monkeypatch.setattr(voz.s, "elevenlabs_voice_id", "test_voice")

    async def mock_llamar_api(texto):
        return b"ID3\x03\x00\x00\x00\x00\x00\x00dummy-mp3-audio-bytes"

    monkeypatch.setattr(voz, "_llamar_api", mock_llamar_api)

    # 1. Detalle de receta ahora incluye URLs de audio
    r = client.get("/api/recetas/huevos-a-la-mexicana")
    assert r.status_code == 200
    paso1 = r.json()["pasos"][0]
    assert paso1["audio_url"] is not None
    assert "/api/recetas/huevos-a-la-mexicana/pasos/1/audio" in paso1["audio_url"]

    # 2. Descargar audio del paso (primera vez MISS, segunda vez HIT)
    r_audio = client.get("/api/recetas/huevos-a-la-mexicana/pasos/1/audio")
    assert r_audio.status_code == 200
    assert r_audio.headers["content-type"] == "audio/mpeg"
    assert r_audio.headers["X-Audio-Cache"] == "MISS"
    assert r_audio.content == b"ID3\x03\x00\x00\x00\x00\x00\x00dummy-mp3-audio-bytes"

    r_audio_hit = client.get("/api/recetas/huevos-a-la-mexicana/pasos/1/audio")
    assert r_audio_hit.status_code == 200
    assert r_audio_hit.headers["X-Audio-Cache"] == "HIT"

    # 3. Endpoint /api/voz
    r_voz = client.post("/api/voz", json={"texto": "Buenos días, vamos a cocinar con calma."})
    assert r_voz.status_code == 200
    assert r_voz.headers["X-Audio-Cache"] == "MISS"
    assert "X-Audio-Url" in r_voz.headers
    url_audio = r_voz.headers["X-Audio-Url"]

    # Obtener el audio guardado por su URL
    nombre_archivo = url_audio.split("/")[-1]
    r_cache = client.get(f"/api/voz/audio/{nombre_archivo}")
    assert r_cache.status_code == 200
    assert r_cache.content == b"ID3\x03\x00\x00\x00\x00\x00\x00dummy-mp3-audio-bytes"

    # 4. Conversación con voz activa (con_voz=True)
    r_conv = client.post("/api/conversacion", json={
        "dispositivo_id": DID,
        "pregunta": "¿Cómo sé si el aceite ya está caliente?",
        "con_voz": True
    })
    assert r_conv.status_code == 200
    assert r_conv.json()["audio_url"] is not None

    # 5. Precalentamiento de frases frecuentes
    r_precalentar = client.post("/api/voz/precalentar")
    assert r_precalentar.status_code == 200
    assert r_precalentar.json()["generadas"] > 0
    assert r_precalentar.json()["errores"] == []


def test_validacion_dispositivo(client):
    assert client.get("/api/perfil", params={"dispositivo_id": "x"}).status_code == 422


def test_interpretar_json_gemini():
    data = {"candidates": [{"content": {"parts": [{"text":
        '{"respuesta": "Uno. Dos. Tres. Cuatro.", "hecho_nuevo": "null", "categoria_hecho": null}'}]}}]}
    r = ClienteGemini._interpretar(data)
    assert r.respuesta == "Uno. Dos. Tres." and r.hecho_nuevo is None


@pytest.mark.parametrize("texto,esperado", [
    ("me duele el pecho", True), ("Me quemé con el aceite", True), ("estoy mareado", True),
    ("¿a qué fuego lo pongo?", False), ("¿cuánta pechuga uso?", False),
])
def test_detectar_emergencia(texto, esperado):
    assert detectar_emergencia(texto) is esperado


def test_compatibilidad_android_retrofit(client):
    # 1. Android sincroniza perfil con POST y campo 'androidId'
    r_perfil = client.post("/api/perfil", json={
        "androidId": "android-dispositivo-xyz",
        "nombre": "Doña Lupita",
        "alergias": ["camarón", "nueces"]
    })
    assert r_perfil.status_code == 200
    data_perfil = r_perfil.json()
    assert data_perfil["androidId"] == "android-dispositivo-xyz"
    assert data_perfil["nombre"] == "Doña Lupita"
    assert len(data_perfil["alergias"]) == 2

    # 2. Android llama a conversar sin enviar dispositivo_id
    r_conv = client.post("/api/conversacion", json={
        "receta_titulo": "Arroz rojo",
        "paso_texto": "Dorar el arroz",
        "pregunta": "¿Cuándo sé que ya está bien doradito?"
    })
    assert r_conv.status_code == 200
    data_conv = r_conv.json()
    assert "respuesta" in data_conv
    assert "hecho_nuevo" in data_conv  # Android espera hecho_nuevo

    # 3. Paso de receta contiene campos requeridos por Kotlin Paso (texto, resumen, grupo)
    r_receta = client.get("/api/recetas/arroz-rojo")
    assert r_receta.status_code == 200
    data_receta = r_receta.json()
    assert len(data_receta["pasos"]) > 0
    paso = data_receta["pasos"][0]
    assert "texto" in paso and paso["texto"] != ""
    assert "resumen" in paso
    ingrediente = data_receta["ingredientes"]["base"][0]
    assert "grupo" in ingrediente and ingrediente["grupo"] != ""
