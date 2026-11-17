from pydantic import BaseModel, EmailStr, ConfigDict
from .models import Role


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: Role


class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: Role

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str
    role: Role