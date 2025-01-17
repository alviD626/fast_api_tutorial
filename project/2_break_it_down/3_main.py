from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def abc():
    return {'data': {'name': 'Sarthak'}}


@app.get("/about")
def abc():
    return {'data': {'about page'}}