from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Literal

# Base
class CategoryBase(BaseModel):
    name: str
    type: Literal["income", "expense"]

# Crear
class CategoryCreate(CategoryBase):
    pass

# Actualizar
class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[Literal["income", "expense"]] = None

# Leer
class CategoryOut(CategoryBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
