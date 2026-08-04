from fastapi import FastAPI
from app.api import categories
from app.db.database import engine
from app.db import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="PRAKTIKA2026 API")

app.include_router(categories.router)

@app.get("/")
def root():
    return {"message": "API для книг и категорий работает"}
