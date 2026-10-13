"""Sesión 1. Streaming: mostrar la respuesta según se genera (mejora la latencia percibida)."""
import os

import anthropic
import openai
from dotenv import load_dotenv
from google import genai

load_dotenv()
PREGUNTA = "Explica en cinco líneas qué es un acuerdo de nivel de servicio (SLA)."

print("--- OpenAI")
for evento in openai.OpenAI().responses.create(
    model=os.environ["OPENAI_MODEL"], input=PREGUNTA, stream=True
):
    if evento.type == "response.output_text.delta":
        print(evento.delta, end="", flush=True)

print("\n--- Claude")
with anthropic.Anthropic().messages.stream(
    model=os.environ["ANTHROPIC_MODEL"], max_tokens=512,
    messages=[{"role": "user", "content": PREGUNTA}],
) as flujo:
    for trozo in flujo.text_stream:
        print(trozo, end="", flush=True)

print("\n--- Gemini")
if os.getenv("GEMINI_API_KEY"):  # opcional: API nativa de Gemini
    cliente = genai.Client()  # en una variable: si no, el SDK cierra el cliente antes de usarlo
    for evento in cliente.interactions.create(
        model=os.environ["GEMINI_MODEL"].removeprefix("google/"), input=PREGUNTA, stream=True
    ):
        if evento.event_type == "step.delta" and evento.delta.type == "text":
            print(evento.delta.text, end="", flush=True)
else:  # por defecto, vía OpenRouter con Chat Completions
    cliente = openai.OpenAI(base_url="https://openrouter.ai/api/v1",
                            api_key=os.environ["OPENROUTER_API_KEY"])
    for trozo in cliente.chat.completions.create(
        model=os.environ["GEMINI_MODEL"], messages=[{"role": "user", "content": PREGUNTA}],
        stream=True,
    ):
        if trozo.choices and trozo.choices[0].delta.content:
            print(trozo.choices[0].delta.content, end="", flush=True)
print()
