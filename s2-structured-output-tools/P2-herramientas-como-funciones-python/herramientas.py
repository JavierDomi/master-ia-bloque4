"""Sesiones 2 y 3. Herramientas de negocio como funciones Python + su esquema JSON.

En la sesión 5 estas mismas funciones pasarán a un servidor MCP."""
import sqlite3
from datetime import date
from pathlib import Path

BD = Path(__file__).with_name("tostadero.db")


def _consulta(sql: str, params: tuple = ()) -> list[dict]:
    with sqlite3.connect(BD) as con:
        con.row_factory = sqlite3.Row
        return [dict(f) for f in con.execute(sql, params)]


def buscar_cliente(texto: str) -> list[dict]:
    return _consulta("SELECT id, nombre, tipo, distrito FROM clientes WHERE nombre LIKE ?",
                     (f"%{texto}%",))


def consultar_pedidos(cliente_id: int) -> list[dict]:
    return _consulta("SELECT id, fecha, estado, total FROM pedidos WHERE cliente_id = ?",
                     (cliente_id,))


def stock_producto(texto: str) -> list[dict]:
    return _consulta("SELECT sku, nombre, precio, stock FROM productos "
                     "WHERE nombre LIKE ? OR sku LIKE ?", (f"%{texto}%", f"%{texto}%"))


def crear_incidencia(cliente_id: int, maquina: str, descripcion: str, prioridad: str) -> dict:
    if not _consulta("SELECT 1 FROM clientes WHERE id = ?", (cliente_id,)):
        return {"error": f"No existe el cliente {cliente_id}. Búscalo antes con buscar_cliente."}
    with sqlite3.connect(BD) as con:
        cur = con.execute(
            "INSERT INTO incidencias (cliente_id, maquina, descripcion, prioridad, fecha) "
            "VALUES (?,?,?,?,?)",
            (cliente_id, maquina, descripcion, prioridad, date.today().isoformat()))
    return {"id": cur.lastrowid, "estado": "abierta"}


def _obj(props: dict) -> dict:
    """Esquema de objeto compatible con el modo estricto de OpenAI:
    todas las propiedades obligatorias y sin propiedades adicionales."""
    return {"type": "object", "properties": props,
            "required": list(props), "additionalProperties": False}


# Definición neutra: nombre, descripción (¡la lee el modelo!) y parámetros en JSON Schema
DEFINICIONES = [
    {"name": "buscar_cliente",
     "description": "Busca clientes por nombre (coincidencia parcial). Devuelve id, nombre, "
                    "tipo y distrito. Úsala antes de cualquier otra herramienta que pida cliente_id.",
     "parameters": _obj({"texto": {"type": "string", "description": "Parte del nombre"}})},
    {"name": "consultar_pedidos",
     "description": "Lista los pedidos de un cliente con fecha, estado y total en euros.",
     "parameters": _obj({"cliente_id": {"type": "integer"}})},
    {"name": "stock_producto",
     "description": "Consulta precio y stock de productos cuyo nombre o SKU contenga el texto.",
     "parameters": _obj({"texto": {"type": "string"}})},
    {"name": "crear_incidencia",
     "description": "Registra una avería de una máquina de un cliente. Úsala solo si el cliente "
                    "describe una avería concreta.",
     "parameters": _obj({
         "cliente_id": {"type": "integer"},
         "maquina": {"type": "string", "description": "SKU de la máquina, p. ej. MAQ-010"},
         "descripcion": {"type": "string"},
         "prioridad": {"type": "string", "enum": ["baja", "media", "alta"]},
     })},
]

FUNCIONES = {"buscar_cliente": buscar_cliente, "consultar_pedidos": consultar_pedidos,
             "stock_producto": stock_producto, "crear_incidencia": crear_incidencia}


# Adaptadores: misma herramienta, cuatro "dialectos"
def para_openai() -> list[dict]:
    return [{"type": "function", "strict": True, **d} for d in DEFINICIONES]


def para_claude() -> list[dict]:
    return [{"name": d["name"], "description": d["description"], "input_schema": d["parameters"]}
            for d in DEFINICIONES]


def para_gemini() -> list[dict]:
    return [{"type": "function", **d} for d in DEFINICIONES]


def para_chat() -> list[dict]:  # Chat Completions: Gemini vía OpenRouter, Ollama...
    return [{"type": "function", "function": d} for d in DEFINICIONES]
