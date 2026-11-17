"""Sesión 4 (P4, demo del profesor). ¿Dónde vive el estado? La misma conversación con Gemini
nativo dos veces: reenviando el historial (en la aplicación) o con previous_interaction_id
(en el proveedor). Necesita la clave gratuita de AI Studio: por OpenRouter no hay estado."""
import os
import sys

from dotenv import load_dotenv
from google import genai

load_dotenv()
if not os.getenv("GEMINI_API_KEY"):
    sys.exit("Falta GEMINI_API_KEY en .env. Crea una clave gratuita en https://aistudio.google.com/ "
             "(OpenRouter no guarda estado, así que esta demo solo funciona con Gemini nativo).")

cliente = genai.Client()  # lee GEMINI_API_KEY
MODELO = os.environ["GEMINI_MODEL"].removeprefix("google/")
SISTEMA = "Eres el asistente comercial de Tostadero Retiro. Responde en español, en una o dos frases."
TURNOS = [
    "Hola, soy del Hotel Prado Suites.",
    "Necesitamos 30 kg de café Etiopía cada semana, entregados antes de las 9:00.",
    "¿Qué molino nos recomendáis para ese volumen?",
    "Recuérdame: ¿qué cantidad semanal te dije y a qué hora entregáis?",
]


def informe(n: int, enviado: str, r) -> None:
    # Caracteres: lo que sale de tu programa. Tokens de entrada: lo que el modelo lee en total.
    print(f"  Turno {n}: envías {len(enviado):>4} caracteres · "
          f"{r.usage.total_input_tokens:>4} tokens de entrada · {r.usage.total_output_tokens} de salida")


def estado_en_la_aplicacion() -> str:
    """Sin estado: cada llamada lleva la transcripción completa, que guardamos nosotros."""
    historial = ""
    for n, texto in enumerate(TURNOS, 1):
        historial += f"Cliente: {texto}\n"
        r = cliente.interactions.create(model=MODELO, system_instruction=SISTEMA, input=historial)
        informe(n, historial, r)
        historial += f"Asistente: {r.output_text}\n"
    return r.output_text


def estado_en_el_proveedor() -> str:
    """Con estado: solo enviamos el turno nuevo y el id de la interacción anterior."""
    anterior = None  # la conversación queda guardada en los servidores de Google
    for n, texto in enumerate(TURNOS, 1):
        r = cliente.interactions.create(model=MODELO, system_instruction=SISTEMA, input=texto,
                                        previous_interaction_id=anterior)
        informe(n, texto, r)
        anterior = r.id
    return r.output_text


if __name__ == "__main__":
    print("A) Estado en la aplicación (reenviar el historial):")
    print("  Última respuesta:", estado_en_la_aplicacion())
    print("\nB) Estado en el proveedor (previous_interaction_id):")
    print("  Última respuesta:", estado_en_el_proveedor())
