#File: app/domain/topics/repositories/topic.py
from typing import Optional
from uuid import UUID

from fastapi import Depends
from sqlmodel import select
from sqlalchemy.orm import selectinload
from app.business.topics.models.topic import CreateVoteDto

from app.common.base.base_repository import BaseSQLRepository
from app.common.infra.sql_adaptors import get_async_session, AsyncSession
from app.domain.topics.models import Topic
from app.domain.topics.models.topic import Vote


class VoteSQLRepository(BaseSQLRepository[Vote]):

    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        super().__init__(Topic, session)
    
    async def createVote(self, create_req: CreateVoteDto) -> Vote:
        new_topic = Vote(id_topic=create_req.id_topic,
                          user=create_req.user,
                          value=create_req.value)
        await self.add(model=new_topic)
        return new_topic

    async def get_by_user_and_topic(self, user: str, id_topic: str) -> Optional[Vote]:
        result = await self.session.exec(
            select(Vote)
            .where((Vote.user == user) & (Vote.id_topic == id_topic))
            .options(selectinload('*'))
        )
        return result.one_or_none()
    
    async def get_by_topic(self, id_topic: str):
        result = await self.session.exec(
            select(Vote)
            .where((Vote.id_topic == id_topic))
            .options(selectinload('*'))
        )
        return result.all()

