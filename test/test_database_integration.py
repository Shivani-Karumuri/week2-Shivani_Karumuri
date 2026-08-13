from uuid import uuid4

from app.models.user import User


def test_user_is_saved_in_postgresql(db):
    email = f"pytest_{uuid4().hex[:8]}@example.com"

    user = User(
        name="Pytest User",
        email=email,
        password="test-hash",
        mobile="9999999999",
        role="customer",
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    saved_user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    assert saved_user is not None
    assert saved_user.name == "Pytest User"
    assert saved_user.email == email
    assert saved_user.role == "customer"
