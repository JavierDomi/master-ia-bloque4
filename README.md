# Máster FP IA y Big Data · Bloque 4: Agentes de IA y LLMs

Material del bloque 4 del módulo 5073, *Programación de Inteligencia Artificial*, del Máster FP en Inteligencia
Artificial y Big Data de la Cámara de Madrid, curso 2026-2027. Clases los martes de 18:00 a 21:30.

Durante el bloque construimos, sesión a sesión, el asistente de operaciones de **Tostadero Retiro S.L.**, una pyme
ficticia que distribuye café de especialidad a bares, restaurantes y hoteles.

## Sesiones

Cada carpeta se publica antes de su clase.

| Sesión | Fecha | Tema | Entregable |
| --- | --- | --- | --- |
| 0 | Martes 6 oct | [Introducción y puesta a punto](s0-intro/) | — |
| 1 | Martes 13 oct | [Integración con LLMs: APIs de OpenAI, Gemini y Claude](s1-llm-apis/) | E1 (10 %) · viernes 16 oct, 23:59 |
| 2 | Martes 20 oct | Salidas estructuradas y uso de herramientas *(próximamente)* | E2 (15 %) |
| 3 | Martes 27 oct | Agentes I: el bucle agéntico, razonamiento y planificación *(próximamente)* | E3 (15 %) |
| 4 | Martes 17 nov | Agentes II: memoria y contexto *(próximamente)* | E4 (15 %) |
| 5 | 2.º trimestre | MCP I: el protocolo y tu primer servidor *(próximamente)* | E5 (15 %) |
| 6 | 2.º trimestre | MCP II: clientes, seguridad y proyecto integrador *(próximamente)* | E6 (30 %) |

## Cómo usar este repositorio

Trabaja siempre en tu carpeta `bloque4`, la que preparaste en la sesión 0 con la
[guía de puesta a punto](s0-intro/README.md): un solo entorno virtual (`.venv`) y un solo `.env` para todo el bloque.
Este repositorio es solo el material: **copia en `bloque4` el contenido de la carpeta `codigo/` de cada sesión** y
trabaja allí.

- **Descarga:** botón **Code › Download ZIP**, o clona el repositorio y actualízalo cada semana:

  ```bash
  git clone https://github.com/JavierDomi/master-ia-bloque4.git
  git pull        # cada semana, para traer la sesión nueva
  ```

- **Cada sesión** tiene la misma estructura:

  ```
  s1-llm-apis/
  ├── README.md      índice de prácticas, entregable y puesta en marcha
  ├── enunciados/    un enunciado por práctica: P1-….md, P2-….md…
  ├── codigo/        los scripts de la sesión: cópialos en bloque4
  └── slides/        las slides en PDF
  ```

- **Esqueletos:** algunos ficheros vienen a medias a propósito. Lo que falta está marcado con `TODO` y el enunciado
  de la práctica dice qué hay que completar.
- **Soluciones:** se publican en la carpeta `soluciones/` de cada sesión cuando pasa su fecha de entrega.

## Entregas

Cada alumno entrega en **su propio repositorio privado** de GitHub:

1. Crea un repositorio **privado** llamado exactamente **`master-ia-bloque4-apellido-nombre`**: primer apellido y
   nombre, en minúsculas, sin tildes ni eñes. Por ejemplo, `master-ia-bloque4-garcia-lucia`.
2. Invita a **JavierDomi**: *Settings › Collaborators › Add people*.
3. Antes del primer commit, copia a la raíz el [`.gitignore`](plantilla-entregas/.gitignore) de
   `plantilla-entregas/`. **Tu `.env` no se sube nunca**: lleva tu clave de API.
4. Una carpeta por entregable, `e1/` a `e6/`, con los ficheros que pide cada sesión:

   ```
   master-ia-bloque4-garcia-lucia/
   ├── .gitignore
   ├── e1/
   │   ├── llm_client.py
   │   ├── comparativa.csv
   │   └── analisis.md
   └── e2/
       └── …
   ```

5. Se corrige el **último commit anterior a la fecha límite** de cada entregable.

Qué lleva cada entregable y su fecha están en el `README.md` de la carpeta de cada sesión.

> **¿Has subido una clave por error?** Revócala al momento en OpenRouter (*Keys*) y crea otra. Borrar el fichero no
> basta: la clave sigue en el historial de git.

## Claves y datos

- Cada alumno usa su propia clave de OpenRouter (recomendado: 5–10 € de saldo y un límite de gasto en la clave).
- Las prácticas usan solo datos inventados: no envíes datos personales reales a ningún modelo.
- Al terminar el curso, revoca tu clave.
