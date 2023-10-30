from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str

class User(UserCreate):
    id: int

    class Config:
        orm_mode = True