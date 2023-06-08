import spacy
import os
import openai
import sys

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


def main(args: dict) -> None:

    model = "text-davinci-002"
    prompt = "Cuenta una historia breve sobre un viaje a un pais europeo"
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=0.1,
        n=1,  # Cantidad de respuestas
        max_tokens=100,
    )

    text_response = response.choices[0].text.strip()
    print(text_response)

    print("*********************************************")

    """
    # Debemos descargar el modelo e instalarlo en la terminal
    # python -m  spacy download es_core_news_md
    """
    modelo_spacy = spacy.load("es_core_news_md")
    analisis = modelo_spacy(text_response)

    """cont = 0
    for token in analisis:
        print('{}: {} -> Grammar Category: {}  -> Dependency: {} , {}'.format(cont, token.text, token.pos_, token.dep_,
                                                                              token.head.text))
        cont += 1"""

    """# Encontrar las entidades
    for entidad in analisis.ents:
        print(entidad.text, entidad.label_)"""

    ubicacion = None
    for ent in analisis.ents:
        if ent.label_ == "LOC":
            ubicacion = ent
            break

    if ubicacion:
        prompt2 = f"Dime mas acerca de {ubicacion}"
        respose2 = openai.Completion.create(
            engine=model,
            prompt=prompt2,
            temperature=0.1,
            n=1,
            max_tokens=100,
        )
        print(respose2.choices[0].text.strip())


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main(sys)
