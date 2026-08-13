# from typing import List

# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session

# from app.database import get_db
# from schemas.order_schema import OrderCreate, OrderResponse, CheckoutRequest
# from services.order_service import OrderService

# router = APIRouter(
#     prefix="/orders",
#     tags=["Orders"]
# )

# order_service = OrderService()


# @router.post("/checkout", response_model=OrderResponse)
# def checkout(
#     order: CheckoutRequest,
#     db: Session = Depends(get_db)
# ):
#     return order_service.checkout(
#         db,
#         order,
#     )


# @router.get("/history/{user_id}",
#             response_model=List[OrderResponse])
# def order_history(
#     user_id: int,
#     db: Session = Depends(get_db)
# ):
#     return order_service.order_history(
#         db,
#         user_id
#     )


# @router.get("/{order_id}",
#             response_model=OrderResponse)
# def order_details(
#     order_id: int,
#     db: Session = Depends(get_db)
# ):
#     return order_service.order_details(
#         db,
#         order_id
#     )


from typing import List

from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.database import get_db
from app.models.user import User
from app.tasks.order_tasks import process_order_background

from schemas.order_schema import CheckoutRequest, OrderResponse
from services.order_service import OrderService

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)

order_service = OrderService()


@router.post("/checkout", response_model=OrderResponse)
def checkout(
    checkout_request: CheckoutRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    saved_order = order_service.checkout(
        db,
        checkout_request,
        current_user.user_id,
    )

    background_tasks.add_task(
        process_order_background,
        saved_order.order_id,
        current_user.email,
    )

    return saved_order



@router.get("/me", response_model=List[OrderResponse])
def order_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return order_service.order_history(
        db,
        current_user.user_id,
    )


@router.get("/{order_id}", response_model=OrderResponse)
def order_details(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return order_service.order_details(
        db,
        order_id,
        current_user.user_id,
    )

