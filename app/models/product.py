from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)

    product_name = Column(String(100), nullable=False)

    description = Column(String(255))

    price = Column(Float, nullable=False)

    available_quantity = Column(Integer, nullable=False)

    product_url = Column(String(255), nullable=False)

    category_id = Column(
        Integer,
        ForeignKey("categories.category_id"),
        nullable=False
    )

    category = relationship("Category")
