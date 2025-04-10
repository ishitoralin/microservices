from fastapi import FastAPI

app = FastAPI()

USER_SERVICE_URL = "http://user-service:8000"

@app.get("/order")
def hello():
    return {"message": "Hello from Order Service!"}
