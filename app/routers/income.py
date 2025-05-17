from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app import crud
from app.auth import get_current_user_id
from app.schemas.income import IncomeCreate, IncomeUpdate, IncomeOut

router = APIRouter(prefix="/incomes", tags=["incomes"])

@router.post("/", response_model=IncomeOut, status_code=status.HTTP_201_CREATED)
def create_income(
    income: IncomeCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return crud.income.create_income(db=db, user_id=user_id, income_data=income)

@router.get("/", response_model=List[IncomeOut])
def list_incomes(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return crud.income.get_incomes(db=db, user_id=user_id)

@router.get("/{income_id}", response_model=IncomeOut)
def get_income(
    income_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    income = crud.income.get_income(db=db, income_id=income_id, user_id=user_id)
    if not income:
        raise HTTPException(status_code=404, detail="Ingreso no encontrado")
    return income

@router.put("/{income_id}", response_model=IncomeOut)
def update_income(
    income_id: int,
    updates: IncomeUpdate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    income = crud.income.get_income(db=db, income_id=income_id, user_id=user_id)
    if not income:
        raise HTTPException(status_code=404, detail="Ingreso no encontrado")
    return crud.income.update_income(db=db, income=income, updates=updates)

@router.delete("/{income_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_income(
    income_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    income = crud.income.get_income(db=db, income_id=income_id, user_id=user_id)
    if not income:
        raise HTTPException(status_code=404, detail="Ingreso no encontrado")
    crud.income.delete_income(db=db, income=income)
