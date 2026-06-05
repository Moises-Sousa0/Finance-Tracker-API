from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    password: str = Field(min_length=5, max_length=72)

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        from_attributes = True #permite ler dados diretamente de objetos/classes, como modelos do sqlaclheemy



class LoginCreate(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str 



class CategoryCreate(BaseModel):
    name: str

class CategoryResponse(BaseModel):
    id: int
    name: str
    id_user: int
    class Config:
        from_attributes = True

class CategoryUpdate(BaseModel):
    name: str | None = None



class TransactionCreate(BaseModel):
    type: str
    value: int
    date_transaction: date
    name: str
    id_category: int

class TransactionResponse(BaseModel):
    id: int
    type: str
    valte: int
    date_transaction: date
    name: str
    id_category: int
    id_user: int
    class Config:
        from_attributes = True #permite ler dados diretamente de objetos/classes, como modelos do sqlaclheemy
