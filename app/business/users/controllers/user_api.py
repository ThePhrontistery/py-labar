import logging

from fastapi import APIRouter
from fastapi import Depends, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.business.users.models.user import CreateUserRequest
from app.business.users.services.user import UserService

# TODO ASR
router = APIRouter()

logger = logging.getLogger(__name__)


# @router.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     # Assuming you have a function to get user data in usercontroller
#     # This is just a placeholder
#     user_data = "Sample user data"
#     user_id = 1
#     return templates.TemplateResponse("index.html", {"request": request, "user_data": user_data, "user_id": user_id})


# @router.post("/login")
# async def login(request: Request, username: str = Form(...), password: str = Form(...),
#                 user_service=Depends(UserService)):
#     # TODO ASR
#     return None


