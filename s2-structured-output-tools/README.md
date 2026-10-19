<!-- Generado desde sesion-2.html con tools/sync_exercises.py. No editar a mano. -->

# Ejercicios · Salidas estructuradas y uso de herramientas

**Entregable:** E2. Clasificador de correos evaluado con al menos 15 casos en los tres proveedores (tres modelos distintos vía OpenRouter) y asistente con herramientas en dos proveedores, con su análisis en `analisis.md`. Entrega en la carpeta `e2/` de tu repositorio de entregas hasta el domingo 25 de octubre a las 23:59.

## Prácticas

Cada práctica tiene su carpeta, con el enunciado (`README.md`) y el código que usa:

- [P1. Clasificador de correos con evaluación](P1-clasificador-de-correos-con-evaluacion/)
- [P2. Herramientas como funciones Python](P2-herramientas-como-funciones-python/)
- [P3. El bucle de herramientas con OpenAI](P3-el-bucle-de-herramientas-con-openai/)
- [P4. El mismo asistente con Claude o con Gemini](P4-el-mismo-asistente-con-claude-o-con-gemini/)

## Código

Los scripts son los del kit del bloque:

- [`requirements.txt`](requirements.txt)
- [`.env.example`](.env.example)
- [`crear_bd.py`](crear_bd.py)
- [`s2_extraer_correo.py`](P1-clasificador-de-correos-con-evaluacion/s2_extraer_correo.py)
- [`herramientas.py`](P2-herramientas-como-funciones-python/herramientas.py)
- [`s2_chat_herramientas.py`](P3-el-bucle-de-herramientas-con-openai/s2_chat_herramientas.py)

## Puesta en marcha

Trabaja siempre en tu carpeta `bloque4`, la que preparaste en la sesión 0 con la guía de puesta a punto:
un solo entorno virtual (`.venv`) y un solo `.env` para todo el bloque. No crees otros.

1. Copia en tu carpeta `bloque4` los ficheros de esta carpeta y el código de cada práctica, todo junto
   (los scripts se importan unos a otros). Si algún fichero ya existe, sustitúyelo: es la versión de esta
   sesión. **No** copies `.env.example` encima de tu `.env`.
2. Abre la terminal en `bloque4`, activa el entorno y actualiza las dependencias:

```bash
source .venv/bin/activate        # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

¿Aún no tienes la carpeta `bloque4`? Sigue antes la guía de puesta a punto de la sesión 0.
