from fastapi import Depends

from app.common.base.base_repository import BaseSQLRepository
from app.common.infra.sql_adaptors import get_async_session, AsyncSession
from app.domain.users.models import User
from app.business.users.models.user import CreateUserRequest

class UserSQLRepository(BaseSQLRepository[User]):

    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        super().__init__(User, session)

    async def create(self,*, create_req: CreateUserRequest) -> User:
        new_user = User(username=create_req.username, email=create_req.email, password=create_req.password)
        await self.add(model=new_user)
        return new_user

    # async def get_pending_todos(self) -> List[Todo]:
    #     todos = await self.session.exec(select(Todo).where(Todo.done == False))
    #     return todos.all()
    #
    # async def todo_done(self, todo_id: UUID) -> Todo:
    #     todo = await self.get(uid=todo_id)
    #     todo.done = True
    #     await self.save(model=todo, refresh=False)
    #     return todo