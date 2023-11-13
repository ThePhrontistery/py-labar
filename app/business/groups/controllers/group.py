#File: app/business/groups/controllers/group.py

from fastapi import APIRouter, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse

from app.business.groups.models.group import GroupDto
from app.business.users.services.user import UserService
from app.domain.groups.repositories.group import GroupSQLRepository
from app.business.groups.services.group import GroupService
from app.business.users.controllers.user import get_user_manager, router as user_router  

# Repositorio y servicio de grupos
group_repository = GroupSQLRepository()

templates = Jinja2Templates(directory="templates")
router = APIRouter(prefix="/groups")


@router.get("/create", response_class=HTMLResponse)
async def create_group(request: Request, user_service: UserService = Depends(UserService)):
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
    return templates.TemplateResponse("create_group.html", {"request": request, "username": user_manager.username, "all_users": all_users})


@router.post("/create", name="create_group")
async def create_group(request: Request, name: str = Form(...),users: str = Form(...),group_service: GroupService = Depends(GroupService)):
    # Divide la cadena de usuarios separados por comas en una lista
    #users_list = [user.strip() for user in users.split(",")]

    # Crea el grupo
    create_group_request = GroupDto(name=name, users=users)
    await group_service.create_group(create_group_request)

    # Puedes agregar una redirección o una respuesta de éxito aquí
    # return {"message": "Grupo creado exitosamente", "group_id": created_group.id}
    #return RedirectResponse(url="/login", status_code=302)
    home_url = user_router.url_path_for("return_home")

    return RedirectResponse(url=home_url, status_code=302)

@router.post("/update_users")
def update_users(request: Request):
    print(request.url)
    # Lógica para manejar la actualización de usuarios
    # ...
    return {"message": "Usuarios actualizados"}