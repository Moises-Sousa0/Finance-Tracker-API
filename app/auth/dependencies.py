from app.auth.service import verify_token
from fastapi import Depends, HTTPException
from fastapi.security import  OAuth2PasswordBearer
from app.database import get_db
from sqlalchemy.orm import Session
from app import models


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    token_verify = verify_token(token)
    search_user = db.query(models.User).filter(models.User.id == int(token_verify)).first()
    
    if search_user is None:
        raise HTTPException(status_code=401, detail="Usuario não encontrado")

    return search_user