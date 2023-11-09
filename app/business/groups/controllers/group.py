from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse
from app.domain.groups.repositories.group import GroupSQLRepository
from app.business.groups.services.group import GroupService

# Repositorio y servicio de grupos
group_repository = GroupSQLRepository()
group_service = GroupService(group_repository)

templates = Jinja2Templates(directory="templates")
router = APIRouter(prefix="/groups")


@router.get("/create", response_class=HTMLResponse)
async def create_group(request: Request):
    return templates.TemplateResponse("create_group.html", {"request": request})


@router.post("/create")
async def create_group(
        name: str = Form(...),
        users: str = Form(...),
):
    # Divide la cadena de usuarios separados por comas en una lista
    users_list = [user.strip() for user in users.split(",")]

    # Crea el grupo
    created_group = await group_service.create_group(name=name, users=users_list)

    # Puedes agregar una redirección o una respuesta de éxito aquí
    # return {"message": "Grupo creado exitosamente", "group_id": created_group.id}
    return RedirectResponse(url="/login", status_code=302)
