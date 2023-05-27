import os
from dotenv import load_dotenv
import openai

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


modelo = "text-davinci-002"
prompt = "Cual es la capital de Francia?"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press ⌘F8 to toggle the breakpoint.
    print("OpenAI: {}".format(OPENAI_API_KEY))

    # models = openai.Model.list()
    # print('Models OpenAI: {}'.format(models))

    respuesta = openai.Completion.create(engine=modelo, prompt=prompt, n=1)

    print(respuesta)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print_hi("PyCharm")
