# File: app/domain/groups/models/group.py

from sqlmodel import Field

from app.common.base.base_entity import BaseUUIDModel


class Group(BaseUUIDModel, table=True):
    name: str = Field(nullable=False)
    users: str = Field(default=[])
