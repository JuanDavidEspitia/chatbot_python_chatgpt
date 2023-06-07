import os
import openai
import sys

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


def main(args: dict) -> None:

    # models = openai.Model.list()
    # print('Models OpenAI: {}'.format(models))

    modelo = "text-davinci-002"
    prompt1 = "De  que se trata la pelicula el Titanic"

    get_response_gpt(modelo, prompt1)
    """
    Conceptos:
        Temperatura: Creatividad (Que tan aleatoria son las respuestas)
        Tokens Maximos: (Largo) ->
        Cantidad de Respuestas
    """

    prompt2 = "Elije un buen nombre para un perro"
    get_response_gpt_loop(modelo, prompt2, 3)


def get_response_gpt(modelo, prompt):
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        temperature=0.1,
        n=1,  # Cantidad de respuestas
        max_tokens=100,
    )

    print(respuesta)

    text_generado = respuesta.choices[0].text.strip()
    print(text_generado)


def get_response_gpt_loop(modelo, prompt, cant_resp):
    respuesta2 = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        temperature=1,
        n=cant_resp,  # Cantidad de respuestas
        max_tokens=50,
    )

    for idx, opcion in enumerate(respuesta2.choices):
        text_generado = opcion.text.strip()
        print(f"Respuesta {idx + 1}: {text_generado} \n")


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main(sys)
