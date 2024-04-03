from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return{"Msg":"Api working sucessfully"}

@app.get("/about")
def about():
    return{"Mgs":"About Page"}

@app.get("/user/{id}")
def user(id:int):
    return{"data":{"id":id}}