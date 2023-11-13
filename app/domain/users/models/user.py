# File: app/domain/users/models/user.py

from sqlmodel import Field

from app.common.base.base_entity import BaseUUIDModel
# from app.domain.topics.models.topic import Topic


class User(BaseUUIDModel, table=True):
    """
    Campo de relación que representa los temas asignados al usuario
    assigned_topics: list[Topic] = Relationship(back_populates="assigned_users")
    """
    username: str = Field(nullable=False, index=True)
    email: str = Field(nullable=False, index=True)
    password: str = Field(nullable=False)
