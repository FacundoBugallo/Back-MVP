from sqlalchemy.orm import Session
from typing import List, Optional

from app.schemas.income import IncomeCreate, IncomeUpdate
from app.models import Income

def create_income(db: Session, user_id: int, income_data: IncomeCreate) -> Income:
    income = Income(**income_data.dict(), user_id=user_id)
    db.add(income)
    db.commit()
    db.refresh(income)
    return income

def get_incomes(db: Session, user_id: int) -> List[Income]:
    return db.query(Income).filter(Income.user_id == user_id).all()

# Obtener un ingreso específico por ID, validando que pertenezca al usuario
def get_income(db: Session, income_id: int, user_id: int) -> Optional[Income]:
    return db.query(Income).filter(Income.id == income_id, Income.user_id == user_id).first()

def update_income(db: Session, income: Income, updates: IncomeUpdate) -> Income:
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(income, field, value)
    db.commit()
    db.refresh(income)
    return income

def delete_income(db: Session, income: Income):
    db.delete(income)
    db.commit()
