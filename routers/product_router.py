from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from schemas.product_schema import ProductCreate, ProductResponse
from services.product_service import ProductService

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

product_service = ProductService()


@router.post("/", response_model=ProductResponse)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    return product_service.create_product(db, product)


@router.get("/", response_model=List[ProductResponse])
def get_all_products(
    db: Session = Depends(get_db)
):
    return product_service.get_all_products(db)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product_by_id(
    product_id: int,
    db: Session = Depends(get_db)
):
    return product_service.get_product_by_id(
        db,
        product_id
    )


@router.get("/search/", response_model=List[ProductResponse])
def search_product(
    product_name: str,
    db: Session = Depends(get_db)
):
    return product_service.search_product(
        db,
        product_name
    )
