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


def get_category(db: Session, user_id, category_id):
    view_category = db.query(models.Category).filter(models.Category.id_user == user_id, models.Category.id == category_id).first()
    if view_category is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada ou não pertence ao seu usuario")
    
    return view_category

def update_category(db: Session, user_id, category_id, name):
    category = db.query(models.Category).filter(models.Category.id_user == user_id, models.Category.id == category_id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada ou não pertence ao seu usuario")

    category.name = name

    db.commit()
    db.refresh(category)
    return category

def delete_category(db: Session, user_id, category_id):
    user_category_id = db.query(models.Category).filter(models.Category.id_user == user_id, models.Category.id == category_id).first()
    if user_category_id is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada ou não pertence ao seu usuario")
    
    db.delete(user_category_id)
    db.commit()