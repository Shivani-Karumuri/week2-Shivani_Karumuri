from fastapi import FastAPI
from app.database import engine, Base
from app.models import User, Category, cart, order
from routers.user_router import router as user_router
from routers.category_router import router as category_router
from routers.product_router import router as product_router
from routers import cart_router
from routers.order_router import router as order_router

Base.metadata.create_all(bind= engine)


app= FastAPI(
    title="Online Shopping API",
    description="Backend API for the ABC online shopping application",
    version="1.0.0"
)

app.include_router(user_router)
app.include_router(user_router)
app.include_router(category_router)
app.include_router(product_router)
app.include_router(cart_router.router)
app.include_router(order_router)

@app.get('/')

def home():
    return "Online Shopping API is running successfully"