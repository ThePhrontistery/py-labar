# File: app/domain/users/repositories/user.py

from typing import Optional

from fastapi import Depends

from app.common.base.base_repository import BaseSQLRepository
from app.common.infra.sql_adaptors import get_async_session, AsyncSession
from app.domain.users.models import User
from app.business.users.models.user import CreateUserRequest


class UserSQLRepository(BaseSQLRepository[User]):

    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        super().__init__(User, session)

    async def create(self, *, create_req: CreateUserRequest) -> User:
        new_user = User(username=create_req.username, email=create_req.email, password=create_req.password)
        await self.add(model=new_user)
        return new_user

    async def get_by_username(self, username: str) -> Optional[User]:
        return await self.get_one_by("username", username)

    async def get_all_users(self):
        return await self.get_all()
