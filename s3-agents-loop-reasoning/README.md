<!-- Generado desde sesion-3.html con tools/sync_exercises.py. No editar a mano. -->

# Ejercicios · Agentes I: el bucle agéntico, razonamiento y planificación

**Entregable:** E3. Agente de atención técnica desde cero y con LangChain, con trazas, límite de pasos y aprobación humana, y una comparación razonada de una página. Entrega en la carpeta `e3/` de tu repositorio de entregas hasta el domingo 1 de noviembre a las 23:59.

## Prácticas

Cada práctica tiene su carpeta, con el enunciado (`README.md`) y el código que usa:

- [P1. Un agente desde cero](P1-un-agente-desde-cero/)
- [P2. Experimentos con el agente](P2-experimentos-con-el-agente/)
- [P3. El mismo agente con LangChain](P3-el-mismo-agente-con-langchain/)
- [P4. Enrutador: workflow delante del agente](P4-enrutador-workflow-delante-del-agente/)

## Código

Los scripts son los del kit del bloque:

- [`requirements.txt`](requirements.txt)
- [`.env.example`](.env.example)
- [`crear_bd.py`](crear_bd.py)
- [`herramientas.py`](P2-experimentos-con-el-agente/herramientas.py)
- [`s3_agente.py`](P1-un-agente-desde-cero/s3_agente.py)
- [`s3_agente_langchain.py`](P3-el-mismo-agente-con-langchain/s3_agente_langchain.py)

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
