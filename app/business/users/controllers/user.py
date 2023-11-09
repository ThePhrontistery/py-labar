import logging

from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from app.business.users.services.user import UserService
from app.business.users.models.user import CreateUserRequest
from app.business.topics.services.topic import TopicService

templates = Jinja2Templates(directory="templates")
router = APIRouter()

logger = logging.getLogger(__name__)


# @router.get("/")
# async def home_page(request: Request):
#     return templates.TemplateResponse('index.html', {"request": request})


@router.post("/login", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...), user_service: UserService = Depends(UserService), topic_service: TopicService = Depends(TopicService)):
    if not await user_service.authenticate_user(username, password):
        error_message = "Usuario y/o contraseña incorrectos"
        return templates.TemplateResponse("index.html", {"request": request, "error": error_message})
    all_topics = await topic_service.get_all_topics()

    return templates.TemplateResponse("home.html", {"request": request, "username": username, "table_topics": all_topics})

@router.get("/register", name="register_user")
async def register_user(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register")
async def register(username: str = Form(...), email: str = Form(...), password: str = Form(...), user_service: UserService = Depends(UserService)):
    create_user_request = CreateUserRequest(username=username, email=email, password=password)
    await user_service.create_user(create_user_request)
    return RedirectResponse(url="/", status_code=302)

@router.get("/", name="logout_user")
async def logout_user(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
