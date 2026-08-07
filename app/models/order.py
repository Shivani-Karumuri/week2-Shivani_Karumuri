from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime
from datetime import datetime

from app.database import Base


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.user_id"),
        nullable=False
    )

    order_date= Column(DateTime, default=datetime.utcnow)

    payment_method= Column(String(50), nullable=False)

    total_amount = Column(Float, nullable=False)

    user = relationship("User")


class OrderDetail(Base):
    __tablename__ = "order_details"

    detail_id = Column(Integer, primary_key=True, index=True)

    order_id = Column(
        Integer,
        ForeignKey("orders.order_id"),
        nullable=False
    )

    product_id = Column(
        Integer,
        ForeignKey("products.product_id"),
        nullable=False
    )

    quantity = Column(Integer, nullable=False)

    price = Column(Float, nullable=False)

    order = relationship("Order")

    product = relationship("Product")
