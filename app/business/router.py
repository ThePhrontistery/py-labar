from fastapi import APIRouter

# Include all routers here
from app.business.users.router import user_management_router

all_router = APIRouter()
all_router.include_router(user_management_router, tags=["User Management"])
