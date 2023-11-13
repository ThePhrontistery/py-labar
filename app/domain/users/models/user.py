# File: app/domain/users/models/user.py

from sqlmodel import Field

from app.common.base.base_entity import BaseUUIDModel
# from app.domain.topics.models.topic import Topic


class User(BaseUUIDModel, table=True):
    username: str = Field(nullable=False, index=True)
    email: str = Field(nullable=False, index=True)
    password: str = Field(nullable=False)
