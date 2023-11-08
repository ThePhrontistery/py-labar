from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

from app.business.groups.router import group_management_router
from app.business.topics.router import topic_management_router
# Include all routers here
from app.business.users.router import user_management_router

all_router = APIRouter()
all_router.include_router(user_management_router, tags=["User Management"])
all_router.include_router(topic_management_router, tags=["Topic Management"])
all_router.include_router(group_management_router, tags=["Group Management"])

templates = Jinja2Templates(directory="templates")


# @all_router.get("/")
# async def home_page_redirect(request: Request):
#     return RedirectResponse("/users")

@all_router.get("/")
async def index_page(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


