from sqlalchemy.orm import Session
from app.models import Income
from app.schemas.income import IncomeCreate, IncomeUpdate
from typing import List, Optional

# Crear ingreso
def create_income(db: Session, user_id: int, income_data: IncomeCreate) -> Income:
    income = Income(**income_data.dict(), user_id=user_id)
    db.add(income)
    db.commit()
    db.refresh(income)
    return income

# Obtener todos los ingresos de un usuario
def get_incomes(db: Session, user_id: int) -> List[Income]:
    return db.query(Income).filter(Income.user_id == user_id).all()

# Obtener ingreso por ID
def get_income(db: Session, income_id: int, user_id: int) -> Optional[Income]:
    return db.query(Income).filter(Income.id == income_id, Income.user_id == user_id).first()

# Actualizar ingreso
def update_income(db: Session, income: Income, updates: IncomeUpdate) -> Income:
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(income, field, value)
    db.commit()
    db.refresh(income)
    return income

# Eliminar ingreso
def delete_income(db: Session, income: Income):
    db.delete(income)
    db.commit()
