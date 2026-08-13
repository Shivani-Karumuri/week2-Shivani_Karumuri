from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException

from schemas.cart_schema import CartCreate
from services.cart_service import CartService

def test_add_to_cart_success():
    db = MagicMock()
    service = CartService()

    service.product_repository = MagicMock()
    service.cart_repository = MagicMock()


    product = SimpleNamespace(
        product_id=1,
        available_quantity=10,
        price=100
    )

    service.product_repository.get_product_by_id.return_value = product
    service.cart_repository.add_to_cart.side_effect = (
        lambda db, cart: cart
    )

    cart_data = CartCreate(
        product_id=1,
        quantity=2
    )

    result = service.add_to_cart(
        db,
        cart_data,
        user_id=5
    )

    assert result.user_id == 5
    assert result.product_id == 1
    assert result.quantity == 2


def test_add_to_cart_product_not_found():
    db = MagicMock()
    service = CartService()

    service.product_repository = MagicMock()
    service.cart_repository = MagicMock()


    service.product_repository.get_product_by_id.return_value = None

    cart_data = CartCreate(
        product_id=999,
        quantity=1
    )

    with pytest.raises(HTTPException) as error:
        service.add_to_cart(
            db,
            cart_data,
            user_id=5
        )

    assert error.value.status_code == 404
    assert error.value.detail == "Product not found"


def test_add_to_cart_insufficient_stock():
    db = MagicMock()
    service = CartService()

    service.product_repository = MagicMock()
    service.cart_repository = MagicMock()


    product = SimpleNamespace(
        product_id=1,
        available_quantity=2,
        price=100
    )

    service.product_repository.get_product_by_id.return_value = product

    cart_data = CartCreate(
        product_id=1,
        quantity=5
    )

    with pytest.raises(HTTPException) as error:
        service.add_to_cart(
            db,
            cart_data,
            user_id=5
        )

    assert error.value.status_code == 400
    assert error.value.detail == "Not enough stock"
