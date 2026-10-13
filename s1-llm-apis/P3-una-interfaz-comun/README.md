<!-- Generado desde sesion-1.html con tools/sync_exercises.py. No editar a mano. -->

# P3. Una interfaz común

**Qué haces:** **programar** en `llm_client.py`, que te damos a medias. Forma parte del entregable E1.

El patrón Adapter oculta las diferencias entre SDK tras un único método `responder()`. El resto del bloque lo usará cuando el proveedor dé igual. El atributo `formato` indica qué formato de API habla cada proveedor (`"responses"`, `"messages"`, `"interactions"` o `"chat"`, es decir, Chat Completions) y decide qué rama de `responder()` se ejecuta.

Código: [`llm_client.py`](llm_client.py)

**Qué te damos hecho:** la clase `Respuesta`, el constructor con los clientes ya creados y las ramas `"chat"` e `"interactions"` de `responder()`. La rama `"chat"` te sirve de modelo, y las llamadas a cada SDK las tienes en `s1_hola_tres.py` (P2).

**Qué tienes que programar:**

1. **La rama `"responses"` (OpenAI)**, donde pone `TODO 1`: llama a la Responses API con el modelo, el mensaje de sistema, el prompt y la temperatura si se pasa, y guarda el texto, los tokens de entrada y los de salida.
2. **La rama `"messages"` (Claude)**, donde pone `TODO 2`: lo mismo con la Messages API. Ojo: `max_tokens` es obligatorio, el mensaje de sistema no va dentro de `messages` y el texto llega repartido en bloques.
3. **El diccionario `PRECIOS`**: añade los tres modelos que usas. La clave es el id del modelo tal y como va en `.env` (por ejemplo, `"openai/gpt-5.4-mini"`) y el valor, `(precio de entrada, precio de salida)` en dólares por millón de tokens, sacados de [openrouter.ai/models](https://openrouter.ai/models).
4. **Un parámetro `max_tokens`**: añade a `responder()` un parámetro opcional `max_tokens` y haz que cada rama lo pase a su API con el nombre que esa API usa. No se llama igual en todas: búscalo en la documentación de cada SDK.
5. *Reto opcional:* un método `responder_stream()` que devuelva un generador de fragmentos de texto. Las llamadas en streaming de cada SDK están en `s1_streaming.py`.

**Cómo comprobarlo:**

- `python llm_client.py` responde con los tres proveedores y ya no aparece ningún «pendiente».
- `LLM("claude").responder("Responde en una frase.", "¿Qué es un token?").coste_usd` devuelve una cifra, no `None`.
- Con `max_tokens=20`, los tokens de salida no pasan de 20. Si algún modelo devuelve el texto vacío, piensa por qué (apartado 3).

**Qué entregas:** `e1/llm_client.py` en tu repositorio de entregas.
