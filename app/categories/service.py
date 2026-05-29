from app.database import get_db 
from sqlalchemy.orm import Session
from app import models
from sqlalchemy.orm import Session
from fastapi import HTTPException

def create_category(db: Session, user_id, name):
    existing_category = db.query(models.Category).filter(models.Category.name == name, models.Category.id_user == user_id).first()
    if existing_category is not None:
        raise HTTPException(status_code=409, detail="Essa categoria já existe")
    
    
    new_category = models.Category(
        name=name,
        id_user=user_id
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


def get_categories(db: Session, user_id):
    view_all = db.query(models.Category).filter(models.Category.id_user == user_id).all()
    
    return view_all

