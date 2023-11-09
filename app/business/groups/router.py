from fastapi import APIRouter

# Include all routers here
from app.business.groups.controllers import group

group_management_router = APIRouter()
group_management_router.include_router(group.router, tags=["Views Group"])