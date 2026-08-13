from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.security import create_access_token, verify_password
from app.database import get_db
from repositories.user_repository import UserRepository
from schemas.user_schema import Token

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
)

user_repository = UserRepository()


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = user_repository.get_user_by_email(
        db,
        form_data.username,
    )

    if user is None or not verify_password(
        form_data.password,
        user.password,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(
        data={"sub": str(user.user_id)},
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
