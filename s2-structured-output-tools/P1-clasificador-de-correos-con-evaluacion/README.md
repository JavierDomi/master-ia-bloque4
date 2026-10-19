<!-- Generado desde sesion-2.html con tools/sync_exercises.py. No editar a mano. -->

# P1. Clasificador de correos con evaluación

**Qué haces:** **programar** en `s2_extraer_correo.py`: ampliar el conjunto de evaluación y añadir una validación de negocio. Forma parte del entregable E2.

Código: [`s2_extraer_correo.py`](s2_extraer_correo.py)

1. Ejecuta el script y anota los aciertos de cada proveedor.
2. Amplía `CASOS` hasta al menos 15, con casos difíciles: ironía, dos clientes en el mismo correo, un correo en inglés, un correo sin nombre de negocio.
3. Revisa cada fallo: ¿es un error del modelo o del caso (etiqueta ambigua)? Corrige las etiquetas dudosas antes de comparar.
4. Añade una validación de negocio: si hay cliente, comprueba con `buscar_cliente` que existe en la base de datos.

**Cómo comprobarlo:** `python s2_extraer_correo.py` imprime los aciertos de los tres proveedores sobre al menos 15 casos, y avisa cuando un correo nombra un cliente que no está en la base de datos (incluye algún caso así).

**Qué entregas:** `e2/s2_extraer_correo.py` y, en `e2/analisis.md`, los aciertos de cada proveedor con tus casos, los fallos que revisaste y las etiquetas que corregiste, y por qué.

**Configuración en clase.** OpenAI / Claude / Gemini = formato de API + modelo. En clase los tres van por OpenRouter con una sola clave: `openai/gpt-5.4-mini` (SDK de OpenAI, Responses API), `anthropic/claude-haiku-4.5` (SDK de Anthropic, Messages API) y `google/gemini-3.8-flash` (SDK de OpenAI, Chat Completions).

- Las salidas estructuradas y las herramientas dependen del modelo. Si `output_parsed`, `parsed_output` o `message.parsed` llega como `None`, el bucle de evaluación falla en `resultado.tipo`: comprueba el modelo que tienes en `.env`.
- Gemini va por Chat Completions: `chat.completions.parse(response_format=CorreoClasificado)`. La API nativa (Interactions) solo se usa si rellenas la `GEMINI_API_KEY` opcional.
