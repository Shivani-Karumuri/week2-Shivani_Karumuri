from sqlalchemy.orm import Session

from app.models.product import Product
from schemas.product_schema import ProductCreate


class ProductRepository:

    def create_product(self, db: Session, product: ProductCreate):

        new_product = Product(
            product_name=product.product_name,
            description=product.description,
            price=product.price,
            available_quantity=product.available_quantity,
            category_id=product.category_id,
            product_url= product.product_url
        )

        db.add(new_product)
        db.commit()
        db.refresh(new_product)

        return new_product

    def get_all_products(self, db: Session):
        return db.query(Product).all()

    def get_product_by_id(self, db: Session, product_id: int):
        return db.query(Product).filter(
            Product.product_id == product_id
        ).first()

    def search_product(self, db: Session, product_name: str):
        return db.query(Product).filter(
            Product.product_name.ilike(f"%{product_name}%")
        ).all()
