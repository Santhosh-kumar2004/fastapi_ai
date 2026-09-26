import os
from dotenv import load_dotenv
from ollama import Client

from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()
OLLAMA_API_KEY = os.environ.get("OLLAMA_API_KEY")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "gpt-oss:120b")

app=FastAPI()

class Request(BaseModel):
    user_input:str

@app.get('/')
def root():
    return {
        "message":"API is running"
    }
@app.post("/generate")
def generate(input:Request):
    reply=ask_ai(input.user_input)

    return {
    "response": reply
}

def get_client():
    if not OLLAMA_API_KEY:
        raise RuntimeError("OLLAMA_API_KEY is not set in your .env file")

    return Client(
        host="https://ollama.com",
        headers={"Authorization": f"Bearer {OLLAMA_API_KEY}"},
    )


def ask_ai(user_input):
    client = get_client()

    response = client.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
             "role":"user",
            "content":user_input
            }
            ]
    )

    return response["message"]["content"]
