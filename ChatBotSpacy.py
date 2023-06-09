import spacy
import os
import openai

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

preguntas_anteriores = []
respuestas_anteriores = []
modelo_spacy = spacy.load("es_core_news_md")
palabras_prohibidas = ["idiota", "imbecil", "bobo", "tonto"]


def filtrar_lista_negra(text, lista_negra):
    token = modelo_spacy(text)
    resultado = []

    for t in token:
        if t.text.lower() not in lista_negra:
            resultado.append(t.text)
        else:
            resultado.append("[xxxxx]")

    return " ".join(resultado)


def get_completion(prompt, model="text-davinci-002"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=1.5,
        n=1,
        max_tokens=100,
    )
    respuesta_sin_filtro = response.choices[0].text.strip()
    respuesta_con_filtro = filtrar_lista_negra(
        respuesta_sin_filtro, palabras_prohibidas
    )
    return respuesta_con_filtro


print("Bienvenido a nuestro ChatBot Basico. Escribe *Salir* cuando quieres terminar")

while True:
    conversacion_historica = ""
    input_user = input("\nTu:")
    if input_user.lower() == "salir":
        break

    for pregunta, respuesta in zip(preguntas_anteriores, respuestas_anteriores):
        conversacion_historica += f"El usuario pregunta: {pregunta}\n"
        conversacion_historica += f"ChatGPT Responde: {respuesta}\n"

    prompt = f"El usuario pregunta: {input_user} \n"
    conversacion_historica += prompt
    response = get_completion(conversacion_historica)
    print(f"{response}")

    preguntas_anteriores.append(input_user)
    respuestas_anteriores.append(response)
