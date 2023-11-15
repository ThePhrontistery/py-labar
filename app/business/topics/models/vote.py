#File: app/business/topics/models/topic.py

from datetime import date

from pydantic import BaseModel

class CreateVoteDto(BaseModel):
    id_topic: str
    user: str
    value: str
    
    class Config:
        orm_mode = True
