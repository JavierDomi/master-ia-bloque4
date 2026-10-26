<!-- Generado desde sesion-3.html con tools/sync_exercises.py. No editar a mano. -->

# P3. El mismo agente con LangChain

Con `create_agent`, el bucle lo pone el framework y el control se añade con middleware. La aprobación humana necesita un *checkpointer*, porque pausar consiste en guardar el estado del grafo y reanudarlo después.

Código: [`s3_agente_langchain.py`](s3_agente_langchain.py)

Comparad ambas versiones: líneas de código, qué viene resuelto (pausa y reanudación, límite de llamadas, cambio de proveedor con una cadena) y qué se pierde (visibilidad del bucle y control fino del formato de los mensajes).

Para cambiar de proveedor basta la cadena del modelo: `"openai:google/gemini-3.8-flash"` (u otro modelo de OpenRouter con herramientas) funciona con la misma clave, porque `langchain-openai`, incluido en `requirements.txt`, lee `OPENAI_BASE_URL` del `.env`. El prefijo `google_genai:` necesitaría instalar `langchain-google-genai` (no está en `requirements.txt`) y una clave propia de Gemini.
