#File: app/business/router.py

from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

from app.business.users.controllers import user
from app.business.groups.controllers import group
from app.business.topics.controllers import topic


all_router = APIRouter()
all_router.include_router(user.router, tags=["User Views"])
all_router.include_router(group.router, tags=["Group Views"])
all_router.include_router(topic.router, tags=["Topic Views"])

templates = Jinja2Templates(directory="templates")


@all_router.get("/", name="index", tag=["Index"])
async def index_page(
    request: Request
    ):
    """
    Asynchronously renders the index page.

    This endpoint is responsible for displaying the main index page of the application. It uses the 'index.html' template to render the page, providing the necessary context for any dynamic content.

    Args:
        request (Request): The request object containing details of the HTTP request.

    Returns:
        TemplateResponse: Renders the 'index.html' template for the index page.
    """
    return templates.TemplateResponse('index.html', {"request": request})

