from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200, examples=["Camiseta Básica"])
    description: Optional[str] = Field(None, examples=["Camiseta 100% algodão"])
    price: float = Field(..., gt=0, examples=[29.99])
    category: str = Field(..., min_length=1, max_length=100, examples=["Roupas"])
    stock: int = Field(0, ge=0, examples=[100])
    sku: Optional[str] = Field(None, max_length=100, examples=["CAM-BASIC-001"])


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    category: Optional[str] = Field(None, min_length=1, max_length=100)
    stock: Optional[int] = Field(None, ge=0)
    sku: Optional[str] = Field(None, max_length=100)


class ProductResponse(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class ProductList(BaseModel):
    total: int
    page: int
    page_size: int
    items: list[ProductResponse]
