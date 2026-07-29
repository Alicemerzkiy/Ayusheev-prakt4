from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db import crud
from app import schemas

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=list[schemas.Book])
def read_books(category_id: int | None = None, db: Session = Depends(get_db)):
    return crud.get_books(db, category_id)

@router.get("/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=schemas.Book, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    category = crud.get_category(db, book.category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return crud.create_book(db, book)

@router.put("/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    if book.category_id is not None:
        category = crud.get_category(db, book.category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")

    result = crud.update_book(db, book_id, book)
    if not result:
        raise HTTPException(status_code=404, detail="Book not found")

    return result

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    result = crud.delete_book(db, book_id)
    if not result:
        raise HTTPException(status_code=404, detail="Book not found")

    return {"message": "Book deleted"}
