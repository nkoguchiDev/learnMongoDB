from mongoengine import connect

from app.core.config import settings

connect(db=settings.DB_NAME,
        username=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        authentication_mechanism='SCRAM-SHA-1',
        authentication_source='admin'
        )
