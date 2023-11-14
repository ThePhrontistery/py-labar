# File: app/domain/topics/models/topic.py

from datetime import date

from sqlmodel import Field

from app.common.base.base_entity import BaseUUIDModel


class Topic(BaseUUIDModel, table=True):
    title: str = Field(nullable=False)
    type: str = Field(nullable=False)
    question: str = Field(nullable=False)
    author: str = Field(nullable=False)
    group_id: str = Field(nullable=True)
    visits: int = Field(default=0)
    close_date: date = Field(nullable=True)

class Vote(BaseUUIDModel, table=True):
    id_topic: str = Field(nullable=False)
    user: str = Field(nullable=False)
    value: str = Field(nullable=False)
