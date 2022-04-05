from mongoengine import (
    Document,
    StringField,
    BooleanField,
    UUIDField)


class User(Document):
    uuid = StringField(required=True)
    full_name = StringField(required=True)
    email = StringField(required=True)
    hashed_password = StringField(required=True)
    is_active = BooleanField(required=True)
    is_superuser = BooleanField(required=False, default=False)
