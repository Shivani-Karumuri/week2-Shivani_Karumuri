from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.cart import Cart
from repositories.cart_repository import CartRepository
from repositories.user_repository import UserRepository
from repositories.product_repository import ProductRepository
from schemas.cart_schema import CartCreate, CartUpdate


class CartService:

    def __init__(self):
        self.cart_repository = CartRepository()
        self.user_repository = UserRepository()
        self.product_repository = ProductRepository()

    def add_to_cart(self, db: Session, cart: CartCreate):

        user = self.user_repository.get_user_by_id(db, cart.user_id)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        product = self.product_repository.get_product_by_id(
            db,
            cart.product_id
        )

        if product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            )

        if cart.quantity > product.available_quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Not enough stock"
            )

        new_cart = Cart(
            user_id=cart.user_id,
            product_id=cart.product_id,
            quantity=cart.quantity
        )

        return self.cart_repository.add_to_cart(db, new_cart)

    def get_cart(self, db: Session, user_id: int):
        return self.cart_repository.get_cart(db, user_id)

    def update_cart(self, db: Session,
                    cart_item_id: int,
                    cart_update: CartUpdate):

        cart_item = self.cart_repository.get_cart_item(
            db,
            cart_item_id
        )

        if cart_item is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cart item not found"
            )

        cart_item.quantity = cart_update.quantity

        return self.cart_repository.update_cart(db, cart_item)

    def delete_cart(self, db: Session, cart_item_id: int):

        cart_item = self.cart_repository.get_cart_item(
            db,
            cart_item_id
        )

        if cart_item is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cart item not found"
            )

        self.cart_repository.delete_cart(db, cart_item)

        return {
            "message": "Item removed from cart"
        }
