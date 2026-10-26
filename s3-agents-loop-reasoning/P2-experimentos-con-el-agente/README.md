<!-- Generado desde sesion-3.html con tools/sync_exercises.py. No editar a mano. -->

# P2. Experimentos con el agente

| Experimento | Qué observar |
| --- | --- |
| Ejecuta el correo de ejemplo | Secuencia de herramientas, prioridad elegida y respuesta final. |
| Fija `max_pasos=2` al crear el agente en el `__main__`: `Agente(SISTEMA, herramientas, max_pasos=2)` | Cómo se corta y qué mensaje recibe el cliente. |
| Rechaza la aprobación | Cómo reacciona el modelo: ¿lo reintenta, lo explica, propone otra cosa? |
| Quita «Úsala solo si el cliente describe una avería» de la descripción de `crear_incidencia` (en `DEFINICIONES`, dentro de `herramientas.py`) y pregunta «¿Revisáis las máquinas en agosto?» | Si crea incidencias innecesarias. |
| Quita el paso 1 del procedimiento en `SISTEMA` | Si se inventa identificadores de cliente. |
