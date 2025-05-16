from sqlalchemy.orm import Session
from app.models import Expense
from app.schemas.expense import ExpenseCreate, ExpenseUpdate

# Crear un gasto
def create_expense(db: Session, user_id: int, expense_data: ExpenseCreate):
    nuevo_expense = Expense(
        user_id=user_id,
        amount=expense_data.amount,
        description=expense_data.description,
        date=expense_data.date,
        category_id=expense_data.category_id,
    )
    db.add(nuevo_expense)
    db.commit()
    db.refresh(nuevo_expense)
    return nuevo_expense

# Listar todos los gastos de un usuario
def get_expenses(db: Session, user_id: int):
    return db.query(Expense).filter(Expense.user_id == user_id).all()

# Obtener un gasto específico por ID
def get_expense(db: Session, expense_id: int, user_id: int):
    return db.query(Expense).filter(Expense.id == expense_id, Expense.user_id == user_id).first()

# Actualizar un gasto existente
def update_expense(db: Session, expense: Expense, updates: ExpenseUpdate):
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(expense, field, value)
    db.commit()
    db.refresh(expense)
    return expense

# Eliminar un gasto
def delete_expense(db: Session, expense: Expense):
    db.delete(expense)
    db.commit()
