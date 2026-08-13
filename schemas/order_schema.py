# from pydantic import BaseModel
# from datetime import datetime

# class OrderCreate(BaseModel):
#     user_id: int


# class OrderResponse(BaseModel):
#     order_id: int
#     user_id: int
#     total_amount: float
#     order_date: datetime
#     payment_method: str

#     class Config:
#         from_attributes = True

# class CheckoutRequest(BaseModel):
#     user_id: int
#     payment_method: str

from datetime import datetime

from pydantic import BaseModel, Field


class OrderResponse(BaseModel):
    order_id: int
    user_id: int
    total_amount: float
    order_date: datetime
    payment_method: str

    class Config:
        from_attributes = True


class CheckoutRequest(BaseModel):
    payment_method: str = Field(
        ...,
        min_length=2,
        max_length=50,
    )

