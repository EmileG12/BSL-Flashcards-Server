import string
from typing import Union

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import os

from fastapi.responses import FileResponse

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


@app.get("/videofileresponse")
async def video_endpoint():

    absolute_path = os.path.dirname(__file__)
    relative_path = "answers/hello.mp4"
    video_path = os.path.join(absolute_path, relative_path)
    print("Requested video")
    return FileResponse(video_path)


@app.get("/decklist/videotest")
async def video_endpoint():
    absolute_path = os.path.dirname(__file__)
    relative_path = "answers/hello.mp4"
    video_path= os.path.join(absolute_path, relative_path)
    def iterfile():
        with open(video_path, mode="rb") as file_like:
            yield from file_like
    return StreamingResponse(iterfile(), media_type="video/mp4")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}