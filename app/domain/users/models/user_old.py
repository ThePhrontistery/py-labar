# File: app/domain/schemas/user.py

from pydantic import BaseModel, EmailStr, Field, UUID4
from typing import Optional

# Schema for user creation.
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=6)

# Schema for user login.
class UserLogin(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)

# Schema for the response that will be sent back to the client.
# This includes the user id and any other fields that you might want to return.
class UserResponse(BaseModel):
    id: UUID4
    username: str
    email: EmailStr

    class Config:
        orm_mode = True  # Allows the output of SQLAlchemy models to be converted to this Pydantic model

# Schema representing the stored user data, including the hashed password.
# This should never be returned to the client.
class UserInDB(BaseModel):
    id: UUID4
    username: str
    email: EmailStr
    hashed_password: str

    class Config:
        orm_mode = True
