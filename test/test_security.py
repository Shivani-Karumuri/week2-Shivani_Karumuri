from app.core.security import hash_password, verify_password


def test_password_is_hashed():
    password = "Test@123"

    hashed_password = hash_password(password)

    assert hashed_password != password
    assert verify_password(password, hashed_password)


def test_wrong_password_is_rejected():
    hashed_password = hash_password("Test@123")

    assert not verify_password("WrongPassword", hashed_password)


def test_invalid_hash_is_rejected():
    assert verify_password("Test@123", "invalid-hash") is False
