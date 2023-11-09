from uuid import UUID
from fastapi import Depends
from app.common.base.base_repository import BaseSQLRepository
from app.common.infra.sql_adaptors import get_async_session, AsyncSession
from app.domain.groups.models import Group


class GroupSQLRepository(BaseSQLRepository[Group]):

    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        super().__init__(Group, session)

    async def create(self, name: str, users: list[str]) -> Group:
        new_group = Group(
            name=name,
            users=users
        )
        await self.add(model=new_group)
        return new_group

    async def edit(self, group_id: UUID, name: str, users: list[str]) -> Group:
        group = await self.get(uid=group_id)
        group.name = name
        group.users = users
        await self.save(model=group, refresh=True)
        return group

    async def remove(self, group_id: UUID):
        group = await self.get(uid=group_id)
        await self.delete(model=group)
