# File: app/business/users/models/user.py

from pydantic import BaseModel, Field


class CreateUserRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(...)
    password: str = Field(..., min_length=6)
