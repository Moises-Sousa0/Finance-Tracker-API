from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    name: str
    email: str
    password: str = Field(min_length=5, max_length=72)

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        from_attributes = True


class LoginCreate(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str 