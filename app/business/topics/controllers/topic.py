from datetime import date, datetime
import logging

from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
# from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from app.business.topics.models.topic import CreateTopicDto
from app.business.topics.services.topic import TopicService

from app.business.users.controllers.user import get_user_manager, router as user_router  
# from app.business.topics.services.topic import TopicService
from app.business.groups.services.group import GroupService

templates = Jinja2Templates(directory="templates")
router = APIRouter(prefix="/topics")

logger = logging.getLogger(__name__)

@router.get("/newtopic", response_class=HTMLResponse, name="new_topic")
async def new_topic(request: Request, group_service: GroupService = Depends(GroupService)):
    user_manager = get_user_manager()
    all_groups = await group_service.get_all_groups()
    return templates.TemplateResponse("new_topic.html", {"request": request, "username": user_manager.username, "all_groups": all_groups})

@router.post("/create", response_class=HTMLResponse, name="create_topic")
async def create_topic(
    request: Request,
    title: str = Form(...),
    close_date: str = Form(...),
    group: str = Form(...),
    topic_service: TopicService = Depends(TopicService)
):
    autor_manager = get_user_manager()
    create_topic_request = CreateTopicDto(title=title, close_date=close_date, author=autor_manager.username, group_id=group, type="emoji", question=title)
    await topic_service.create_topic(create_topic_request)
    
    
    home_url = user_router.url_path_for("return_home")

    return RedirectResponse(url=home_url, status_code=302)

@router.post("/reopen", response_class=HTMLResponse, name="reopen_topic")
async def reopen_topic(
    request: Request,
    topic_id: str = Form(...),
    close_date: date = Form(...),
    topic_service: TopicService = Depends(TopicService)
):
    
    topic = await topic_service.get_topic(topic_id)
    await topic_service.edit_topic(topic_id, topic.title, topic.type, topic.question, topic.author, topic.group_id, close_date)
    
    
    home_url = user_router.url_path_for("return_home")

    return RedirectResponse(url=home_url, status_code=302)

@router.post("/close", response_class=HTMLResponse, name="close_topic")
async def close_topic(
    request: Request,
    topic_id: str = Form(...),
    topic_service: TopicService = Depends(TopicService)
):
    
    actual_date = datetime.now().date()
    topic = await topic_service.get_topic(topic_id)
    await topic_service.edit_topic(topic_id, topic.title, topic.type, topic.question, topic.author, topic.group_id, actual_date)
    
    
    home_url = user_router.url_path_for("return_home")

    return RedirectResponse(url=home_url, status_code=302)