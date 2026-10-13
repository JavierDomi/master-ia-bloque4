"""Sesión 1. Una interfaz común para varios proveedores (patrón Adapter).

El resto del bloque usará LLM.responder() cuando el proveedor dé igual."""
import os
import time
from dataclasses import dataclass

import anthropic
import openai
from dotenv import load_dotenv
from google import genai

load_dotenv()

OPENROUTER = "https://openrouter.ai/api/v1"

# Precios en USD por millón de tokens (entrada, salida), con el id del modelo tal y como
# va en .env, p. ej. "openai/gpt-5.4-mini". Rellénalos con https://openrouter.ai/models:
# cambian a menudo y no conviene fiarse de la memoria.
PRECIOS: dict[str, tuple[float, float]] = {}


@dataclass
class Respuesta:
    texto: str
    tokens_entrada: int
    tokens_salida: int
    segundos: float
    modelo: str

    @property
    def coste_usd(self) -> float | None:
        if self.modelo not in PRECIOS:
            return None
        p_in, p_out = PRECIOS[self.modelo]
        return (self.tokens_entrada * p_in + self.tokens_salida * p_out) / 1_000_000


class LLM:
    """proveedor: 'openai' | 'claude' | 'gemini' | 'ollama'.

    Cada proveedor habla un formato de API: Responses (OpenAI), Messages (Claude),
    Interactions (Gemini nativo) o Chat Completions (Gemini vía OpenRouter y Ollama)."""

    def __init__(self, proveedor: str, modelo: str | None = None):
        self.proveedor = proveedor
        defecto = {
            "openai": os.getenv("OPENAI_MODEL"),
            "claude": os.getenv("ANTHROPIC_MODEL"),
            "gemini": os.getenv("GEMINI_MODEL"),
            "ollama": "llama3.2",
        }
        self.modelo = modelo or defecto[proveedor]
        if proveedor == "openai":
            self.formato = "responses"
            self._c = openai.OpenAI(max_retries=3)  # reintentos con espera exponencial
        elif proveedor == "claude":
            self.formato = "messages"
            self._c = anthropic.Anthropic(max_retries=3)
        elif proveedor == "gemini" and os.getenv("GEMINI_API_KEY"):  # opcional: API nativa
            self.formato = "interactions"
            self.modelo = self.modelo.removeprefix("google/")
            self._c = genai.Client()
        elif proveedor == "gemini":  # por defecto, vía OpenRouter
            self.formato = "chat"
            self._c = openai.OpenAI(base_url=OPENROUTER, api_key=os.environ["OPENROUTER_API_KEY"],
                                    max_retries=3)
        elif proveedor == "ollama":  # Ollama expone una API compatible con OpenAI
            self.formato = "chat"
            self._c = openai.OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
        else:
            raise ValueError(f"Proveedor no soportado: {proveedor}")

    def responder(self, sistema: str, prompt: str, temperatura: float | None = None) -> Respuesta:
        extra = {} if temperatura is None else {"temperature": temperatura}
        t0 = time.perf_counter()
        if self.formato == "responses":
            # TODO 1 (P3): OpenAI con la Responses API. Llama a self._c.responses.create(...)
            # con self.modelo, el sistema, el prompt y **extra, y rellena texto, t_in y t_out.
            # Pista: con_openai() en s1_hola_tres.py hace la misma llamada.
            raise NotImplementedError("TODO 1: rama 'responses' (OpenAI)")
        elif self.formato == "messages":
            # TODO 2 (P3): Claude con la Messages API. Llama a self._c.messages.create(...).
            # Ojo: max_tokens es obligatorio, el sistema no va dentro de messages y el texto
            # llega repartido en bloques. Pista: con_claude() en s1_hola_tres.py.
            raise NotImplementedError("TODO 2: rama 'messages' (Claude)")
        elif self.formato == "interactions":
            config = {"generation_config": extra} if extra else {}
            r = self._c.interactions.create(
                model=self.modelo, system_instruction=sistema, input=prompt, **config
            )
            texto, t_in, t_out = r.output_text, r.usage.total_input_tokens, r.usage.total_output_tokens
        else:  # Chat Completions, el formato "clásico" de OpenAI que imitan casi todos
            # Esta rama ya está hecha: úsala de modelo para las dos de arriba.
            r = self._c.chat.completions.create(
                model=self.modelo,
                messages=[{"role": "system", "content": sistema}, {"role": "user", "content": prompt}],
                **extra,
            )
            texto = r.choices[0].message.content
            t_in, t_out = r.usage.prompt_tokens, r.usage.completion_tokens
        return Respuesta(texto, t_in, t_out, time.perf_counter() - t0, self.modelo)


if __name__ == "__main__":
    for proveedor in ["openai", "claude", "gemini"]:
        try:
            r = LLM(proveedor).responder("Responde en una frase.", "¿Qué es un token?")
        except NotImplementedError as e:
            print(f"{proveedor:7} pendiente: {e}")
            continue
        print(f"{proveedor:7} {r.segundos:5.2f} s  {r.tokens_entrada:4}/{r.tokens_salida:<4} {r.texto}")
