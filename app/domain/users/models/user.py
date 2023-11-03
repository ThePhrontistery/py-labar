from sqlmodel import Field
from app.common.base.base_entity import BaseUUIDModel


# DB ENTITY
class User(BaseUUIDModel, table=True):
    username: str = Field(nullable=False, unique=True, index=True)
    email: str = Field(nullable=False)
    password: str = Field(nullable=False)