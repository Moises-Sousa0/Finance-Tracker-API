from fastapi import APIRouter
from app import schemas
from app.categories import service
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.dependencies import get_current_user 
from typing import List

router = APIRouter()

@router.post("/categories", status_code=201, response_model=schemas.CategoryResponse)
def create_category(name: schemas.CategoryCreate, current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    result = service.create_category(db, current_user.id, name.name)
    
    return result


@router.get("/categories", status_code=200, response_model=List[schemas.CategoryResponse])
def get_categories(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    result = service.get_categories(db, current_user.id)

    return result

@router.get("/categories/{id}", status_code=200, response_model=schemas.CategoryResponse)
def get_category(id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user) ):
    result = service.get_category(db, current_user.id, id)

    return result