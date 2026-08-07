from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from schemas.order_schema import OrderCreate, OrderResponse, CheckoutRequest
from services.order_service import OrderService

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

order_service = OrderService()


@router.post("/checkout", response_model=OrderResponse)
def checkout(
    order: CheckoutRequest,
    db: Session = Depends(get_db)
):
    return order_service.checkout(
        db,
        order,
    )


@router.get("/history/{user_id}",
            response_model=List[OrderResponse])
def order_history(
    user_id: int,
    db: Session = Depends(get_db)
):
    return order_service.order_history(
        db,
        user_id
    )


@router.get("/{order_id}",
            response_model=OrderResponse)
def order_details(
    order_id: int,
    db: Session = Depends(get_db)
):
    return order_service.order_details(
        db,
        order_id
    )

