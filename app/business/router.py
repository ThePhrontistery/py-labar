from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

# Include all routers here
from app.business.users.controllers import user
from app.business.groups.controllers import group
from app.business.topics.controllers import topic


all_router = APIRouter()
all_router.include_router(user.router, tags=["User Views"])
all_router.include_router(group.router, tags=["Group Views"])
all_router.include_router(topic.router, tags=["Topic Views"])

templates = Jinja2Templates(directory="templates")


@all_router.get("/", name="index")
async def index_page(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})

