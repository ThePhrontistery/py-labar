from uuid import UUID

from fastapi import Depends

from app.common.base.base_repository import BaseSQLRepository
from app.common.infra.sql_adaptors import get_async_session, AsyncSession
from app.domain.topics.models import Topic


class TopicSQLRepository(BaseSQLRepository[Topic]):

    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        super().__init__(Topic, session)

    async def create(self, title: str, type: str, question: str, author: str, groupId: str, closeDate: str, status: str) -> Topic:
        new_topic = Topic(
            title=title,
            type=type,
            question=question,
            author=author,
            groupId=groupId,
            closeDate=closeDate,
            status=status
        )
        await self.add(model=new_topic)
        return new_topic

    async def edit(self, topic_id: UUID, title: str, type: str, question: str, author: str, groupId: str, closeDate: str, status: str) -> Topic:
        topic = await self.get(uid=topic_id)
        topic.title = title
        topic.type = type
        topic.question = question
        topic.author = author
        topic.groupId = groupId
        topic.closeDate = closeDate
        topic.status = status
        await self.save(model=topic, refresh=True)
        return topic

    async def remove(self, topic_id: UUID):
        topic = await self.get(uid=topic_id)
        await self.delete(model=topic)

