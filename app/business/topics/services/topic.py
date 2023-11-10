from app.business.topics.models.topic import TopicDto, CreateTopicDto
from app.domain.topics.models import Topic
from app.domain.topics.repositories.topic import TopicSQLRepository
from fastapi import Depends
from datetime import datetime

date_format = "%Y-%m-%d %H:%M:%S"


def parse_to_dto(topic_entity: Topic):
    return TopicDto(**topic_entity.dict())


class TopicService:

    def __init__(self, repository: TopicSQLRepository = Depends(TopicSQLRepository)):
        self.topic_repo = repository

    async def create_topic(self,  create_req: CreateTopicDto) -> Topic:
        raw_new_topic = await self.topic_repo.create(create_req = create_req)
        return raw_new_topic

    async def delete_topic(self, topic_id: str):
        raw_topic = await self.topic_repo.get(uid=topic_id)
        await self.topic_repo.delete(model=raw_topic)

    async def edit_topic(self, topic_id: str, title: str, type: str, question: str, author: str, group_id: str,
                         close_date: str) -> TopicDto:
        raw_topic = await self.topic_repo.get(uid=topic_id)
        raw_topic.title = title
        raw_topic.type = type
        raw_topic.question = question
        raw_topic.author = author
        raw_topic.group_id = group_id
        raw_topic.close_date = close_date
        await self.topic_repo.save(model=raw_topic)
        return parse_to_dto(raw_topic)

    async def get_topic(self, topic_id: str) -> TopicDto:
        raw_topic = await self.topic_repo.get(uid=topic_id)
        return parse_to_dto(raw_topic)

    async def get_all_topics(self):
        return await self.topic_repo.get_all_topics()