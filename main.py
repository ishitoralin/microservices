# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from ldap3 import Server, Connection, ALL, SIMPLE
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

AD_SERVER     = "10.90.1.133"
AD_LDAPS_PORT = 636

class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    message: str
    user: str

class ErrorResponse(BaseModel):
    error: str

class PingResponse(BaseModel):
    message: str

@app.post("/login", response_model=LoginResponse, responses={401: {"model": ErrorResponse}})
async def login(req: LoginRequest):
    email = req.email
    pwd   = req.password

    print(email,pwd)
    try:
        # 建立 LDAPS 連線（加密）
        server = Server(AD_SERVER, port=AD_LDAPS_PORT, use_ssl=True, get_info=ALL)
        conn = Connection(
            server,
            user=email,
            password=pwd,
            authentication=SIMPLE,
            auto_bind=True
        )
        conn.unbind()
        logging.info("AD bind success: %s", email)
        return {"message": "登入成功", "user": email}

    except Exception as e:
        logging.error("AD bind failed for %s: %s", email, e)
        raise HTTPException(status_code=401, detail="帳號或密碼錯誤")
    
@app.get("/ping", response_model=PingResponse, responses={401: {"model": ErrorResponse}})
async def ping():
    return {"message": "pong"}
