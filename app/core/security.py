from datetime import datetime, timedelta, timezone
import os
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from passlib.exc import UnknownHashError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User

SECRET_KEY = os.getenv(
    "JWT_SECRET_KEY",
    "dev-only-change-this-secret-key-before-production",
)
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="api/auth/login",
)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except (UnknownHashError, ValueError):
        return False


def create_access_token(
    data: dict,
    expires_delta: timedelta | None = None,
) -> str:
    payload = data.copy()
    expire_time = datetime.now(timezone.utc) + (
        expires_delta
        or timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    )
    payload.update({"exp": expire_time})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired authentication token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )
        user_id = int(payload.get("sub", ""))
    except (JWTError, TypeError, ValueError):
        raise credentials_exception

    user = (
        db.query(User)
        .filter(User.user_id == user_id)
        .first()
    )

    if user is None:
        raise credentials_exception

    return user

def require_roles(*allowed_roles: str):
    def role_dependency(
        current_user: User = Depends(get_current_user)
    ):
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient role permissions"
            )

        return current_user

    return role_dependency


