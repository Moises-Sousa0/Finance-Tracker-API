from fastapi import APIRouter, HTTPException
from app import schemas, models
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.service import hash_password, verify_password, create_token

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


@router.post("/login", status_code=200, response_model=schemas.LoginResponse)
def user_login(user: schemas.LoginCreate, db: Session = Depends(get_db)):
    login_verification = db.query(models.User).filter(models.User.email == user.email).first()
    if  login_verification is None:
        raise HTTPException(status_code=401, detail="Email ou senha incorreta")
    
    password_verification = verify_password(user.password, login_verification.hash_password)
    if not password_verification:
        raise HTTPException(status_code=401, detail="Email ou senha incorreta")

    token = create_token({"sub": str(login_verification.id)})
    return {"access_token": token, "token_type": "bearer"}
