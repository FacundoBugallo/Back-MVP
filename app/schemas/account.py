from pydantic import BaseModel
from datetime import datetime

class AccountBase(BaseModel):
    name:str

class AccountCreate(AccountBase):
    pass

class AccountOut(AccountBase):
    id: int
    created_at: datetime
    
    class Config:
      orm_mode = True