import os
import openai

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


def crear_contenido(tema, tokens, temperatura, modelo="text-davinci-002"):
    prompt = f"Por favor escribe un articulo corto sobre el tema {tema}"
    respuesta = openai.Completion.create(
        engine=modelo, prompt=prompt, temperature=temperatura, n=1, max_tokens=tokens
    )
    return respuesta.choices[0].text.strip()
