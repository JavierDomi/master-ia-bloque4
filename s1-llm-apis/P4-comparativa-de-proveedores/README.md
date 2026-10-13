<!-- Generado desde sesion-1.html con tools/sync_exercises.py. No editar a mano. -->

# P4. Comparativa de proveedores

**Qué haces:** **programar** un bucle corto en `s1_comparativa.py` y después analizar los resultados en equipo. Forma parte del entregable E1. Necesitas tener P3 terminada: el script usa tu `llm_client.py`.

Código: [`s1_comparativa.py`](s1_comparativa.py)

**Qué tienes que programar**, donde pone `TODO`:

1. Para cada proveedor (`"openai"`, `"claude"` y `"gemini"`), crea un único `LLM`.
2. Con ese `LLM`, responde a cada correo de `CORREOS` con el mismo `SISTEMA`.
3. Por cada respuesta, escribe una fila en el CSV con las columnas de la cabecera y en ese orden: los segundos con dos decimales y `calidad_1a5` vacía.
4. Imprime una línea por llamada para ver el avance.

**Cómo comprobarlo:** `python s1_comparativa.py` genera `comparativa.csv` con la cabecera y 15 filas (3 proveedores × 5 correos), y la columna `coste_usd` tiene cifras. Si sale vacía, revisa `PRECIOS` en P3.

**Qué analizáis en equipo** (sin programar):

1. Puntuad de 1 a 5 la columna `calidad_1a5` de cada respuesta.
2. Mirad la columna de tokens de salida y explicad en `analisis.md` por qué un modelo gasta muchos más que los otros para respuestas igual de cortas. (Pista: apartado 3.)
3. Responded en `analisis.md`: *¿qué modelo elegiríais para contestar 2.000 correos al mes y por qué?* Apoyaos en datos de la tabla (coste, latencia y calidad), no en impresiones.

**Qué entregas:** `e1/comparativa.csv`, con la calidad puntuada, y `e1/analisis.md` en tu repositorio de entregas.
