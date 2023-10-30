from typing import Annotated
from fastapi import Depends, FastAPI, Form, HTTPException, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import FastAPI
from .database import Base, engine, User
from sqlalchemy.orm import Session
from app.domain.schemas.user import UserCreate, User

from app.business.controllers import user_controller
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configura Jinja2 para cargar plantillas desde el directorio 'templates'
templates = Jinja2Templates(directory="templates")

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine) 

# Ruta principal para renderizar la plantilla HTML
@app.get("/", response_class=HTMLResponse)

async def read_root(request: Request):
    """
    Read_root function in main.py is fetching user_data and user_id using the controllers\\user_controller.py
    This function is also passing the user_data and user_id to the index.html template.
    """
    user_data = user_controller.get_users_mock() 
    user_id = user_controller.get_user_by_id(1)
    return templates.TemplateResponse("login.html", {"request": request, "user_data": user_data, "user_id": user_id})


@app.post("/create_user/", response_model=dict)
def create_user_route(user: UserCreate):
    return user_controller.create_user(user)


@app.get("/users/", response_model=list[User])
def get_users():
    users = user_controller.get_users()
    return users

@app.get("/users/{name}", response_model=User)
def get_user_by_name(name: str):
    for user in get_users():
        if user.username == name:
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


# Definición de la ruta en FastAPI
@app.post('/login')
async def login(request: Request, user_code: str = Form(...), password: str = Form(...)):
    error = None

    user = get_user_by_name(user_code)

    if user is None:
        error = 'Invalid user or password'
        return templates.TemplateResponse("login.html", {"request": request, "error": error})

    # Tu lógica de autenticación es correcta, establece la sesión
    # Reemplaza esto con tu propia lógica de autenticación
    session = request.session
    session['CURRENT_USER'] = user_code

    # Redirecciona al usuario a otra página después de la autenticación (por ejemplo, 'index')
    return RedirectResponse(url="/index", status_code=status.HTTP_303_SEE_OTHER)
