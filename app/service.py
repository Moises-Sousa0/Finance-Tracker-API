from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from app import models, schemas
import os


load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORTIHM = os.getenv("ALGORTIHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") 

def hash_password():
    hash_senha = pwd_context.hash()

def criar_token(dados: dict):
    payload = dados.copy()
    expiracao = datetime.now(timezone.utc) + timedelta(minutes=30)
    payload.update({"exp": expiracao})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORTIHM)


