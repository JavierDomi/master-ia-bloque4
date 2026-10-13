"""Sesión 1. Comparativa de proveedores sobre los mismos correos (genera comparativa.csv)."""
import csv

from llm_client import LLM

SISTEMA = ("Eres el asistente de atención al cliente de Tostadero Retiro S.L. "
           "Responde en español y en dos frases como máximo.")
CORREOS = [
    "¿Hacéis entregas los sábados en Chamberí?",
    "La cafetera gotea por el grupo 1 desde esta mañana.",
    "Quiero 15 kg de blend y dos cajas de vasos para el jueves.",
    "¿Por qué la factura de septiembre es más alta que la de agosto?",
    "Somos un hotel nuevo en Centro: ¿qué café nos recomendáis para el desayuno?",
]

with open("comparativa.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["proveedor", "correo", "segundos", "tokens_entrada", "tokens_salida",
                "coste_usd", "calidad_1a5", "respuesta"])
    # TODO (P4): para cada proveedor ("openai", "claude" y "gemini"), crea UN LLM y pásale
    # cada correo de CORREOS con el mismo SISTEMA. Por cada respuesta, escribe una fila con
    # las columnas de la cabecera y en el mismo orden: los segundos con dos decimales y
    # calidad_1a5 vacía (la puntuáis luego en equipo). Imprime una línea por llamada para
    # ver el avance; con 3 proveedores y 5 correos son 15 llamadas.
    pass

print("Hecho: abre comparativa.csv y puntúa la columna calidad_1a5 en equipo.")
