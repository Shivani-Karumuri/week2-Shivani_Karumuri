from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from repositories.product_repository import ProductRepository
from repositories.category_repository import CategoryRepository
from schemas.product_schema import ProductCreate


class ProductService:

    def __init__(self):
        self.product_repository = ProductRepository()
        self.category_repository = CategoryRepository()

    def create_product(self, db: Session, product: ProductCreate):

        category = self.category_repository.get_category_by_id(
            db,
            product.category_id
        )

        if category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found"
            )

        return self.product_repository.create_product(db, product)

    def get_all_products(self, db: Session):
        return self.product_repository.get_all_products(db)

    def get_product_by_id(self, db: Session, product_id: int):

        product = self.product_repository.get_product_by_id(
            db,
            product_id
        )

        if product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            )

        return product

    def search_product(self, db: Session, product_name: str):
        return self.product_repository.search_product(
            db,
            product_name
        )
