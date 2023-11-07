import logging

from fastapi import APIRouter, Request, Form, status, Depends
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from app.business.users.services.user import UserService
from app.business.users.models.user import CreateUserRequest

templates = Jinja2Templates(directory="templates")
router = APIRouter(prefix="/users")

logger = logging.getLogger(__name__)


@router.get("/")
async def home_page(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


@router.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...), user_service: UserService = Depends(UserService)):
    await user_service.authenticate_user(username, password)
    return RedirectResponse(url="/users/home", status_code=302)

@router.get("/home")
async def initial_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/register", name="register_user")
async def register_user(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register")
async def register(username: str = Form(...), email: str = Form(...), password: str = Form(...), user_service: UserService = Depends(UserService)):
    create_user_request = CreateUserRequest(username=username, email=email, password=password)
    await user_service.create_user(create_user_request)
    return RedirectResponse(url="/", status_code=302)
