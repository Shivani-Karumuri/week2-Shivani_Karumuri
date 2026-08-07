from sqlalchemy.orm import Session

from app.models.order import Order


class OrderRepository:

    def create_order(self, db: Session, order: Order):

        db.add(order)
        db.commit()
        db.refresh(order)

        return order

    def get_order_by_user(self, db: Session, user_id: int):
        return db.query(Order).filter(
            Order.user_id == user_id
        ).all()

    def get_order_by_id(self, db: Session, order_id: int):
        return db.query(Order).filter(
            Order.order_id == order_id
        ).first()
