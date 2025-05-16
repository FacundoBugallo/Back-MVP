from __future__ import annotations
from pydantic import BaseModel
from datetime import date
from typing import Optional

# Base común para ingreso
class IncomeBase(BaseModel):
    amount: float
    description: Optional[str] = None
    date: date
    category_id: int

# Crear ingreso
class IncomeCreate(IncomeBase):
    pass

# Actualizar ingreso
class IncomeUpdate(BaseModel):
    amount: Optional[float] = None
    description: Optional[str] = None
    date: Optional[date] = None
    category_id: Optional[int] = None

# Para mostrar un ingreso
class IncomeOut(IncomeBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
