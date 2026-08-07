from pydantic import BaseModel
from datetime import datetime

class OrderCreate(BaseModel):
    user_id: int


class OrderResponse(BaseModel):
    order_id: int
    user_id: int
    total_amount: float
    order_date: datetime
    payment_method: str

    class Config:
        from_attributes = True

class CheckoutRequest(BaseModel):
    user_id: int
    payment_method: str


