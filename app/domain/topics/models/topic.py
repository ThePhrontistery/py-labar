from sqlmodel import Field, Relationship
from app.common.base.base_entity import BaseUUIDModel
from app.domain.users.models import User


# DB ENTITY
class Topic(BaseUUIDModel, table=True):
    title: str = Field(nullable=False)
    type: str = Field(nullable=False)
    question: str = Field(nullable=False)
    author: str = Field(nullable=False)
    groupId: str = Field(nullable=True)
    status: str = Field(nullable=False)
    visits: int = Field(default=0)  # Valor predeterminado de visitas
    closeDate: str = Field(nullable=True)
    # Campo de relación que representa la lista de usuarios asignados al tema
    # assigned_users: list[User] = Relationship(back_populates="assigned_topics")
