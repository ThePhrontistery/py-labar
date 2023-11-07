from fastapi import APIRouter
# Include all routers here
from app.business.users.controllers import user

user_management_router = APIRouter()
user_management_router.include_router(user.router, tags=["Views User"])
