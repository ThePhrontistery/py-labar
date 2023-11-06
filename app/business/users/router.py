from fastapi import APIRouter
# Include all routers here
from app.business.users.controllers import user_api
from app.business.users.controllers import user_views

user_management_router = APIRouter()
user_management_router.include_router(user_api.router, tags=["API User"])
user_management_router.include_router(user_views.router, tags=["Views User"])