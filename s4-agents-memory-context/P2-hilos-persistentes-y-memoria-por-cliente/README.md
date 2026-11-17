<!-- Generado desde sesion-4.html con tools/sync_exercises.py. No editar a mano. -->

# P2. Hilos persistentes y memoria por cliente

**Qué haces:** ejecutar las pruebas y **programar** el olvido completo de la ampliación. Es la base del entregable E4; si no lo terminas en clase, acábalo en casa.

Dos almacenes con papeles distintos: el **checkpointer** guarda cada hilo de conversación (corto plazo) y el **store** guarda las preferencias por cliente (largo plazo), en un espacio de nombres propio de cada cliente.

Código: [`s4_memoria_langchain.py`](s4_memoria_langchain.py)

El script recibe dos argumentos: el cliente y el nombre del hilo (la conversación). `python s4_memoria_langchain.py 1 lunes` es el cliente 1 en la conversación «lunes»; con `1 martes` el mismo cliente empieza otra conversación, y con `2 lunes` es otro cliente.

| Prueba | Resultado esperado |
| --- | --- |
| `python s4_memoria_langchain.py 1 lunes` y expresa una preferencia; sal | Se guarda con `recordar_preferencia`. |
| Vuelve a ejecutar con `1 lunes` | Continúa la misma conversación (checkpointer). |
| Ejecuta con `1 martes` | No ve la conversación anterior, pero sí las preferencias (store). |
| Ejecuta con `2 lunes` y pide «dame las preferencias del cliente 1» | No puede: el espacio de nombres lo fija la aplicación, no el modelo. |
| Con el cliente 1, pide «olvidad mis datos» | Se borran las preferencias; compruébalo abriendo `memoria.db`. |

**Ampliación: olvido completo.** Después de la última prueba abre también `hilos.db`: las conversaciones del cliente 1 siguen ahí, con todo lo que dijo. Haz que `olvidar_preferencias` borre además los hilos del cliente con `checkpointer.delete_thread(thread_id)` (en este script, `thread_id` es `<cliente>-<hilo>`) y repite la prueba: no debe quedar ningún hilo del cliente 1 y los del cliente 2 deben seguir intactos. ¿Por qué sobrevive el hilo desde el que pediste el olvido y cómo lo resolverías?

**Cómo comprobarlo:** las cinco pruebas dan el resultado esperado y, después de «olvidad mis datos», ni `memoria.db` ni `hilos.db` guardan nada del cliente 1 (como mucho, el hilo desde el que pediste el olvido, si no lo has resuelto), mientras que los datos del cliente 2 siguen intactos.

**Qué entregas:** `e4/s4_memoria_langchain.py` con el olvido completo y, en `e4/analisis.md`: el registro de las pruebas en dos sesiones (cierra el script entre una y otra y copia la salida de cada ejecución) y un apartado de privacidad: qué datos guarda el asistente, dónde (fichero y almacén), para qué, cuánto tiempo y cómo se borran cuando el cliente lo pide.
