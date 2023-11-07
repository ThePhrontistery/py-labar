from sqlmodel import Field

from app.common.base.base_entity import BaseUUIDModel


# DB ENTITY
class Topic(BaseUUIDModel, table=True):
    title: str = Field(nullable=False)
    type: str = Field(nullable=False)
    question: str = Field(nullable=False)
    author: str = Field(nullable=False)
    group_id: str = Field(nullable=True)
    visits: int = Field(default=0)  # Valor predeterminado de visitas
    close_date: str = Field(nullable=True)
    # Campo de relación que representa la lista de usuarios asignados al tema
    # assigned_users: list[User] = Relationship(back_populates="assigned_topics")
