from typing import Annotated
from fastapi import Depends, FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from .database import Base, engine
from sqlalchemy.orm import Session
from app.domain.schemas.user import UserCreate, User

from app.business.controllers import user_controller

app = FastAPI()

# Configura Jinja2 para cargar plantillas desde el directorio 'templates'
templates = Jinja2Templates(directory="app/templates")

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
    return templates.TemplateResponse("index.html", {"request": request, "user_data": user_data, "user_id": user_id})


@app.post("/create_user/", response_model=dict)
def create_user_route(user: UserCreate):
    return user_controller.create_user(user)


@app.get("/users/", response_model=list[User])
def get_users():
    users = user_controller.get_users()
    return users
