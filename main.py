import string
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
 

@app.get("/decklist")
def read_decklist():
    decklist = ["Ronaldo", "Neymar"]
    print("Received call")
    return decklist

@app.get("/decklist/{deckname}")
def read_deck(deckname: str):
    if deckname == "Ronaldo":
        return {"Real":"Madrid", "Paris":"Saint Germain"}
    elif (deckname == "Neymar"):
        return {"Selecao": "Canarinha", }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}