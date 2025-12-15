from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}


@app.post("/items/")
async def create_item(item: Item):
    return {"created": True, "item": item}