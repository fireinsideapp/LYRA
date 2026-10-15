-- =============================================================================
-- LYRA: Asistente de Cocina Humana y Accesible para Personas de la Tercera Edad
-- Script DDL de Base de Datos (PostgreSQL)
-- =============================================================================

-- 1. TABLA: dispositivos (identidad invisible por ANDROID_ID)
CREATE TABLE IF NOT EXISTS dispositivos (
    id SERIAL PRIMARY KEY,
    dispositivo_id VARCHAR(128) NOT NULL UNIQUE,
    nombre VARCHAR(80),
    tratamiento VARCHAR(10) NOT NULL DEFAULT 'usted',
    contacto_nombre VARCHAR(80),
    contacto_telefono VARCHAR(30),
    preferencias JSONB NOT NULL DEFAULT '{}'::jsonb,
    creado_en TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    actualizado_en TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS ix_dispositivos_dispositivo_id 
    ON dispositivos (dispositivo_id);


-- 2. TABLA: recetas (catálogo base de platillos tradicionales)
CREATE TABLE IF NOT EXISTS recetas (
    id SERIAL PRIMARY KEY,
    slug VARCHAR(120) NOT NULL UNIQUE,
    titulo VARCHAR(200) NOT NULL,
    descripcion TEXT NOT NULL,
    porciones INTEGER NOT NULL,
    tiempo_total_min INTEGER NOT NULL,
    dificultad VARCHAR(20) NOT NULL DEFAULT 'fácil',
    imagen VARCHAR(200)
);

CREATE INDEX IF NOT EXISTS ix_recetas_slug 
    ON recetas (slug);


-- 3. TABLA: ingredientes (categorizados en base, salsa y servicio)
CREATE TABLE IF NOT EXISTS ingredientes (
    id SERIAL PRIMARY KEY,
    receta_id INTEGER NOT NULL REFERENCES recetas(id) ON DELETE CASCADE,
    categoria VARCHAR(20) NOT NULL, -- 'base', 'salsa', 'servicio'
    nombre VARCHAR(120) NOT NULL,
    cantidad VARCHAR(80) NOT NULL,
    orden INTEGER NOT NULL DEFAULT 0
);

CREATE INDEX IF NOT EXISTS ix_ingredientes_receta_id 
    ON ingredientes (receta_id);


-- 4. TABLA: pasos (dualidad resumen visual para pantalla + detalle hablado para voz)
CREATE TABLE IF NOT EXISTS pasos (
    id SERIAL PRIMARY KEY,
    receta_id INTEGER NOT NULL REFERENCES recetas(id) ON DELETE CASCADE,
    orden INTEGER NOT NULL,
    resumen_visual VARCHAR(200) NOT NULL,
    detalle_hablado TEXT NOT NULL,
    alertas_seguridad JSONB NOT NULL DEFAULT '[]'::jsonb,
    nota_seguridad TEXT,
    temporizador_segundos INTEGER,
    imagen VARCHAR(200)
);

CREATE INDEX IF NOT EXISTS ix_pasos_receta_id 
    ON pasos (receta_id);


-- 5. TABLA: hechos_memoria (recuerdos personales, salud y alergias)
CREATE TABLE IF NOT EXISTS hechos_memoria (
    id SERIAL PRIMARY KEY,
    dispositivo_pk INTEGER NOT NULL REFERENCES dispositivos(id) ON DELETE CASCADE,
    categoria VARCHAR(20) NOT NULL DEFAULT 'personal', -- 'personal', 'salud', 'alergia', 'preferencia'
    texto VARCHAR(500) NOT NULL,
    texto_normalizado VARCHAR(500) NOT NULL,
    origen VARCHAR(20) NOT NULL DEFAULT 'conversacion', -- 'conversacion', 'perfil'
    activo BOOLEAN NOT NULL DEFAULT TRUE,
    creado_en TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS ix_hechos_memoria_dispositivo_pk 
    ON hechos_memoria (dispositivo_pk);

CREATE INDEX IF NOT EXISTS ix_hechos_memoria_texto_normalizado 
    ON hechos_memoria (texto_normalizado);


-- 6. TABLA: mensajes (historial conversacional con Lyra)
CREATE TABLE IF NOT EXISTS mensajes (
    id SERIAL PRIMARY KEY,
    dispositivo_pk INTEGER NOT NULL REFERENCES dispositivos(id) ON DELETE CASCADE,
    rol VARCHAR(10) NOT NULL, -- 'usuario', 'lyra'
    contenido TEXT NOT NULL,
    receta_titulo VARCHAR(200),
    paso_texto TEXT,
    creado_en TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS ix_mensajes_dispositivo_pk 
    ON mensajes (dispositivo_pk);

CREATE INDEX IF NOT EXISTS ix_mensajes_creado_en 
    ON mensajes (creado_en);
