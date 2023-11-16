#File: app/business/topics/services/topic.py

from datetime import datetime
from typing import List

from fastapi import Depends

from app.business.topics.models.vote import CreateVoteDto
from app.domain.topics.models.vote import Vote
from app.domain.topics.repositories.vote import VoteSQLRepository


class VoteService:

    def __init__(self, repository: VoteSQLRepository = Depends(VoteSQLRepository)):
        self.vote_repo = repository
    
    async def create_vote(self,  create_req: CreateVoteDto) -> Vote:
        raw_new_topic = await self.vote_repo.createVote(create_req = create_req)
        return raw_new_topic
    
    async def get_vote(self,  id_topic: str, username: str) -> Vote:
        raw_new_topic = await self.vote_repo.get_by_user_and_topic(username, id_topic)
        return raw_new_topic
    
    async def get_votes_by_topic(self,  id_topic: str) -> Vote:
        return await self.vote_repo.get_by_topic(id_topic)
    
    async def group_by_value(self, votes: List[Vote]):
        grouped_votes = {}

        for vote in votes:
            value = vote.value
            if value in grouped_votes:
                grouped_votes[value] = grouped_votes[value] + 1
            else:
                grouped_votes[value] = 1
        
        for i in range(1, 6):
            if str(i) not in grouped_votes:
                grouped_votes[str(i)] = 0

        return grouped_votes
