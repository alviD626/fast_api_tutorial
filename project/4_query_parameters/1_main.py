from fastapi import FastAPI

app = FastAPI()


@app.get("/blog")
def index(limit):
    return {"data": f"{limit} blogs from the db"}

@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}