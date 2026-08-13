from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException

from schemas.order_schema import CheckoutRequest
from services.order_service import OrderService

def test_checkout_empty_cart():
    db = MagicMock()
    service = OrderService()

    service.cart_repository = MagicMock()
    service.order_repository = MagicMock()

    service.cart_repository.get_cart.return_value = []

    checkout_data = CheckoutRequest(
        payment_method="UPI"
    )

    with pytest.raises(HTTPException) as error:
        service.checkout(
            db,
            checkout_data,
            user_id=1
        )

    assert error.value.status_code == 400
    assert error.value.detail == "Cart is empty"

def test_order_history():
    db = MagicMock()
    service = OrderService()

    service.order_repository = MagicMock()

    expected_orders = [
        SimpleNamespace(order_id=1, user_id=1)
    ]

    service.order_repository.get_order_by_user.return_value = (
        expected_orders
    )

    result = service.order_history(
        db,
        user_id=1
    )

    assert result == expected_orders
    service.order_repository.get_order_by_user.assert_called_once_with(
        db,
        1
    )

def test_order_details_wrong_user():
    db = MagicMock()
    service = OrderService()

    service.order_repository = MagicMock()

    order = SimpleNamespace(
        order_id=10,
        user_id=2
    )

    service.order_repository.get_order_by_id.return_value = order

    with pytest.raises(HTTPException) as error:
        service.order_details(
            db,
            order_id=10,
            user_id=1
        )

    assert error.value.status_code == 404
    assert error.value.detail == "Order not found"

