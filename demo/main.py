from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Karibu! This is my first API"}

@app.get("/about")
def about():
    return {"message": "Hello! My name is Cliffe."}
