<!-- Generado desde sesion-1.html con tools/sync_exercises.py. No editar a mano. -->

# P2. El mismo encargo a tres proveedores

El script manda el mismo encargo a tres modelos distintos, cada uno con un formato de API diferente: OpenAI con la Responses API, Claude con la Messages API y Gemini con Chat Completions a través de OpenRouter (o con su Interactions API nativa si has puesto `GEMINI_API_KEY`).

Código: [`s1_hola_tres.py`](s1_hola_tres.py)

Ejecuta el script dos veces y responde en equipo:

- ¿Qué proveedor responde antes? ¿La diferencia se mantiene entre ejecuciones?
- Para el mismo texto, ¿por qué no coinciden los tokens de entrada? (Pista: cada proveedor usa un tokenizador distinto.)
- El correo es mixto: incidencia y pedido. ¿Lo clasifican bien los tres?
- ¿Cambia la redacción entre la primera y la segunda ejecución?
