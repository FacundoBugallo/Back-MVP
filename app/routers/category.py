from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.auth import get_current_user_id
from app import crud
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryOut

router = APIRouter(prefix="/categories", tags=["categories"])

@router.post("/", response_model=CategoryOut, status_code=status.HTTP_201_CREATED)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return crud.category.create_category(db, user_id, category)

@router.get("/", response_model=List[CategoryOut])
def list_categories(
    type: Optional[str] = None,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return crud.category.get_categories(db, user_id, type_filter=type)

@router.get("/{category_id}", response_model=CategoryOut)
def get_category(
    category_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    category = crud.category.get_category(db, category_id, user_id)
    if not category:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return category

@router.put("/{category_id}", response_model=CategoryOut)
def update_category(
    category_id: int,
    updates: CategoryUpdate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    category = crud.category.get_category(db, category_id, user_id)
    if not category:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return crud.category.update_category(db, category, updates)

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    category = crud.category.get_category(db, category_id, user_id)
    if not category:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    crud.category.delete_category(db, category)
