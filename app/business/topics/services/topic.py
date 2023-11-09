from app.business.topics.models.topic import TopicDto
from app.common.services.sse import EventPublisher
from app.domain.topics.models import Topic
from app.domain.topics.repositories.topic import TopicSQLRepository
from fastapi import Depends
from datetime import datetime

date_format = "%Y-%m-%d %H:%M:%S"


def parse_to_dto(topic_entity: Topic):
    return TopicDto(**topic_entity.dict())


class TopicService:
    _topic_event_publisher = EventPublisher()

    def __init__(self, repository: TopicSQLRepository = Depends(TopicSQLRepository)):
        self.topic_repo = repository

    async def create_topic(self, title: str, type: str, question: str, author: str, group_id: str) -> TopicDto:
        raw_new_topic = await self.topic_repo.create(
            title=title,
            type=type,
            question=question,
            author=author,
            group_id=group_id
        )
        topic_dto = parse_to_dto(raw_new_topic)
        return topic_dto

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
        all_topics = await self.topic_repo.get_all_topics()
        for topic in all_topics:
            if topic.close_date:
                date_parts = topic.close_date.split(" ")[0].split("-")
                topic.close_date = datetime(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))
                topic.close_date = topic.close_date.strftime("%d-%m-%Y")
            else:
                topic.close_date = ""
        return await self.topic_repo.get_all_topics()