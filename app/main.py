# from fastapi import FastAPI
# from app.database import engine, Base
# from app.models import User, Category, cart, order
# from routers.user_router import router as user_router
# from routers.category_router import router as category_router
# from routers.product_router import router as product_router
# from routers import cart_router
# from routers.order_router import router as order_router

# Base.metadata.create_all(bind= engine)


# app= FastAPI(
#     title="Online Shopping API",
#     description="Backend API for the ABC online shopping application",
#     version="1.0.0"
# )

# app.include_router(user_router)
# app.include_router(category_router)
# app.include_router(product_router)
# app.include_router(cart_router.router)
# app.include_router(order_router)

# @app.get('/')

# def home():
#     return "Online Shopping API is running successfully"

# from fastapi import FastAPI

# from app.database import Base, engine
# from app.models import (
#     Cart as _Cart,
#     Category as _Category,
#     Order as _Order,
#     OrderDetail as _OrderDetail,
#     Product as _Product,
#     User as _User,
# )
# from app.routers.auth_router import router as auth_router
# from routers.cart_router import router as cart_router
# from routers.category_router import router as category_router
# from routers.order_router import router as order_router
# from routers.product_router import router as product_router
# from routers.user_router import router as user_router

# Base.metadata.create_all(bind=engine)

# app = FastAPI(
#     title="Online Shopping API",
#     description="Backend API for the ABC online shopping application",
#     version="1.0.0",
# )

# app.include_router(auth_router)
# app.include_router(user_router)
# app.include_router(category_router)
# app.include_router(product_router)
# app.include_router(cart_router)
# app.include_router(order_router)



# @app.get("/")
# def home():
#     return "Online Shopping API is running successfully"

import logging
import asyncio
from time import perf_counter

from fastapi import FastAPI, Request, HTTPException, BackgroundTasks
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.logging_config import configure_logging
from app.database import Base, engine


from app.models import (
    Cart as _Cart,
    Category as _Category,
    Order as _Order,
    OrderDetail as _OrderDetail,
    Product as _Product,
    User as _User,
)

from app.routers.auth_router import router as auth_router

from routers.cart_router import router as cart_router
from routers.category_router import router as category_router
from routers.order_router import router as order_router
from routers.product_router import router as product_router
from routers.user_router import router as user_router


# Configure logging before starting the application
configure_logging()

logger = logging.getLogger("shopping_api")


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Online Shopping API",
    description="Backend API for the ABC online shopping application",
    version="1.0.0",
)

@app.exception_handler(HTTPException)
async def http_exception_handler(
    request: Request,
    exc: HTTPException,
):
    logger.warning(
        "%s %s -> %s | %s",
        request.method,
        request.url.path,
        exc.status_code,
        exc.detail,
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": jsonable_encoder(exc.detail)
        },
        headers=exc.headers,
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
    logger.warning(
        "Validation error: %s %s | %s",
        request.method,
        request.url.path,
        exc.errors(),
    )

    return JSONResponse(
        status_code=422,
        content={
            "detail": "Request validation failed",
            "errors": jsonable_encoder(exc.errors()),
        },
    )


@app.exception_handler(Exception)
async def general_exception_handler(
    request: Request,
    exc: Exception,
):
    logger.exception(
        "Unhandled exception: %s %s",
        request.method,
        request.url.path,
    )

    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error"
        },
    )



@app.middleware("http")
async def request_logging_middleware(
    request: Request,
    call_next
):
    start_time = perf_counter()

    try:
        response = await call_next(request)

        elapsed_time = perf_counter() - start_time

        logger.info(
            "%s %s -> %s in %.3f seconds",
            request.method,
            request.url.path,
            response.status_code,
            elapsed_time,
        )

        return response

    except Exception:
        elapsed_time = perf_counter() - start_time

        logger.exception(
            "%s %s failed after %.3f seconds",
            request.method,
            request.url.path,
            elapsed_time,
        )

        raise



async def run_background_job(message: str):
    logger.info("Background job started: %s", message)

    # Simulates slow async work
    await asyncio.sleep(2)

    logger.info("Background job completed: %s", message)



app.include_router(auth_router)
app.include_router(user_router)
app.include_router(category_router)
app.include_router(product_router)
app.include_router(cart_router)
app.include_router(order_router)


@app.get("/")
def home():
    logger.info("Home endpoint called")

    return {
        "message": "Online Shopping API is running successfully"
    }


@app.post("/milestone5/background-test")
def background_test(background_tasks: BackgroundTasks):

    background_tasks.add_task(
        run_background_job,
        "Milestone 5 background task test"
    )

    logger.info("Background job scheduled")

    return {
        "message": "Background job scheduled successfully"
    }


