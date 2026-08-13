# from fastapi import APIRouter, Depends, status
# from sqlalchemy.orm import Session

# from app.database import get_db
# from schemas.user_schema import UserCreate, UserResponse, UserLogin
# from services.user_service import UserService


# router = APIRouter(
#     prefix = "/users",
#     tags= ["Users"]
# )

# user_service = UserService()

# @router.post("/register", response_model= UserResponse)
# def register_user(user: UserCreate, db: Session = Depends(get_db)):
#     return user_service.register_user(db, user)

# @router.post('/login')
# def login_user(user: UserLogin, db: Session= Depends(get_db)):
#     return user_service.login_user(db, user)


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.database import get_db
from app.models.user import User
from schemas.user_schema import UserCreate, UserResponse
from services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

user_service = UserService()


@router.post("/register", response_model=UserResponse)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    return user_service.register_user(db, user)


@router.get("/me", response_model=UserResponse)
def get_my_profile(
    current_user: User = Depends(get_current_user),
):
    return current_user
