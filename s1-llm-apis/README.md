<!-- Generado desde sesion-1.html con tools/sync_exercises.py. No editar a mano. -->

# Ejercicios · Integración con LLMs: APIs de OpenAI, Gemini y Claude

**Entregable:** E1. `llm_client.py` funcionando con tres proveedores y `comparativa.csv` con su análisis en `analisis.md`. Entrega en la carpeta `e1/` de tu repositorio de entregas hasta el viernes 16 de octubre a las 23:59.

## Prácticas

- [P1. Entorno](P1-entorno.md)
- [P2. El mismo encargo a tres proveedores](P2-el-mismo-encargo-a-tres-proveedores.md)
- [P3. Una interfaz común](P3-una-interfaz-comun.md)
- [P4. Comparativa de proveedores](P4-comparativa-de-proveedores.md)
- [P5. Streaming y modelo local](P5-streaming-y-modelo-local.md)

## Código

Los scripts de esta carpeta son los del kit del bloque. Los marcados como esqueleto tienen partes por completar (busca `TODO`):

- [`crear_bd.py`](crear_bd.py)
- [`s1_hola_tres.py`](s1_hola_tres.py)
- [`llm_client.py`](llm_client.py): esqueleto, lo completas en P3
- [`s1_comparativa.py`](s1_comparativa.py): esqueleto, lo completas en P4
- [`s1_streaming.py`](s1_streaming.py)

## Puesta en marcha

Trabaja siempre en tu carpeta `bloque4`, la que preparaste en la sesión 0 con la guía de puesta a punto:
un solo entorno virtual (`.venv`) y un solo `.env` para todo el bloque. No crees otros.

1. Copia los ficheros de esta carpeta en tu carpeta `bloque4`. Si alguno ya existe, sustitúyelo:
   es la versión de esta sesión. **No** copies `.env.example` encima de tu `.env`.
2. Abre la terminal en `bloque4`, activa el entorno y actualiza las dependencias:

```bash
source .venv/bin/activate        # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

¿Aún no tienes la carpeta `bloque4`? Sigue antes la guía de puesta a punto de la sesión 0.
