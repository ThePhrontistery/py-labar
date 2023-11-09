from pydantic import BaseModel
from typing import List


class GroupDto(BaseModel):
    name: str
    users: str

    class Config:
        orm_mode = True
