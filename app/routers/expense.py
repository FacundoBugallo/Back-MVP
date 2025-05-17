from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app import crud
from app.auth import get_current_user_id
from app.schemas.expense import ExpenseCreate, ExpenseUpdate, ExpenseOut

router = APIRouter(prefix="/expenses", tags=["expenses"])

@router.post("/", response_model=ExpenseOut, status_code=status.HTTP_201_CREATED)
def create_expense(
    expense: ExpenseCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return crud.expense.create_expense(db=db, user_id=user_id, expense_data=expense)

@router.get("/", response_model=List[ExpenseOut])
def list_expenses(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return crud.expense.get_expenses(db=db, user_id=user_id)

@router.get("/{expense_id}", response_model=ExpenseOut)
def get_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    expense = crud.expense.get_expense(db=db, expense_id=expense_id, user_id=user_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Gasto no encontrado")
    return expense

@router.put("/{expense_id}", response_model=ExpenseOut)
def update_expense(
    expense_id: int,
    updates: ExpenseUpdate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    expense = crud.expense.get_expense(db=db, expense_id=expense_id, user_id=user_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Gasto no encontrado")
    return crud.expense.update_expense(db=db, expense=expense, updates=updates)

@router.delete("/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    expense = crud.expense.get_expense(db=db, expense_id=expense_id, user_id=user_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Gasto no encontrado")
    crud.expense.delete_expense(db=db, expense=expense)
