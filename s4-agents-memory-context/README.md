<!-- Generado desde sesion-4.html con tools/sync_exercises.py. No editar a mano. -->

# Ejercicios · Agentes II: memoria y contexto

**Entregable:** E4. Asistente con hilos persistentes y preferencias por cliente (guardar, consultar y olvidar), con registro de pruebas en dos sesiones y un apartado de privacidad. Entrega en la carpeta `e4/` de tu repositorio de entregas hasta el domingo 22 de noviembre a las 23:59.

## Prácticas

Cada práctica tiene su carpeta, con el enunciado (`README.md`) y el código que usa:

- [P1. Compactación desde cero](P1-compactacion-desde-cero/)
- [P2. Hilos persistentes y memoria por cliente](P2-hilos-persistentes-y-memoria-por-cliente/)
- [P3. Selección automática de memoria](P3-seleccion-automatica-de-memoria/)
- [P4. Estado en el servidor del proveedor](P4-estado-en-el-servidor-del-proveedor/)

## Código

Los scripts son los del kit del bloque:

- [`requirements.txt`](requirements.txt)
- [`.env.example`](.env.example)
- [`s4_compactar.py`](P1-compactacion-desde-cero/s4_compactar.py)
- [`s4_memoria_langchain.py`](P2-hilos-persistentes-y-memoria-por-cliente/s4_memoria_langchain.py)
- [`s4_estado_gemini.py`](P4-estado-en-el-servidor-del-proveedor/s4_estado_gemini.py)

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
