from typing import Any, Dict, Optional, Union


from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

import uuid


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def create(self, *, obj_in: UserCreate) -> User:
        db_obj = User(
            uuid=str(uuid.uuid4().hex),
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            is_active=obj_in.is_active,
            is_superuser=obj_in.is_superuser,
        )
        db_obj.save()
        return db_obj


user = CRUDUser(User)
