from pydantic import BaseModel
from datetime import date


class ExpenseBase(BaseModel):
    amount: float
    description: str | None = None
    date: date
    category_id: int


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseOut(ExpenseBase):
    id: int

    class Config:
        orm_mode = True

class ExpenseUpdate(BaseModel):
    amount: float | None = None
    description: str | None = None
    date: date | None = None
    category_id: int | None = None
