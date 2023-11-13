# File: app/business/users/services/user.py

from typing import Optional

from fastapi import Depends

from app.business.users.models.user import CreateUserRequest
from app.domain.users.models.user import User
from app.domain.users.repositories.user import UserSQLRepository


class UserService:

    def __init__(self, repository: UserSQLRepository = Depends(UserSQLRepository)):
        self.user_repository = repository

    async def create_user(self, create_req: CreateUserRequest) -> User:
        raw_new_user = await self.user_repository.create(create_req=create_req)
        return raw_new_user

    async def authenticate_user(self, username: str, password: str) -> Optional[User]:
        user = await self.user_repository.get_by_username(username)
        if user and user.password == password:
            return user
        return None

    async def get_all_users(self):
        return await self.user_repository.get_all_users()

    async def exists_user(self, username: str) -> bool:
        user_by_username = await self.user_repository.get_by_username(username)
        if user_by_username is not None:
            return True
        else:
            return False
