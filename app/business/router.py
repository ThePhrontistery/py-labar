from fastapi import APIRouter

# Include all routers here
from app.business.router import router

all_router = APIRouter()
all_router.include_router(router, tags=["Todo Management"])

