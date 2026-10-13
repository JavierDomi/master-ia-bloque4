<!-- Generado desde sesion-1.html con tools/sync_exercises.py. No editar a mano. -->

# P3. Una interfaz común

El patrón Adapter oculta las diferencias entre SDK tras un único método `responder()`. El resto del bloque lo usará cuando el proveedor dé igual. El atributo `formato` indica qué formato de API habla cada proveedor (`"responses"`, `"messages"`, `"interactions"` o `"chat"`, es decir, Chat Completions) y decide qué rama de `responder()` se ejecuta.

Código: [`llm_client.py`](../codigo/llm_client.py)

Te damos un esqueleto: la clase `Respuesta`, el constructor con los clientes ya creados y la rama `"chat"` de `responder()` hecha, que te sirve de modelo. Tareas:

1. Completa las ramas `"responses"` (OpenAI) y `"messages"` (Claude) de `responder()`, marcadas con `TODO`: cada una llama a su SDK y devuelve el texto y los tokens de entrada y de salida en una `Respuesta`. Las llamadas las tienes en `s1_hola_tres.py`. Prueba con `python llm_client.py`: al terminar deben responder los tres proveedores.
2. Rellena `PRECIOS` con los modelos que uses: la clave es el id del modelo tal y como va en `.env` (por ejemplo, `"openai/gpt-5.4-mini"`) y los precios, en dólares por millón de tokens, salen de [openrouter.ai/models](https://openrouter.ai/models). Comprueba que `coste_usd` devuelve una cifra.
3. Añade un parámetro común `max_tokens` y tradúcelo al parámetro de cada proveedor.
4. Reto: añade un método `responder_stream()` que devuelva un generador de fragmentos de texto (las llamadas en streaming de cada SDK están en `s1_streaming.py`).
