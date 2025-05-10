from pydantic import BaseModel
from datetime import date


class IncomeBase(BaseModel):
    amount: float
    description: str | None = None
    date: date
    category_id: int


class IncomeCreate(IncomeBase):
    pass


class IncomeOut(IncomeBase):
    id: int

    class Config:
        orm_mode = True
