from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item