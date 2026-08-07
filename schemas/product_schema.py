from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    product_name: str
    description: str
    price: float = Field(gt=0)
    available_quantity: int = Field(ge=0)
    category_id: int
    product_url: str


class ProductResponse(BaseModel):
    product_id: int
    product_name: str
    description: str
    price: float
    available_quantity: int
    category_id: int
    product_url: str

    class Config:
        from_attributes = True
