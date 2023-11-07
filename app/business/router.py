from fastapi import APIRouter, Request
from starlette.responses import RedirectResponse

# Include all routers here
from app.business.users.router import user_management_router
from app.business.topics.router import topic_management_router

all_router = APIRouter()
all_router.include_router(user_management_router, tags=["User Management"])
all_router.include_router(topic_management_router, tags=["Topic Management"])


@all_router.get("/")
async def home_page_redirect(request: Request):
    return RedirectResponse("/users")
