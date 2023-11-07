from fastapi import APIRouter

# Include all routers here
from app.business.topics.controllers import topic

topic_management_router = APIRouter()
topic_management_router.include_router(topic.router, tags=["Views Topic"])