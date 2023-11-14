#File: app/business/users/controllers/user.py

from datetime import datetime
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


class UserManager:
    def __init__(self):
        self.username = None


user_manager = UserManager()


def get_user_manager():
    return user_manager


@router.post("/home", response_class=HTMLResponse, name="login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    user_service: UserService = Depends(UserService),
    topic_service: TopicService = Depends(TopicService)
    ):
    """
    Asynchronously handles user login and redirects to the home page or displays an error.

    This function attempts to authenticate a user using the provided username and password. If authentication fails, it returns the index page with an error message. On successful authentication, it retrieves all topics using the TopicService, updates the user manager with the username, and then renders the 'home.html' template with the necessary data.

    Args:
        request (Request): The request object containing details of the HTTP request.
        username (str): The username provided by the user.
        password (str): The password provided by the user.
        user_service (UserService): A service for user-related operations, injected as a dependency.
        topic_service (TopicService): A service for handling topic-related operations, injected as a dependency.

    Returns:
        TemplateResponse: Renders the 'home.html' template with topics and current date if authentication is successful, otherwise returns the 'index.html' template with an error message.

    Note:
        The actual authentication logic is handled by the UserService.
    """
    if not await user_service.authenticate_user(username, password):
        error_message = "Usuario y/o contraseña incorrectos"
        return templates.TemplateResponse("index.html", {"request": request, "error": error_message})
    all_topics = await topic_service.get_all_topics()
    user_manager.username = username
    actual_date = datetime.now().date()
    return templates.TemplateResponse("home.html", {"request": request, "username": username, "table_topics": all_topics, "actual_date": actual_date})


@router.get("/register", name="register_user")
async def register_user(
    request: Request
    ):
    """
    Asynchronously renders the user registration page.

    This endpoint displays the 'register.html' template, allowing a user to fill out the registration form. It's a simple view function that returns the registration page without any additional context or processing.

    Args:
        request (Request): The request object containing details of the HTTP request.

    Returns:
        TemplateResponse: Renders the 'register.html' template, allowing the user to register.
    """
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/register")
async def register(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    user_service: UserService = Depends(UserService)
    ):
    """
    Asynchronously handles the user registration process.

    This function processes the user registration form data. It checks if the provided username already exists. If it doesn't, the function creates a new user using the provided username, email, and password, and then redirects to the home page. If the username exists, it returns the registration page with an error message.

    Args:
        request (Request): The request object containing details of the HTTP request.
        username (str): The desired username of the new user.
        email (str): The email address of the new user.
        password (str): The chosen password for the new account.
        user_service (UserService): The service for user-related operations, injected as a dependency.

    Returns:
        RedirectResponse or TemplateResponse: Redirects to the home page on successful registration, or returns the 'register.html' template with an error message if the username exists.

    Note:
        User creation is managed by the UserService.
    """
    exists_user = await user_service.exists_user(username)
    if not exists_user:
        create_user_request = CreateUserRequest(username=username, email=email, password=password)
        await user_service.create_user(create_user_request)
        return RedirectResponse(url="/", status_code=302)
    else:
        request.error = "El nombre de usuario ya existe"
        return templates.TemplateResponse("register.html", {"request": request})


@router.get("/home", response_class=HTMLResponse, name="return_home")
async def login(
    request: Request,
    topic_service: TopicService = Depends(TopicService)
    ):
    """
    Asynchronously displays the home page with a list of all topics.

    This function fetches all topics using the TopicService and displays them on the home page. It also includes the current date and the username of the user currently logged in. The 'home.html' template is used to render the page.

    Args:
        request (Request): The request object containing details of the HTTP request.
        topic_service (TopicService): A service for handling topic-related operations, injected as a dependency.

    Returns:
        TemplateResponse: Renders the 'home.html' template with a list of all topics, the current date, and the username of the logged-in user.
    """
    all_topics = await topic_service.get_all_topics()
    actual_date = datetime.now().date()
    return templates.TemplateResponse("home.html", {"request": request, "username": user_manager.username,
                                                    "table_topics": all_topics, "actual_date": actual_date})


@router.get("/", name="logout_user")
async def logout_user(
    request: Request
    ):
    """
    Asynchronously renders the logout or index page.

    This function handles the user logout process by simply rendering the 'index.html' template. It signifies the user has been logged out and is now viewing the index page. This function does not perform any session termination or user-specific action beyond displaying the index page.

    Args:
        request (Request): The request object containing details of the HTTP request.

    Returns:
        TemplateResponse: Renders the 'index.html' template, representing the logout or index page.
    """
    return templates.TemplateResponse("index.html", {"request": request})
