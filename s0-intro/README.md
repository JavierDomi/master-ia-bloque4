# Guía de puesta a punto · Bloque 4: Agentes de IA y LLMs

Al terminar esta guía tendrás en tu ordenador todo lo necesario para el bloque:
Python, VS Code con un asistente de IA, Git y GitHub, y el código del curso funcionando.

Tiempo estimado: 30–45 minutos. Las instrucciones cubren **macOS** y **Windows**.
Si algo falla, lee el error **de abajo arriba**: la última línea dice qué ha pasado. Después mira
[Problemas frecuentes](#problemas-frecuentes) al final.

---

## 1. Python 3.11 o superior

Te recomendamos Python 3.12.

**macOS**
1. Descarga el instalador desde [python.org/downloads](https://www.python.org/downloads/) e instálalo.
   (Si usas Homebrew: `brew install python@3.12`).
2. Comprueba en una terminal:
   ```bash
   python3 --version
   ```

**Windows**
1. Descarga el instalador desde [python.org/downloads](https://www.python.org/downloads/).
2. En la primera pantalla del instalador **marca "Add python.exe to PATH"** antes de pulsar *Install Now*.
3. Comprueba en PowerShell:
   ```powershell
   py --version
   ```

Debe mostrar `Python 3.11` o superior.

> En esta guía, donde ponga `python`, usa `python3` en macOS y `py` en Windows
> hasta que actives el entorno virtual (paso 5). Dentro del entorno virtual, `python` funciona en los dos.

## 2. VS Code y sus extensiones

1. Descarga e instala VS Code desde [code.visualstudio.com](https://code.visualstudio.com/).
2. Abre VS Code, ve a la vista de **Extensiones** (`Ctrl+Shift+X` / `Cmd+Shift+X`) e instala:
   - **Python** (de Microsoft)
   - **Jupyter** (de Microsoft), para abrir los notebooks `.ipynb`
3. La terminal integrada se abre en **Terminal › New Terminal**. Usaremos siempre esa.

## 3. Git y una cuenta de GitHub

**Instalar Git**
- **macOS:** escribe `git --version` en la terminal. Si no está instalado, macOS te ofrecerá instalar las
  *Command Line Tools*: acepta.
- **Windows:** instala *Git for Windows* desde [git-scm.com](https://git-scm.com/download/win) con las opciones por defecto.
  Después cierra y vuelve a abrir VS Code.

**Configurar tu nombre y correo** (los que aparecerán en tus commits):
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@correo.com"
```

**Cuenta de GitHub**
1. Crea una cuenta en [github.com](https://github.com/) si no tienes.
2. Si eres estudiante, solicita el **GitHub Student Developer Pack** en [education.github.com](https://education.github.com/):
   entre otras cosas, da acceso gratuito a GitHub Copilot con más uso que el plan gratuito. La verificación puede tardar unos días:
   pídelo cuanto antes (ver el aviso del paso 4).

## 4. GitHub Copilot en VS Code

1. En VS Code, inicia sesión con tu cuenta de GitHub (icono de cuenta, abajo a la izquierda, o el aviso de Copilot).
2. Si no aparece el chat de Copilot, instala la extensión **GitHub Copilot** desde Extensiones.
3. Comprueba que funciona: abre el chat de Copilot y pregúntale *"¿Qué hace `python -m venv`?"*.

Sin el Student Developer Pack tendrás el **plan gratuito (Copilot Free)**, con un límite de uso mensual. Es suficiente para empezar.

> **Guarda cupo para la sesión 5.** Copilot Free tiene un **límite mensual** de peticiones al chat y de sugerencias,
> y vas a usarlo desde hoy. En la sesión 5, VS Code con Copilot Free es la aplicación desde la que se prueba tu servidor MCP
> (práctica P4): si ese mes ya has gastado el cupo, no podrás hacerla. Úsalo con cabeza y deja margen para ese día,
> o solicita el **GitHub Student Developer Pack** (paso 3), que da Copilot con mucho más uso.

> **Copilot sí, pero con cabeza.** Úsalo para que te explique código y errores, y para ir más rápido.
> No pegues código que no entiendas: tendrás que explicar todo lo que entregues.
> Nunca pegues claves de API ni datos personales en el chat.

## 5. El kit del bloque

El código del bloque (el *kit*) se publica **sesión a sesión** en el repositorio del bloque,
[github.com/JavierDomi/master-ia-bloque4](https://github.com/JavierDomi/master-ia-bloque4). Todo va en **una sola carpeta**
que irá creciendo: los scripts de cada sesión usan los de las anteriores (se importan unos a otros, así que tienen que
estar juntos).

> **Una carpeta, un entorno, un `.env`.** Durante todo el bloque trabajarás en la carpeta `bloque4` que creas hoy, con
> **un solo entorno virtual** (`.venv`) y **un solo fichero `.env`**. No crees otra carpeta ni otro entorno en cada sesión:
> en cada sesión descargas los ficheros nuevos en `bloque4`, activas el entorno y, si te lo indicamos, vuelves a ejecutar
> `pip install -r requirements.txt` en ese mismo entorno.

1. Crea una carpeta de trabajo, por ejemplo `bloque4`.
2. Copia en esa carpeta los ficheros de `s0-intro/` del repositorio del bloque. Para la puesta a punto necesitas:
   `requirements.txt`, `.env.example` y `crear_bd.py`.
   En cada sesión copiarás aquí los ficheros de esa sesión y los scripts de sus prácticas, **siempre en esta misma
   carpeta**.
3. En VS Code: **File › Open Folder…** y elige esa carpeta.
4. Abre la terminal integrada (estará ya en esa carpeta) y crea el **entorno virtual**:

   **macOS**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   **Windows (PowerShell)**
   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   Sabrás que está activo porque la línea de la terminal empieza por `(.venv)`.
   Tendrás que activarlo cada vez que abras una terminal nueva.

5. Instala las dependencias del bloque y el soporte para notebooks:
   ```bash
   pip install -r requirements.txt
   pip install ipykernel
   ```
6. Dile a VS Code que use ese entorno: `Ctrl+Shift+P` / `Cmd+Shift+P` → **Python: Select Interpreter** → elige el que
   aparece con `.venv`.

## 6. Las claves de API (`.env`)

Para hablar con los modelos desde código hacen falta **claves de API**. El máster no las proporciona.

### Opción recomendada: OpenRouter con 10 € de saldo

No es obligatorio, pero **sí muy recomendable**. [OpenRouter](https://openrouter.ai/) da acceso a cientos de modelos con
una sola clave, y con ella funcionan todos los ejemplos del bloque con modelos de **OpenAI, Anthropic (Claude) y
Google (Gemini)**. 10 € dan de sobra: ejecutar todo el código del bloque una vez cuesta unos 15 céntimos. Además, haber
comprado saldo sube el límite de los modelos gratuitos de 50 a 1.000 peticiones al día.

1. Crea una cuenta en [openrouter.ai](https://openrouter.ai/) y añade 10 € de saldo en **Credits**.
2. En **Keys**, crea una clave (empieza por `sk-or-`). Si quieres, ponle un límite de gasto.
3. Copia la plantilla del kit, que ya viene preparada para OpenRouter (solo esta vez: en las sesiones siguientes
   sigues usando el mismo `.env`, no lo sobrescribas):
   - macOS: `cp .env.example .env`
   - Windows: `copy .env.example .env`
4. Abre `.env` en VS Code y pega tu clave en la línea `OPENROUTER_API_KEY`. Nada más: las demás líneas la reutilizan.

   ```
   OPENROUTER_API_KEY=sk-or-...    ← tu clave, solo aquí

   OPENAI_BASE_URL=https://openrouter.ai/api/v1
   OPENAI_API_KEY=${OPENROUTER_API_KEY}
   OPENAI_MODEL=openai/gpt-5.4-mini

   ANTHROPIC_BASE_URL=https://openrouter.ai/api
   ANTHROPIC_API_KEY=${OPENROUTER_API_KEY}
   ANTHROPIC_MODEL=anthropic/claude-haiku-4.5

   GEMINI_MODEL=google/gemini-3.8-flash
   ```

**¿Por qué funciona?** El código del kit usa las librerías oficiales de OpenAI (Responses API) y de Anthropic (Messages
API). OpenRouter acepta esos dos formatos, así que basta con decirle a cada librería que hable con OpenRouter (las líneas
`..._BASE_URL`). Gemini va por OpenRouter con *Chat Completions*, el formato «clásico» de OpenAI que imitan casi todos.
El modelo que contesta es el que pongas en `..._MODEL`.

**Opcional: Gemini con su API nativa.** Si creas una clave gratuita en [aistudio.google.com](https://aistudio.google.com/)
(**Get API key**) y la pegas en `GEMINI_API_KEY`, los ejemplos usan la API nativa de Gemini en lugar de OpenRouter.
En el plan gratuito `gemini-3.8-flash` suele estar saturado (error 503): si te pasa, pon
`GEMINI_MODEL=google/gemini-3.5-flash-lite`.

### Sin gastar dinero

Puedes seguir el bloque gratis, sabiendo que irá peor:

| Opción | Qué hacer | Limitaciones |
| --- | --- | --- |
| **OpenRouter, modelos gratuitos** | La misma receta de arriba, pero con un modelo gratuito en los tres `..._MODEL`, por ejemplo `nvidia/nemotron-3-super-120b-a12b:free` (los gratuitos acaban en `:free`). | 50 peticiones al día. A veces están saturados (error 429). Son más flojos, sobre todo en la sesión 2. |
| **Gemini** (Google) | En [aistudio.google.com](https://aistudio.google.com/) pulsa **Get API key** y pégala en `GEMINI_API_KEY`. | Solo funciona en la parte «Gemini» de los ejemplos. |
| **Ollama** (modelos en tu ordenador) | Instálalo desde [ollama.com](https://ollama.com/) y descarga un modelo: `ollama pull llama3.2` (unos 2 GB). | Solo en algunos ejemplos. Los modelos pequeños razonan peor. |

### Cuidado con las claves

- El fichero `.env` **nunca** se sube a Git ni se comparte.
- Si una clave se filtra (la subes a Git, la pegas en un chat…), revócala en **Keys** y crea otra.
- **Privacidad:** el proveedor recibe todo lo que envías y, en los modelos gratuitos, puede usarlo para mejorar sus
  modelos. En las prácticas usamos datos inventados: nunca envíes datos personales reales.

No te preocupes si hoy no tienes la clave: la necesitaremos a partir de la sesión 1.

## 7. Comprobación final

Con el entorno virtual activo, ejecuta:
```bash
python crear_bd.py
```

Si ves `Base de datos creada en …/tostadero.db`, **está todo listo**: Python, el entorno virtual y el kit funcionan.
Ese fichero `tostadero.db` es la base de datos de ejemplo que usaremos durante el bloque.

## 8. Opcional: tu propio repositorio

Para guardar tu trabajo y tener historial de cambios:

1. Crea un fichero `.gitignore` en la carpeta `bloque4` con este contenido:
   ```
   .env
   .venv/
   __pycache__/
   *.db
   ```
2. Inicializa el repositorio y haz el primer commit:
   ```bash
   git init
   git add .
   git commit -m "Kit del bloque 4"
   ```
3. Crea un repositorio **privado** en GitHub y súbelo siguiendo las instrucciones que te muestra GitHub
   (o desde VS Code: vista **Source Control** › *Publish Branch*).

Antes del primer `git add`, comprueba que `.env` aparece en `.gitignore`: tus claves no deben llegar nunca a GitHub.

---

## Más adelante en el bloque

No hace falta instalarlo hoy:

| Qué | Para qué | Cuándo |
| --- | --- | --- |
| Node.js 20 o superior ([nodejs.org](https://nodejs.org/)) | MCP Inspector, para probar servidores MCP | Sesión 5 |
| Docker Desktop | Práctica opcional: el servidor MCP en un contenedor | Sesión 6 (opcional) |

## Problemas frecuentes

| Síntoma | Solución |
| --- | --- |
| `python` / `py` no se reconoce (Windows) | Reinstala Python marcando **"Add python.exe to PATH"** y reabre VS Code. |
| `command not found: python` (macOS) | Usa `python3` hasta activar el entorno virtual. |
| PowerShell no deja ejecutar `Activate.ps1` ("la ejecución de scripts está deshabilitada") | Ejecuta una vez `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` y vuelve a activar. |
| `pip install` falla compilando algo | Comprueba que usas Python 3.11 o superior dentro del entorno (`python --version`). |
| VS Code no encuentra los paquetes instalados (subrayados en rojo) | **Python: Select Interpreter** y elige el de `.venv`. |
| El notebook pide instalar un kernel | Instala `ipykernel` con el entorno activo y elige `.venv` como kernel (arriba a la derecha del notebook). |
| `git` no se reconoce (Windows) | Instala Git for Windows y reinicia VS Code. |
| La terminal ya no muestra `(.venv)` | Es una terminal nueva: vuelve a activar el entorno (paso 5.4). |
| `ModuleNotFoundError: No module named 'dotenv'` (u otro paquete del kit) | El entorno no está activo o VS Code usa otro intérprete: activa `.venv` y elige su intérprete. Si sigue, `pip install -r requirements.txt`. |
| `ModuleNotFoundError: No module named 'herramientas'` (u otro script del kit) | Ese fichero no está en `bloque4`: todos los ficheros del kit van en la misma carpeta. |
| `sqlite3.OperationalError: no such table: …` | Falta la base de datos: ejecuta `python crear_bd.py` dentro de `bloque4`. |
| Copilot dice que has alcanzado el límite del plan | Es el cupo mensual de Copilot Free: espera al mes siguiente o solicita el Student Developer Pack (paso 3). |
| `SSL: CERTIFICATE_VERIFY_FAILED` al llamar a una API (macOS, Python de python.org) | Ejecuta una vez **Install Certificates.command**, en la carpeta `/Applications/Python 3.x/`. |
| `curl` se comporta raro en PowerShell | Escribe `curl.exe` en lugar de `curl` (en PowerShell, `curl` es otro comando). |
