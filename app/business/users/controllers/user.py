import logging

from fastapi import APIRouter, FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from app.business.users.services.user import UserService
from app.business.users.models.user import CreateUserRequest
from app.business.topics.services.topic import TopicService
from datetime import datetime

templates = Jinja2Templates(directory="templates")
router = APIRouter()

logger = logging.getLogger(__name__)


class UserManager:
    def __init__(self):
        self.username = None


user_manager = UserManager()


def get_user_manager():
    return user_manager


@router.post("/home", response_class=HTMLResponse, name="login")
async def login(request: Request, username: str = Form(...), password: str = Form(...),
                user_service: UserService = Depends(UserService), topic_service: TopicService = Depends(TopicService)):
    if not await user_service.authenticate_user(username, password):
        error_message = "Usuario y/o contraseña incorrectos"
        return templates.TemplateResponse("index.html", {"request": request, "error": error_message})
    all_topics = await topic_service.get_all_topics()
    user_manager.username = username
    actual_date = datetime.now().date()
    isHomePage = True
    return templates.TemplateResponse("home.html",
                                      {"request": request, "username": username, "table_topics": all_topics,
                                       "actual_date": actual_date, "isHomePage": isHomePage})


@router.get("/register", name="register_user")
async def register_user(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/register")
async def register(request: Request, username: str = Form(...), email: str = Form(...), password: str = Form(...),
                   user_service: UserService = Depends(UserService)):
    exists_user = await user_service.exists_user(username)
    if not exists_user:
        create_user_request = CreateUserRequest(username=username, email=email, password=password)
        await user_service.create_user(create_user_request)
        return RedirectResponse(url="/", status_code=302)
    else:
        request.error = "El nombre de usuario ya existe"
        return templates.TemplateResponse("register.html", {"request": request})


@router.get("/home", response_class=HTMLResponse, name="return_home")
async def login(request: Request, topic_service: TopicService = Depends(TopicService)):
    all_topics = await topic_service.get_all_topics()
    isHomePage = True
    actual_date = datetime.now().date()
    return templates.TemplateResponse("home.html", {"request": request, "username": user_manager.username,
                                                    "table_topics": all_topics, "actual_date": actual_date,
                                                    "isHomePage": isHomePage})


@router.get("/", name="logout_user")
async def logout_user(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
