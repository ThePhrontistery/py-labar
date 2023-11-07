from sqlmodel import Field, Relationship
from app.common.base.base_entity import BaseUUIDModel
from app.domain.topics.models.topic import Topic


# DB ENTITY
class User(BaseUUIDModel, table=True):
    username: str = Field(nullable=False, index=True)
    email: str = Field(nullable=False, index=True)
    password: str = Field(nullable=False)
    # Campo de relación que representa los temas asignados al usuario
    # assigned_topics: list[Topic] = Relationship(back_populates="assigned_users")