from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import List
from database import create, all, get_one, update, delete

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

@app.post("/create/", response_model=str)
async def create_todo(item: Item):
    data = {"name": item.name, "description": item.description}
    response = create(data)
    return str(response)

@app.get("/all/", response_model=List[Item])
async def read_all_todos():
    response = all()
    todos = [Item(**todo) for todo in response]
    return todos

@app.get("/get/{name}", response_model=Item)
async def read_todo(name: str):
    response = get_one(name)
    if response:
        return Item(**response)
    else:
        raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/update/{name}", response_model=int)
async def update_todo(name: str, item: Item):
    data = {"name": item.name, "description": item.description}
    response = update(name, data)
    return response

@app.delete("/delete/{name}", response_model=int)
async def delete_todo(name: str):
    response = delete(name)
    return response
