import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.models import (
    Cart,
    Category,
    Order,
    OrderDetail,
    Product,
    User,
)


TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

test_engine = (
    create_engine(TEST_DATABASE_URL, pool_pre_ping=True)
    if TEST_DATABASE_URL
    else None
)

TestingSessionLocal = (
    sessionmaker(
        bind=test_engine,
        autocommit=False,
        autoflush=False,
    )
    if test_engine
    else None
)


@pytest.fixture()
def db():
    if test_engine is None:
        pytest.skip(
            "TEST_DATABASE_URL is not set"
        )

    Base.metadata.create_all(bind=test_engine)

    session = TestingSessionLocal()

    try:
        yield session
    finally:
        session.close()

