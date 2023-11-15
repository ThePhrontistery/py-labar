#File: app/business/topics/controllers/topic.py

from datetime import date, datetime
import logging

from fastapi import APIRouter, Request, Depends, Form, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates

from app.business.topics.models.topic import CreateTopicDto
from app.business.topics.models.vote import CreateVoteDto
from app.business.topics.services.topic import TopicService
from app.business.users.controllers.user import get_user_manager, router as user_router  
from app.business.groups.services.group import GroupService
from app.business.users.services.user import UserService

templates = Jinja2Templates(directory="templates")
router = APIRouter(prefix="/topics")

logger = logging.getLogger(__name__)

PATH_FOR_RETURN_HOME = user_router.url_path_for("return_home")


@router.get("/newtopic", response_class=HTMLResponse, name="new_topic")
async def new_topic(
    request: Request, 
    group_service: GroupService = Depends(GroupService)
    ):
    """
    Asynchronously renders the 'new_topic' page with a list of all groups.

    This endpoint is designed to display the 'new_topic.html' template. It fetches all group information using the provided GroupService and passes this data, along with the user information, to the template for rendering.

    Args:
        request (Request): The request object, which includes all the details of the HTTP request.
        group_service (GroupService): A service to handle group-related operations. It is injected as a dependency.

    Returns:
        TemplateResponse: The 'new_topic.html' template rendered with the necessary context, including the current user's username and all available groups.
    
    Note:
        This function assumes that a user manager is available to provide the current user's username.
    """
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
    """
    Asynchronously creates a new topic and redirects to the home page.

    This function handles the creation of a new topic based on the title, close date, and group provided through the form. It uses the TopicService to save the new topic. After creation, it redirects the user to the home page.

    Args:
        request (Request): The request object containing details of the HTTP request.
        title (str): The title of the topic to be created.
        close_date (str): The closing date for the topic.
        group (str): The group ID associated with the topic.
        topic_service (TopicService): The service used for topic-related operations, injected as a dependency.

    Returns:
        RedirectResponse: Redirects to the home URL with a status code of 302 after creating the topic.
    """
    autor_manager = get_user_manager()
    create_topic_request = CreateTopicDto(title=title, close_date=close_date, author=autor_manager.username, group_id=group, type="emoji", question=title)
    await topic_service.create_topic(create_topic_request)
    
    return RedirectResponse(url=home_url, status_code=302)


@router.post("/reopen", response_class=HTMLResponse, name="reopen_topic")
async def reopen_topic(
    request: Request,
    topic_id: str = Form(...),
    close_date: date = Form(...),
    topic_service: TopicService = Depends(TopicService)
    ):
    """
    Asynchronously reopens an existing topic and extends its close date.

    This endpoint is used to modify an existing topic, identified by its topic ID, and to extend or change its close date. It fetches the topic details, updates them, and saves the changes using the TopicService. After updating, it redirects to the home page.

    Args:
        request (Request): The request object with HTTP request details.
        topic_id (str): The unique identifier of the topic to be reopened.
        close_date (date): The new closing date for the topic.
        topic_service (TopicService): A service for handling operations related to topics, injected as a dependency.

    Returns:
        RedirectResponse: Redirects to the home URL with a status code of 302 after updating the topic.
    """
    topic = await topic_service.get_topic(topic_id)
    await topic_service.edit_topic(topic_id, topic.title, topic.type, topic.question, topic.author, topic.group_id, close_date)
    
    return RedirectResponse(url=PATH_FOR_RETURN_HOME, status_code=302)


@router.post("/close", response_class=HTMLResponse, name="close_topic")
async def close_topic(
    request: Request,
    topic_id: str = Form(...),
    topic_service: TopicService = Depends(TopicService)
    ):
    """
    Asynchronously closes a topic and redirects to the home page.

    This function handles the closing of a topic identified by its topic ID. It sets the topic's closing date to the current date and updates the topic details using the TopicService. After the update, it redirects the user to the home page.

    Args:
        request (Request): The request object containing details of the HTTP request.
        topic_id (str): The unique identifier of the topic to be closed.
        topic_service (TopicService): The service used for topic-related operations, injected as a dependency.

    Returns:
        RedirectResponse: Redirects to the home URL with a status code of 302 after closing the topic.

    Note:
        The closing date is set to the current date automatically.
    """
    actual_date = datetime.now().date()
    topic = await topic_service.get_topic(topic_id)
    await topic_service.edit_topic(topic_id, topic.title, topic.type, topic.question, topic.author, topic.group_id, actual_date)

    return RedirectResponse(url=PATH_FOR_RETURN_HOME, status_code=302)


@router.post("/delete_topic", response_class=HTMLResponse, name="delete_topic")
async def delete_topic(
    request: Request,
    topic_id: str = Form(...),
    topic_service: TopicService = Depends(TopicService)
    ):
    """
    Deletes a topic.

    Args:
        request (Request): The request object.
        topic_id (str): The ID of the topic to be deleted.
        topic_service (TopicService): Dependency injection of the TopicService.
        
    Returns:
        RedirectResponse: Redirects to the home page after deletion.
    """
    await topic_service.delete_topic(topic_id)

    return RedirectResponse(url=PATH_FOR_RETURN_HOME, status_code=302)

@router.get("/modal_votation", response_class=HTMLResponse, name="modal_votation")
async def modal_votation(request: Request, topic_id: str, topic_service: TopicService = Depends(TopicService)):
    user_manager = get_user_manager()
    topic = await topic_service.get_topic(topic_id)
    vote = await topic_service.get_vote(topic_id, user_manager.username)
    if vote is not None:

        return templates.TemplateResponse("error_vote_message.html", {"request": request})

    return templates.TemplateResponse("modal_votation.html", {"request": request, "username": user_manager.username, "topic": topic})

@router.post("/vote", name="create_vote")
async def create_vote(
    request: Request,
    id_topic: str = Form(...),
    vote: str = Form(...),
    user_service: UserService = Depends(UserService),
    topic_service: TopicService = Depends(TopicService)
):
    autor_manager = get_user_manager()
    autor = await user_service.get_user_by_username(autor_manager.username)
    create_vote_request = CreateVoteDto(id_topic=id_topic, user=autor.username, value=vote)
    await topic_service.create_vote(create_vote_request)

    return RedirectResponse(url=PATH_FOR_RETURN_HOME, status_code=302)