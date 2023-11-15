# File: app/domain/topics/models/vote.py

from sqlmodel import Field

from app.common.base.base_entity import BaseUUIDModel

class Vote(BaseUUIDModel, table=True):
    id_topic: str = Field(nullable=False)
    user: str = Field(nullable=False)
    value: str = Field(nullable=False)
