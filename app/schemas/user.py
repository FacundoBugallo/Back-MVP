from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Esquema base
class UserBase(BaseModel):
    name: str
    email: EmailStr

# Para crear un usuario (registro)
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

# Para mostrar un usuario (sin contraseña)
class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
