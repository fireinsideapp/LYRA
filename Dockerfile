# syntax=docker/dockerfile:1
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Dependencias primero para aprovechar la caché de capas
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app ./app
COPY static ./static

# Usuario sin privilegios
RUN useradd --create-home --uid 10001 lyra \
    && mkdir -p /app/audio_cache \
    && chown -R lyra:lyra /app
USER lyra

ENV PORT=8000
EXPOSE 8000

CMD ["python", "-m", "app.main"]
