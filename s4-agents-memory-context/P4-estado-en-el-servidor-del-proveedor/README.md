<!-- Generado desde sesion-4.html con tools/sync_exercises.py. No editar a mano. -->

# P4. Estado en el servidor del proveedor

**Qué haces:** mirar la demo. **No hay que programar** y no se entrega.

Demo del profesor (5 min) con Gemini nativo y la clave gratuita de AI Studio: `s4_estado_gemini.py` mantiene la misma conversación de cuatro turnos dos veces, primero reenviando el historial en cada llamada (estado en la aplicación) y después con `previous_interaction_id` (estado en el proveedor), e imprime en cada turno lo que envía el programa y los tokens de entrada que lee el modelo. Fíjate en tres cosas: tokens facturados, cantidad de código y qué datos quedan almacenados en el proveedor.

Si tienes la clave gratuita de Gemini (`GEMINI_API_KEY` en `.env`), puedes reproducirla con `python s4_estado_gemini.py`. Por OpenRouter no funciona: su API no guarda estado.
