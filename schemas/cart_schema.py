# from pydantic import BaseModel

# class CartCreate(BaseModel):
#     user_id: int
#     product_id: int
#     quantity: int

# class CartUpdate(BaseModel):
#     quantity: int

# class CartResponse(BaseModel):
#     cart_item_id: int
#     user_id: int
#     product_id: int
#     quantity: int

#     class Config:
#         from_attributes = True

from pydantic import BaseModel, Field


class CartCreate(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)


class CartUpdate(BaseModel):
    quantity: int = Field(..., gt=0)


class CartResponse(BaseModel):
    cart_item_id: int
    user_id: int
    product_id: int
    quantity: int

    class Config:
        from_attributes = True
