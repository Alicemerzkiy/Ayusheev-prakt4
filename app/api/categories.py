from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List

from app.db import models, schemas
from app.db.database import get_db

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

@router.get("/", response_model=List[schemas.Category])
def get_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = db.query(models.Category).offset(skip).limit(limit).all()
    return categories

@router.get("/{category_id}", response_model=schemas.Category)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return category

@router.post("/", response_model=schemas.Category, status_code=status.HTTP_201_CREATED)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = models.Category(**category.dict())
    try:
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return db_category
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Категория с таким названием уже существует."
        )

@router.put("/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    
    try:
        for key, value in category.dict().items():
            setattr(db_category, key, value)
        db.commit()
        db.refresh(db_category)
        return db_category
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Категория с таким названием уже существует."
        )

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    
    books_count = db.query(models.Book).filter(models.Book.category_id == category_id).count()
    if books_count > 0:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Нельзя удалить категорию, содержащую книги."
        )
    
    db.delete(db_category)
    db.commit()
    return None
