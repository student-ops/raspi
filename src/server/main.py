from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    id:  int


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item