import os
import openai

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


def analizar_sentimiento(texto, modelo="text-davinci-002"):
    prompt = f"Por favor, analiza el sentimiento predominante en el siguiente texto:  '{texto}'. El sentimiento es: "
    respuesta = openai.Completion.create(
        engine=modelo, prompt=prompt, temperature=0.5, n=1, max_tokens=50
    )
    return respuesta.choices[0].text.strip()


texto = input("Ingresa un texto: ")
sentimiento = analizar_sentimiento(texto)
print(sentimiento)
