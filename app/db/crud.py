from sqlalchemy.orm import Session
from app.db.models import Category, Book

# ---------------------- CATEGORY ----------------------

def get_categories(db: Session):
    return db.query(Category).all()

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def create_category(db: Session, title: str):
    category = Category(title=title)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def update_category(db: Session, category_id: int, data):
    category = get_category(db, category_id)

    if category:
        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(category, key, value)

        db.commit()
        db.refresh(category)

    return category

def delete_category(db: Session, category_id: int):
    category = get_category(db, category_id)

    if category:
        db.delete(category)
        db.commit()

    return category

# ---------------------- BOOK ----------------------

def get_books(db: Session, category_id=None):
    query = db.query(Book)

    if category_id:
        query = query.filter(Book.category_id == category_id)

    return query.all()

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, data):
    book = Book(**data.model_dump())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def update_book(db: Session, book_id: int, data):
    book = get_book(db, book_id)

    if book:
        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(book, key, value)

        db.commit()
        db.refresh(book)

    return book

def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)

    if book:
        db.delete(book)
        db.commit()

    return book
