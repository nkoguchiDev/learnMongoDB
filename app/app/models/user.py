from mongoengine import (
    Document,
    EmbeddedDocument,
    StringField,
    IntField,
    DateTimeField,
    ListField,
    EmbeddedDocumentField,
    BooleanField)

name = StringField(required=True)
age = IntField(required=False)


class User(Base):
    id = StringField(required=True)
    full_name = StringField(required=True)
    email = StringField(required=True)
    hashed_password = StringField(required=True)
    is_active = BooleanField(required=True)
    is_superuser = BooleanField(required=True)
    # items = relationship("Item", back_populates="owner")
