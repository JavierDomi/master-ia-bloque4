"""Sesión 4. Memoria de corto plazo desde cero: compactar el historial cuando crece."""
import os

import anthropic
from dotenv import load_dotenv

load_dotenv()
llm = anthropic.Anthropic()
MODELO = os.environ["ANTHROPIC_MODEL"]
SISTEMA = "Eres el asistente comercial de Tostadero Retiro. Responde en español, con brevedad."
UMBRAL_TOKENS = 1000  # bajo a propósito, para ver la compactación en clase
MANTENER = 6          # mensajes recientes que se conservan literales (número par)


def compactar(mensajes: list[dict]) -> list[dict]:
    antiguos, recientes = mensajes[:-MANTENER], mensajes[-MANTENER:]
    transcripcion = "\n".join(f"{m['role']}: {m['content']}" for m in antiguos)
    r = llm.messages.create(
        model=MODELO, max_tokens=600,
        system=("Resume esta conversación de atención al cliente. Conserva datos concretos: "
                "nombres, ids, cantidades, fechas, compromisos adquiridos y temas pendientes."),
        messages=[{"role": "user", "content": transcripcion}],
    )
    resumen = "".join(b.text for b in r.content if b.type == "text")
    return [
        {"role": "user", "content": f"[Resumen de la conversación hasta aquí]\n{resumen}"},
        {"role": "assistant", "content": "Entendido. Continúo con ese contexto."},
        *recientes,  # empieza por un mensaje de usuario porque MANTENER es par
    ]


if __name__ == "__main__":
    historial: list[dict] = []
    tokens_historial = 0  # tamaño del historial según el uso que devolvió la última llamada
    while texto := input("Cliente: ").strip():
        if len(historial) > MANTENER and tokens_historial > UMBRAL_TOKENS:
            historial = compactar(historial)
            print("   (historial compactado)")
        historial.append({"role": "user", "content": texto})
        r = llm.messages.create(model=MODELO, max_tokens=800, system=SISTEMA, messages=historial)
        tokens_historial = r.usage.input_tokens + r.usage.output_tokens
        respuesta = "".join(b.text for b in r.content if b.type == "text")
        historial.append({"role": "assistant", "content": respuesta})
        print(f"Asistente: {respuesta}\n   [{r.usage.input_tokens} tokens de entrada en esta llamada]")
