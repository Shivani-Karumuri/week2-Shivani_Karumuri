from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.order import Order
from repositories.order_repository import OrderRepository
from repositories.cart_repository import CartRepository
from schemas.order_schema import OrderCreate, CheckoutRequest
from app.models.order import Order, OrderDetail


class OrderService:

    def __init__(self):
        self.order_repository = OrderRepository()
        self.cart_repository = CartRepository()

    def checkout(self, db: Session, order: CheckoutRequest):

        cart_items = self.cart_repository.get_cart(
            db,
            order.user_id,
        )

        if len(cart_items) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cart is empty"
            )

        total = 0

        for item in cart_items:
            total += item.product.price * item.quantity

        new_order = Order(
            user_id=order.user_id,
            payment_method= order.payment_method,
            total_amount=total
        )

        saved_order = self.order_repository.create_order(
            db,
            new_order
        )

        for item in cart_items:
            order_detail= OrderDetail(
                order_id= saved_order.order_id,
                product_id= item.product_id,
                quantity= item.quantity,
                price= item.product.price
            )
            db.add(order_detail)

        db.commit()

        self.cart_repository.clear_cart(
            db,
            order.user_id
        )

        return saved_order

    def order_history(self, db: Session, user_id: int):
        return self.order_repository.get_order_by_user(
            db,
            user_id
        )

    def order_details(self, db: Session, order_id: int):
        return self.order_repository.get_order_by_id(
            db,
            order_id
        )
