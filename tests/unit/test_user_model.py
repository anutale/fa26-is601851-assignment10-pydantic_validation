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
