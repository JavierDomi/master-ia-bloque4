"""Crea la base de datos de ejemplo de Tostadero Retiro S.L. (hilo conductor del bloque)."""
import sqlite3
from pathlib import Path

RUTA = Path(__file__).with_name("tostadero.db")

ESQUEMA = """
DROP TABLE IF EXISTS lineas_pedido; DROP TABLE IF EXISTS pedidos;
DROP TABLE IF EXISTS incidencias;   DROP TABLE IF EXISTS productos;
DROP TABLE IF EXISTS clientes;

CREATE TABLE clientes (
  id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, tipo TEXT NOT NULL,
  distrito TEXT, email TEXT, condiciones TEXT
);
CREATE TABLE productos (
  sku TEXT PRIMARY KEY, nombre TEXT NOT NULL, categoria TEXT NOT NULL,
  precio REAL NOT NULL, stock INTEGER NOT NULL
);
CREATE TABLE pedidos (
  id INTEGER PRIMARY KEY, cliente_id INTEGER REFERENCES clientes(id),
  fecha TEXT NOT NULL, estado TEXT NOT NULL, total REAL NOT NULL
);
CREATE TABLE lineas_pedido (
  pedido_id INTEGER REFERENCES pedidos(id), sku TEXT REFERENCES productos(sku),
  cantidad INTEGER NOT NULL
);
CREATE TABLE incidencias (
  id INTEGER PRIMARY KEY, cliente_id INTEGER REFERENCES clientes(id),
  maquina TEXT, descripcion TEXT NOT NULL, prioridad TEXT NOT NULL,
  estado TEXT NOT NULL DEFAULT 'abierta', fecha TEXT NOT NULL
);
"""

CLIENTES = [
    (1, "Bar La Esquina", "bar", "Retiro", "pedidos@laesquina.es", "Pago a 30 días"),
    (2, "Restaurante Lumbre", "restaurante", "Chamberí", "compras@lumbre.es", "Pago a 15 días"),
    (3, "Hotel Prado Suites", "hotel", "Centro", "eco@pradosuites.es", "Pago a 60 días, entrega antes de las 9:00"),
    (4, "Cafetería Atocha 12", "cafeteria", "Arganzuela", "hola@atocha12.es", "Pago al contado"),
    (5, "Panadería Ibiza", "cafeteria", "Retiro", "info@panaderiaibiza.es", "Pago a 30 días"),
]
PRODUCTOS = [
    ("CAF-001", "Café de especialidad Etiopía 1 kg", "cafe", 24.50, 120),
    ("CAF-002", "Café blend hostelería 1 kg", "cafe", 16.90, 340),
    ("CAF-003", "Café descafeinado 1 kg", "cafe", 19.80, 45),
    ("MAQ-010", "Cafetera espresso 2 grupos", "maquina", 2890.00, 4),
    ("MOL-020", "Molino on-demand", "maquina", 640.00, 9),
    ("CON-100", "Vasos compostables 8 oz (1000 u.)", "consumible", 54.00, 60),
]
PEDIDOS = [
    (1001, 1, "2026-09-22", "entregado", 169.00),
    (1002, 3, "2026-09-25", "en_reparto", 1225.00),
    (1003, 2, "2026-09-28", "pendiente", 496.40),
    (1004, 1, "2026-09-30", "pendiente", 98.00),
]
LINEAS = [
    (1001, "CAF-002", 10), (1002, "CAF-001", 50), (1003, "CAF-002", 20),
    (1003, "CAF-003", 8), (1004, "CAF-001", 4),
]
INCIDENCIAS = [
    (1, 2, "MAQ-010", "La cafetera pierde presión en el grupo 2", "alta", "abierta", "2026-09-29"),
    (2, 4, "MOL-020", "El molino hace ruido al arrancar", "media", "en_curso", "2026-09-27"),
]

def main() -> None:
    with sqlite3.connect(RUTA) as con:
        con.executescript(ESQUEMA)
        con.executemany("INSERT INTO clientes VALUES (?,?,?,?,?,?)", CLIENTES)
        con.executemany("INSERT INTO productos VALUES (?,?,?,?,?)", PRODUCTOS)
        con.executemany("INSERT INTO pedidos VALUES (?,?,?,?,?)", PEDIDOS)
        con.executemany("INSERT INTO lineas_pedido VALUES (?,?,?)", LINEAS)
        con.executemany("INSERT INTO incidencias VALUES (?,?,?,?,?,?,?)", INCIDENCIAS)
    print(f"Base de datos creada en {RUTA}")

if __name__ == "__main__":
    main()
