# from typing import List

# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session

# from app.database import get_db
# from schemas.cart_schema import (
#     CartCreate,
#     CartUpdate,
#     CartResponse
# )
# from services.cart_service import CartService

# router = APIRouter(
#     prefix="/cart",
#     tags=["Cart"]
# )

# cart_service = CartService()


# @router.post("/add", response_model=CartResponse)
# def add_to_cart(
#     cart: CartCreate,
#     db: Session = Depends(get_db)
# ):
#     return cart_service.add_to_cart(db, cart)


# @router.get("/{user_id}", response_model=List[CartResponse])
# def get_cart(
#     user_id: int,
#     db: Session = Depends(get_db)
# ):
#     return cart_service.get_cart(db, user_id)


# @router.put("/update/{cart_item_id}", response_model=CartResponse)
# def update_cart(
#     cart_item_id: int,
#     cart: CartUpdate,
#     db: Session = Depends(get_db)
# ):
#     return cart_service.update_cart(
#         db,
#         cart_item_id,
#         cart
#     )


# @router.delete("/remove/{cart_item_id}")
# def delete_cart(
#     cart_item_id: int,
#     db: Session = Depends(get_db)
# ):
#     return cart_service.delete_cart(
#         db,
#         cart_item_id
#     )

from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.database import get_db
from app.models.user import User
from schemas.cart_schema import CartCreate, CartResponse, CartUpdate
from services.cart_service import CartService

router = APIRouter(
    prefix="/cart",
    tags=["Cart"],
)

cart_service = CartService()


@router.post("/add", response_model=CartResponse)
def add_to_cart(
    cart: CartCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return cart_service.add_to_cart(
        db,
        cart,
        current_user.user_id,
    )


@router.get("/me", response_model=List[CartResponse])
def get_my_cart(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return cart_service.get_cart(
        db,
        current_user.user_id,
    )


@router.put("/update/{cart_item_id}", response_model=CartResponse)
def update_cart(
    cart_item_id: int,
    cart: CartUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return cart_service.update_cart(
        db,
        cart_item_id,
        cart,
        current_user.user_id,
    )


@router.delete("/remove/{cart_item_id}")
def delete_cart(
    cart_item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return cart_service.delete_cart(
        db,
        cart_item_id,
        current_user.user_id,
    )
