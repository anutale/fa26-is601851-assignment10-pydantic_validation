from unittest.mock import Mock

from app.models.user import User


def test_user_table_defines_unique_credentials_and_created_at():
    columns = User.__table__.columns

    assert columns["username"].unique is True
    assert columns["email"].unique is True
    assert columns["password_hash"].nullable is False
    assert columns["created_at"].nullable is False
    assert columns["created_at"].default is not None
    assert "password" not in columns


def test_legacy_password_attribute_aliases_password_hash():
    user = User(password="hashed-value")

    assert user.password_hash == "hashed-value"
    assert user.password == "hashed-value"


def test_registration_hashes_password_and_verifies_it():
    db = Mock()
    db.query.return_value.filter.return_value.first.return_value = None
    raw_password = "SecurePass123"

    user = User.register(
        db,
        {
            "first_name": "John",
            "last_name": "Doe",
            "username": "johndoe",
            "email": "john.doe@example.com",
            "password": raw_password,
        },
    )

    assert user.password_hash != raw_password
    assert user.verify_password(raw_password)
    assert not user.verify_password("WrongPass123")
    db.add.assert_called_once_with(user)
