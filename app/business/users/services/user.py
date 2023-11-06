from app.business.users.models.user import CreateUserRequest
from app.domain.users.models.user import User
from app.domain.users.repositories.user import UserSQLRepository
from fastapi import Depends

from app.common.services.sse import EventPublisher


# def parse_to_dto(todo_entity: Todo):
#     return TodoDto(**todo_entity.dict())


class UserService:

    def __init__(self, repository: UserSQLRepository = Depends(UserSQLRepository)):
        self.user_repository = repository

    async def create_user(self, create_req: CreateUserRequest) -> User:
        raw_new_user = await self.user_repository.create()
        # TODO ASR hacer mapeo de User (Database) a User (Dto)
        # todo_dto = parse_to_dto(raw_new_todo)
        return raw_new_user