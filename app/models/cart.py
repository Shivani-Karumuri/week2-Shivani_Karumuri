from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Cart(Base):
    __tablename__= "Cart"

    cart_item_id = Column(Integer, primary_key=True, index=True)

    user_id= Column(Integer, ForeignKey("users.user_id"), nullable=False)

    product_id= Column(Integer, ForeignKey("products.product_id"), nullable=False)

    quantity= Column(Integer, nullable=False)

    user= relationship("User")
    product= relationship("Product")
