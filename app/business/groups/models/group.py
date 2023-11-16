# File: app/business/groups/models/group.py

from typing import List

from pydantic import BaseModel


class GroupDto(BaseModel):
    """
    Data transfer object (DTO) for representing a group.

    This class is used to define the structure of a group data object, including its name and a string representing its users. It extends BaseModel from Pydantic, which provides validation and parsing for the class attributes.

    Attributes:
        name (str): The name of the group.
        users (str): A string representation of the users associated with the group.

    Config:
        orm_mode (bool): Enables ORM mode. When set to True, the model can be returned directly from ORM queries.
    """
    name: str
    users: str

    class Config:
        orm_mode = True
