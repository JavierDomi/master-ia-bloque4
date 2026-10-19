<!-- Generado desde sesion-2.html con tools/sync_exercises.py. No editar a mano. -->

# P4. El mismo asistente con Claude o con Gemini

**Qué haces:** **programar** el bucle de P3 para otro proveedor. Forma parte del entregable E2; si no la terminas en clase, acábala en casa.

Porta el bucle a otro proveedor usando la tabla del apartado 4: a Claude con `para_claude()` o a Gemini con `para_chat()` (Chat Completions, que es como va Gemini en clase; `para_gemini()` y la Interactions API solo si tienes la `GEMINI_API_KEY` opcional). Compara con OpenAI el número de llamadas, los tokens y la calidad de la respuesta final.

**Qué tienes que programar:** un fichero nuevo, `s2_chat_claude.py` o `s2_chat_gemini.py`, con una función `preguntar_claude()` o `preguntar_gemini()` que haga lo mismo que `preguntar()` de P3: mismo `SISTEMA` (impórtalo de `s2_chat_herramientas`), mismas herramientas, la misma traza y un límite de vueltas.

**Cómo comprobarlo:** con las cuatro preguntas de P3, la traza muestra las mismas herramientas que con OpenAI y la respuesta final usa los datos reales de la base de datos.

- OpenAI / Claude / Gemini = formato de API + modelo. En clase van por OpenRouter: `gpt-5.4-mini`, `claude-haiku-4.5` y `gemini-3.8-flash`.
- Tokens: imprime `r.usage` en cada vuelta del bucle. En Responses y Messages trae `input_tokens` y `output_tokens`; en Chat Completions, `prompt_tokens` y `completion_tokens`.

**Qué entregas:** `e2/s2_chat_claude.py` o `e2/s2_chat_gemini.py` y, en `e2/analisis.md`, una tabla que compare OpenAI con el proveedor que elegiste en las cuatro preguntas de P3: número de llamadas a herramientas, tokens de entrada y de salida, y calidad de la respuesta final.
