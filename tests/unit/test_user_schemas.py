from datetime import datetime
from uuid import uuid4

import pytest
from pydantic import ValidationError

from app.schemas import UserCreate, UserRead


def test_user_create_schema_accepts_registration_fields():
    user = UserCreate(
        username="johndoe",
        email="john.doe@example.com",
        password="SecurePass123",
        first_name="John",
        last_name="Doe",
    )

    assert user.username == "johndoe"
    assert user.email == "john.doe@example.com"
    assert user.password == "SecurePass123"


def test_user_create_rejects_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(
            username="johndoe",
            email="not-an-email",
            password="SecurePass123",
            first_name="John",
            last_name="Doe",
        )


def test_user_read_schema_omits_password_hash():
    user = UserRead.model_validate(
        {
            "id": uuid4(),
            "username": "johndoe",
            "email": "john.doe@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "is_active": True,
            "is_verified": False,
            "created_at": datetime(2026, 1, 1),
            "updated_at": datetime(2026, 1, 1),
            "password_hash": "not-for-output",
        }
    )

    assert "password_hash" not in user.model_dump()
