from fastapi import APIRouter, HTTPException
from app import schemas, models
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.service import hash_password

router = APIRouter()

@router.post("/register", status_code=201, response_model=schemas.UserResponse)
def user_register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    email_verification = db.query(models.User).filter(models.User.email == user.email).first()
    if email_verification is not None:
        raise HTTPException(status_code=400, detail="Já existe uma conta com esse email")
    
    new_user = models.User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)

    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user