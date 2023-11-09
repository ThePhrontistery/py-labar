from pydantic import BaseModel
from typing import List


class GroupDto(BaseModel):
    id: str
    name: str
    users: List[str]

    class Config:
        orm_mode = True
