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
    """
    Data Transfer Object (DTO) for creating a new topic.

    This class is used as a schema to define the structure and data types for creating a new topic. It includes fields for the topic's title, type, question, author, group ID, and closing date. Inherits from Pydantic's BaseModel for data validation and serialization.

    Attributes:
        title (str): The title of the topic.
        type (str): The type of the topic.
        question (str): The question or main content of the topic.
        author (str): The author's identifier for the topic.
        group_id (str): The identifier of the group associated with the topic.
        close_date (str): The closing date for the topic, typically indicating when the topic is no longer active or relevant.

    Config:
        orm_mode (bool): When set to True, allows the model to work with ORMs directly by parsing ORM objects to Pydantic models.
    """
    title: str
    type: str
    question: str
    author: str
    group_id: str
    close_date: str

    class Config:
        orm_mode = True
