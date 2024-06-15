import string
from typing import Union

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import os
import re
from fastapi.responses import FileResponse

app = FastAPI()
def sanitize_paths(path):
    return re.sub(r'\W+', '', path)


@app.get("/")
def read_root():
    return {"Hello": "World"}
 

@app.get("/decklist")
def read_decklist():
    absolute_path = os.path.dirname(__file__)
    relative_path = "answers/"
    answers_path = os.path.join(absolute_path, relative_path)
    return os.listdir(answers_path)


@app.get("/decklist/{deckname}")
def read_deck(deckname: str):
    deckname = sanitize_paths(deckname)
    absolute_path = os.path.dirname(__file__)
    relative_path = "answers/"
    answers_path = os.path.join(absolute_path, relative_path)
    deck_path = os.path.join(answers_path, deckname)
    return os.listdir(deck_path)


@app.get("/videofileresponse")
async def video_endpoint():

    absolute_path = os.path.dirname(__file__)
    relative_path = "answers/Helloworld/hello.mp4"
    video_path = os.path.join(absolute_path, relative_path)
    print("Requested video")
    return FileResponse(video_path)

def create_vid_path(params:list = []):
    absolute_path = os.path.dirname(__file__)

    for i in params:
        absolute_path = os.path.join(absolute_path, i)

    return absolute_path

@app.get("/getvideo/")
async def get_video(deckname: str = "None", videoname: str = "None"):
    video_path = create_vid_path(["answers",deckname,videoname])
    async def iterfile():
        with open(video_path, mode="rb") as file_like:
            for chunk in iter(lambda: file_like.read(65536), b""):
                yield chunk
                
    return StreamingResponse(iterfile(), media_type="video/mp4")


@app.get("/videotest")
async def video_endpoint():
    absolute_path = os.path.dirname(__file__)
    relative_path = r"answers/Helloworld/hello.mp4"
    video_path = os.path.join(absolute_path, relative_path)
    print(video_path)
    async def iterfile():
        with open(video_path, mode="rb") as file_like:
            for chunk in iter(lambda: file_like.read(65536), b""):
                yield chunk

    return StreamingResponse(iterfile(), media_type="video/mp4")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}