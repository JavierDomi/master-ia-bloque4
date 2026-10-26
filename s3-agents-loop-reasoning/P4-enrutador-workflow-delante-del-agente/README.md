<!-- Generado desde sesion-3.html con tools/sync_exercises.py. No editar a mano. -->

# P4. Enrutador: workflow delante del agente

No todo correo necesita un agente. Combina el clasificador de la sesión 2 con el agente para que solo los casos complejos usen el camino caro:

```python
from llm_client import LLM                 # copia de la sesión 1
from s2_extraer_correo import con_openai   # copia de la sesión 2

SISTEMA_CONSULTAS = "..."                  # lo escribes tú

def atender(correo: str) -> str:
    clasificacion = con_openai(correo)        # sesión 2: salida estructurada
    if clasificacion.tipo == "consulta":      # camino barato y predecible
        return LLM("gemini").responder(SISTEMA_CONSULTAS, correo).texto
    return agente.ejecutar(correo)            # camino agéntico para lo complejo
```

- **Ficheros:** el pack de ejercicios de hoy solo trae `crear_bd.py`, `herramientas.py` y los `s3_*`. Copia `llm_client.py` (sesión 1) y `s2_extraer_correo.py` (sesión 2) en la misma carpeta.
- **Tu parte:** escribe `SISTEMA_CONSULTAS` (instrucciones para responder consultas sencillas) y construye `agente` como en el `__main__` de `s3_agente.py`.
- **Modelo del camino barato:** `LLM("gemini")` funciona sin más claves (va por OpenRouter a `google/gemini-3.8-flash`), pero es un modelo de razonamiento y genera más tokens de salida. `LLM` acepta `modelo`: prueba también `LLM("openai", modelo="openai/gpt-5.4-nano")`, aún más barato, y compara.

Mide con los casos de la sesión 2 cuántas llamadas y tokens ahorra el enrutador. `agente.ejecutar()` solo devuelve el texto, así que suma `r.usage` dentro de su bucle; en el camino barato, la `Respuesta` de `LLM` ya trae `tokens_entrada` y `tokens_salida`.
