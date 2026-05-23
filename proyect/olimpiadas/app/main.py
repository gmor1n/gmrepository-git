
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "Hola Pringao, tu API funciona 🚀"}



def sumar(a, b):
    return a + b

def multiplicar(a, b):


    return a * b

