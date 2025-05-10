from pydantic import BaseModel
from datetime import datetime


class CategoryBase(BaseModel):
    name: str
    type: str  


class CategoryCreate(CategoryBase):
    pass


class CategoryOut(CategoryBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
