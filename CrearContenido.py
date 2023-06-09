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


def resumir_texto(texto, tokens, temperatura, modelo="text-davinci-002"):
    prompt = f"Por favor genera un resumen del siguiente texto {texto}\n\n"
    respuesta = openai.Completion.create(
        engine=modelo, prompt=prompt, temperature=temperatura, n=1, max_tokens=tokens
    )
    return respuesta.choices[0].text.strip()


tema = input("Elije un tema para tu articulo: ")
tokens = int(input("Cuantos tokens maximos tendra tu articulo?: "))
temperatura = (
    int(input("Del 1 al 10, Que tan creativo quieres que sea tu articulo?: ")) / 10
)

articulo = crear_contenido(tema, tokens, temperatura)
print(f"El articulo es: \n {articulo}")

resumen = resumir_texto(articulo, tokens, temperatura)
print(f"El resumen del articulo es: \n {resumen}")
