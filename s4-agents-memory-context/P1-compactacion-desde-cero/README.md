<!-- Generado desde sesion-4.html con tools/sync_exercises.py. No editar a mano. -->

# P1. Compactación desde cero

**Qué haces:** ejecutar el script y cambiar sus constantes. **No hay que programar**, pero tus observaciones forman parte del entregable E4.

Sin frameworks: solo el SDK de Anthropic (en clase, `anthropic/claude-haiku-4.5` vía OpenRouter, con `ANTHROPIC_MODEL` y `ANTHROPIC_BASE_URL` del `.env`). El tamaño del historial se toma del uso (`r.usage`) que devuelve cada respuesta: entrada más salida de la última llamada.

Código: [`s4_compactar.py`](s4_compactar.py)

1. Conversa al menos diez turnos y observa cómo crecen los tokens de entrada y cómo caen tras compactar.
2. Comprueba qué datos sobreviven: pregunta por algo que dijiste en el primer turno.
3. Cambia `MANTENER` y `UMBRAL_TOKENS` y anota el efecto en coste y calidad.
4. Explica por qué `MANTENER` debe ser par en este diseño.

**Qué entregas:** en `e4/analisis.md`, los tokens de entrada antes y después de compactar en una conversación de al menos diez turnos, qué datos del primer turno sobrevivieron al resumen, el efecto de cambiar `MANTENER` y `UMBRAL_TOKENS` en coste y calidad, y por qué `MANTENER` debe ser par.
