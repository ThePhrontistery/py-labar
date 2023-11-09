from app.business.groups.models.group import GroupDto
from app.domain.groups.models import Group
from app.domain.groups.repositories.group import GroupSQLRepository
from fastapi import Depends


def parse_to_dto(group_entity: Group):
    return GroupDto(**group_entity.dict())


class GroupService:

    def __init__(self, repository: GroupSQLRepository = Depends(GroupSQLRepository)):
        self.group_repo = repository

    async def create_group(self,  create_req: GroupDto) -> Group:
        raw_new_group = await self.group_repo.create(create_req = create_req)
        return raw_new_group

    async def delete_group(self, group_id: str):
        raw_group = await self.group_repo.get(uid=group_id)
        await self.group_repo.delete(model=raw_group)

    async def edit_group(self, group_id: str, name: str, users: list[str]) -> GroupDto:
        raw_group = await self.group_repo.get(uid=group_id)
        raw_group.name = name
        raw_group.users = users
        await self.group_repo.save(model=raw_group)
        return parse_to_dto(raw_group)

    async def get_group(self, group_id: str) -> GroupDto:
        raw_group = await self.group_repo.get(uid=group_id)
        return parse_to_dto(raw_group)
    
    async def get_all_groups(self):
       return await self.group_repo.get_all_groups()