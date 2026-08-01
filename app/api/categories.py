from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

@app.post("/categories/", response_model=schemas.Category)
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

@app.put("/categories/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category is None:
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
