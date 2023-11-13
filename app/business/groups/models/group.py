#File: app/business/groups/models/group.py

from typing import List

from pydantic import BaseModel



class GroupDto(BaseModel):
    name: str
    users: str

    class Config:
        orm_mode = True
