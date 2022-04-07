from typing import Any, Dict, Optional, Union


from app.core.security import get_password_hash, verify_password
from app.core.generator import generate_uuid
from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, *, email: str) -> Optional[User]:
        return self.model.objects.filter(email=email).first()

    def create(self, *, obj_in: UserCreate) -> User:
        db_obj = User(
            uuid=generate_uuid(),
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            is_active=obj_in.is_active,
            is_superuser=obj_in.is_superuser
        )
        db_obj.save()
        return db_obj

    def update(self,
               uuid: str,
               db_obj: User,
               obj_in: Union[UserUpdate, Dict[str, Any]]) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(uuid=uuid, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, *,
                     email: str,
                     password: str) -> Optional[User]:
        user = self.get_by_email(email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


user = CRUDUser(User)
