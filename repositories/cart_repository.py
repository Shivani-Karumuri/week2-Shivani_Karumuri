from sqlalchemy.orm import Session

from app.models.cart import Cart


class CartRepository:

    def add_to_cart(self, db: Session, cart: Cart):

        db.add(cart)
        db.commit()
        db.refresh(cart)

        return cart

    def get_cart(self, db: Session, user_id: int):
        return db.query(Cart).filter(
            Cart.user_id == user_id
        ).all()

    def get_cart_item(self, db: Session, cart_item_id: int):
        return db.query(Cart).filter(
            Cart.cart_item_id == cart_item_id
        ).first()

    def update_cart(self, db: Session, cart_item: Cart):

        db.commit()
        db.refresh(cart_item)

        return cart_item

    def delete_cart(self, db: Session, cart_item: Cart):

        db.delete(cart_item)
        db.commit()

    def clear_cart(self, db: Session, user_id: int):
        cart_items = db.query(Cart).filter(
            Cart.user_id == user_id
        ).all()

        for item in cart_items:
            db.delete(item)

        db.commit()

    
