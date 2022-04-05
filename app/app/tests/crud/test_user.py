
from app import crud
from app.schemas.user import UserCreate, UserUpdate
from app.tests.utils.utils import random_email, random_lower_string


def test_create_user():
    email = random_email()
    password = random_lower_string()
    full_name = f"full_name_{random_lower_string()}"
    user_in = UserCreate(
        email=email,
        password=password,
        full_name=full_name,
        is_active=True)
    user = crud.user.create(obj_in=user_in)
    assert user.email == email
    assert hasattr(user, "hashed_password")
