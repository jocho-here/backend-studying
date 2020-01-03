from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


class User(BaseModel):
    username: str
    full_name: str = None


app = FastAPI()


@app.get("/get")
async def read_items(*, q: str = Query(None, min_length=3, max_length=50, regex="^fixedquery$")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item, user: User, importance: int = Body(...)):
    return {"item_id": item_id, "item": item, "user": user}
