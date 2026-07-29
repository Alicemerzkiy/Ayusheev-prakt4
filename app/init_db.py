from app.db.db import Base, engine, SessionLocal
from app.db.models import Category
from app.db.crud import create_category, create_book
from app.schemas import BookCreate

# Создание таблиц
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Создание категорий (если их ещё нет)
fiction = db.query(Category).filter(
    Category.title == "Художественная литература"
).first()

if not fiction:
    fiction = create_category(db, "Художественная литература")

programming = db.query(Category).filter(
    Category.title == "Программирование"
).first()

if not programming:
    programming = create_category(db, "Программирование")

# Добавление книг

create_book(
    db,
    BookCreate(
        title="Война и мир",
        description="Роман Л. Н. Толстого",
        price=1200,
        url="https://example.com/war-and-peace",
        category_id=fiction.id
    )
)

create_book(
    db,
    BookCreate(
        title="Преступление и наказание",
        description="Роман Ф. М. Достоевского",
        price=950,
        url="https://example.com/crime-and-punishment",
        category_id=fiction.id
    )
)

create_book(
    db,
    BookCreate(
        title="Изучаем Python",
        description="Учебник по Python",
        price=1800,
        url="https://example.com/learn-python",
        category_id=programming.id
    )
)

create_book(
    db,
    BookCreate(
        title="SQL для начинающих",
        description="Основы SQL",
        price=1500,
        url="https://example.com/sql-start",
        category_id=programming.id
    )
)

db.close()

print("База данных успешно заполнена.")
