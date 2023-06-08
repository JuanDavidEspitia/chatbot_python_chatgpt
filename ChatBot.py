import sys
import os
import openai

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


def get_completion(prompt, model="text-davinci-002"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=1.5,
        n=1,
        max_tokens=100,
    )
    return response.choices[0].text.strip()


print("Bienvenido a nuestro ChatBot Basico. Escribe *Salir* cuando quieres terminar")

while True:
    input_user = input("\nTu:")
    if input_user.lower() == "salir":
        break
    prompt = f"El usuario pregunta: {input_user} \n ChatGPT Responde:"
    response = get_completion(prompt)
    print(f"ChatBot: {response}")
