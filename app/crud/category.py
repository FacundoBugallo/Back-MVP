from sqlalchemy.orm import Session
from typing import List, Optional
from app.models import Category
from app.schemas.category import CategoryCreate, CategoryUpdate

def create_category(db: Session, user_id: int, data: CategoryCreate) -> Category:
    category = Category(**data.dict(), user_id=user_id)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def get_categories(db: Session, user_id: int, type_filter: Optional[str] = None) -> List[Category]:
    query = db.query(Category).filter(Category.user_id == user_id)
    if type_filter:
        query = query.filter(Category.type == type_filter)
    return query.all()

def get_category(db: Session, category_id: int, user_id: int) -> Optional[Category]:
    return db.query(Category).filter(Category.id == category_id, Category.user_id == user_id).first()

def update_category(db: Session, category: Category, updates: CategoryUpdate) -> Category:
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(category, field, value)
    db.commit()
    db.refresh(category)
    return category

def delete_category(db: Session, category: Category):
    db.delete(category)
    db.commit()
