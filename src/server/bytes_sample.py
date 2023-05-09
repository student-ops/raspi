from fastapi import FastAPI, Request
import os
from pathlib import Path
import sys

sys.path.append('../')

sys.path.append(str(Path(__file__).resolve().parent.parent))

from address import set_address
from playsound import playsound

app = FastAPI()
_ ,local = set_address.SetAddress()
@app.post("/foo")
async def parse_input(request: Request):
    data: bytes = await request.body()
    print(data)
    dest = "../audio/server.wav"
    f = open(dest,"wb")
    f.write(data)
    f.close()
    return

@app.post("/speak")
async def parse_input(request: Request):
    data: bytes = await request.body()
    print(data)
    dest = "../audio/server.wav"
    f = open(dest,"wb")
    f.write(data)
    f.close()
    if(local):
      playsound(dest)
    return