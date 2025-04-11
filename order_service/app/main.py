from fastapi import FastAPI

app = FastAPI()

USER_SERVICE_URL = "http://user-service:8000"

@app.get("")
def hello():
    return {"message": "Order root!"}

@app.get("/hello")
def hello():
    return {"message": "Order Hello!"}

@app.get("/world")
def hello():
    return {"message": "Order world!"}