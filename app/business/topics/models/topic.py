#File: app/business/topics/models/topic.py

from datetime import date

from pydantic import BaseModel


class TopicDto(BaseModel):
    id: str
    title: str
    type: str
    question: str
    author: str
    group_id: str
    visits: int
    close_date: date

    class Config:
        orm_mode = True


class CreateTopicDto(BaseModel):
    title: str
    type: str
    question: str
    author: str
    group_id: str
    close_date: str

    class Config:
        orm_mode = True
