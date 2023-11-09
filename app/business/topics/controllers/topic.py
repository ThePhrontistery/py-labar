import logging

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
# from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

# from app.business.topics.services.topic import TopicService

templates = Jinja2Templates(directory="templates")
router = APIRouter(prefix="/topics")

logger = logging.getLogger(__name__)

@router.get("/newtopic", response_class=HTMLResponse, name="new_topic")
async def create_topic(request: Request):
    return templates.TemplateResponse("new_topic.html", {"request": request})

@router.post("/create", response_class=HTMLResponse)
async def create_topic(
    request: Request,
    title: str = Form(...),
    close_date: str = Form(...),
):
    try:
        # Replace the following with your actual logic to create a topic
        # For instance, you may have a service method like this:
        # TopicService.create(TopicCreate(title=title, close_date=close_date, emoji=emoji))
        new_topic_data = TopicCreate(title=title, close_date=close_date, emoji=emoji)
        new_topic = TopicService.create(new_topic_data)  # This should be an async call if your service is async

        # Redirect to the topic list page after creation, or return a success message
        # return RedirectResponse(url='/topics/list', status_code=HTTP_201_CREATED)
        return JSONResponse(
            status_code=HTTP_201_CREATED,
            content={"message": "Topic created successfully", "id": new_topic.id}
        )
    except Exception as e:
        logger.exception("Failed to create a new topic", exc_info=e)
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))