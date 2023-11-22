# File: app/business/groups/controllers/group.py

from fastapi import APIRouter, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse

from app.business.groups.models.group import GroupDto
from app.business.users.services.user import UserService
from app.domain.groups.repositories.group import GroupSQLRepository
from app.business.groups.services.group import GroupService
from app.business.users.controllers.user import get_user_manager, router as user_router

group_repository = GroupSQLRepository()

templates = Jinja2Templates(directory="templates")
router = APIRouter(prefix="/groups")

PATH_FOR_RETURN_HOME = user_router.url_path_for("return_home")


@router.get("/create", response_class=HTMLResponse)
async def create_group(
        request: Request,
        user_service: UserService = Depends(UserService)
):
    """
    Asynchronously handles a GET request to create a new group, rendering a template with all available users.

    This endpoint is mapped to respond to the '/create' path with an HTML response. It uses an instance of `UserService` to fetch all users and includes them in the rendered HTML template for group creation.

    Parameters:
    - request (Request): The request object containing request-specific information.
    - user_service (UserService, optional): The user service dependency, which is responsible for user-related operations. Defaults to an instance provided by the `Depends` function.

    Returns:
    - TemplateResponse: An instance of `TemplateResponse` that renders the 'create_group.html' template. The template is provided with the current request, the username of the user initiating the request (obtained from `user_manager`), and a list of all users (fetched using `user_service`).
    """
    user_manager = get_user_manager()
    all_users = await user_service.get_all_users()
    return templates.TemplateResponse("create_group.html",
                                      {"request": request, "username": user_manager.username, "all_users": all_users})


@router.post("/create", name="create_group")
async def create_group(
        name: str = Form(...),
        users: str = Form(...),
        group_service: GroupService = Depends(GroupService)
):
    """
    Handle the creation of a new group.

    This asynchronous endpoint handles the creation of a new group with the specified name and users. The users are expected to be provided in a comma-separated string format. The function creates a new group using the provided GroupService and redirects to the home URL upon successful creation.

    Args:
        name (str): The name of the group to be created. Obtained from form data.
        users (str): A comma-separated string of user identifiers. Obtained from form data.
        group_service (GroupService): The service used for group-related operations, injected as a dependency.

    Returns:
        RedirectResponse: Redirects to the home URL upon successful group creation, with a status code of 302.

    Note:
        The function does not directly handle the splitting and parsing of the 'users' string into a list. This should be handled before calling this endpoint or within the GroupService implementation.
    """
    # Divide la cadena de usuarios separados por comas en una lista
    # users_list = [user.strip() for user in users.split(",")]
    create_group_request = GroupDto(name=name, users=users)
    await group_service.create_group(create_group_request)

    return RedirectResponse(url=PATH_FOR_RETURN_HOME, status_code=302)


@router.post("/update_users")
def update_users(
        request: Request
):
    """
    Handle the request to update users.

    This endpoint logs the request URL and returns a confirmation message indicating that the users have been updated. The actual user update logic is not implemented within this function, and should be handled separately.

    Args:
        request (Request): The request object containing details of the incoming HTTP request.

    Returns:
        dict: A dictionary with a message indicating the completion of the user update process.

    Note:
        This function is a stub and does not perform any actual user update operations. It should be further implemented to handle the user update logic.
    """
    print(request.url)
    # Lógica para manejar la actualización de usuarios
    # ...
    return {"message": "Usuarios actualizados"}
