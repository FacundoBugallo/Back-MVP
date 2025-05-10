from pydantic import BaseModel, EmailStr
from datetime import datetime

#login de usuario
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Esquema base
class UserBase(BaseModel):
    name: str
    email: EmailStr

# crear un usuario (registro)
class UserCreate(UserBase):
    password: str

# Para mostrar un usuario (sin contraseña)
class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
