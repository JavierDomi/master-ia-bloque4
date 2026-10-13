<!-- Generado desde sesion-1.html con tools/sync_exercises.py. No editar a mano. -->

# P1. Entorno

**Qué haces:** preparar el entorno y ejecutar un script. **No hay que programar.**

Trabaja en tu carpeta `bloque4`, la que preparaste en la sesión 0: un solo entorno virtual y un solo `.env` para todo el bloque. Si no hiciste la puesta a punto, sigue antes la guía de la sesión 0 (entorno, `.env` y `python crear_bd.py`).

1. Descarga del repositorio del bloque ([github.com/JavierDomi/master-ia-bloque4](https://github.com/JavierDomi/master-ia-bloque4)) la carpeta `s1-llm-apis/` y copia en `bloque4` sus ficheros y los scripts de cada práctica, todo junto: `s1_hola_tres.py`, `llm_client.py`, `s1_comparativa.py` y `s1_streaming.py`.
2. En `.env`, pega tu clave de OpenRouter una sola vez, en la línea `OPENROUTER_API_KEY`: las demás la reutilizan. Los modelos ya vienen puestos (`openai/gpt-5.4-mini`, `anthropic/claude-haiku-4.5` y `google/gemini-3.8-flash`, los tres a través de OpenRouter).
3. Activa el entorno, actualiza las dependencias y ejecuta el script de prueba:

```
source .venv/bin/activate        # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python s1_hola_tres.py
```

**Listo cuando:** `python s1_hola_tres.py` muestra tres respuestas (OpenAI, Claude y Gemini), cada una con sus segundos y sus tokens.

Opcional: si pegas una clave gratuita de [AI Studio](https://aistudio.google.com/) en `GEMINI_API_KEY`, Gemini usará su API nativa. Sin saldo, consulta las alternativas gratuitas en la guía de puesta a punto.
