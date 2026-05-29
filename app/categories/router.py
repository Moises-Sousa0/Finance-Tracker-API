from fastapi import APIRouter
from app import schemas
from app.categories import service
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.dependencies import get_current_user 
router = APIRouter()

@router.post("/categories", status_code=201, response_model=schemas.CategoryResponse)
def create_category(name: schemas.CategoryCreate, current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    result = service.create_category(db, current_user.id, name.name)
    
    return result