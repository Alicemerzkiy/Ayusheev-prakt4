from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

class CategoryBase(BaseModel):
    title: str = Field(..., min_length=1)

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)

class Category(CategoryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class BookBase(BaseModel):
    title: str = Field(..., min_length=1)
    description: str
    price: float = Field(..., gt=0)
    url: str
    category_id: int

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    url: Optional[str] = None
    category_id: Optional[int] = None

class Book(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
