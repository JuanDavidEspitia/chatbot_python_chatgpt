import os
import openai

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


def clasificar_texto(texto, modelo="text-davinci-002"):
    categorias = [
        "arte",
        "ciencia",
        "deportes",
        "economia",
        "educacion",
        "entretenimiento",
        "medio ambiente",
        "politica",
        "salud",
        "tecnologia",
    ]
    prompt = f"Por favor, clasifica el siguiente texto '{texto} en una de las siguientes  categorias {','.join(categorias)}. La categoria es: "
    respuesta = openai.Completion.create(
        engine=modelo, prompt=prompt, temperature=0.5, n=1, max_tokens=50
    )
    return respuesta.choices[0].text.strip()


text = input("Ingrese un texto: ")
clasificacion = clasificar_texto(text)
print(clasificacion)
