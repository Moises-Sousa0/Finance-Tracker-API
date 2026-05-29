from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from fastapi import HTTPException
from passlib.context import CryptContext
import os


load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


def hash_password(password: str):
    return pwd_context.hash(password)
    
def create_token(dados: dict):
    payload = dados.copy()
    expiracao = datetime.now(timezone.utc) + timedelta(minutes=30)
    payload.update({"exp": expiracao})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Login invalido")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalido ou inexistente")

    return user_id

def verify_password(plain_password: str, hashed_password: str): 
    return pwd_context.verify(plain_password, hashed_password)

