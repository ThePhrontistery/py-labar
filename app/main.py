from typing import Annotated
from fastapi import Depends, FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

from app.business.controllers import user_controller

app = FastAPI()

# Configura Jinja2 para cargar plantillas desde el directorio 'templates'
templates = Jinja2Templates(directory="app/templates")

# Ruta principal para renderizar la plantilla HTML
@app.get("/", response_class=HTMLResponse)

async def read_root(request: Request):
    """
    Read_root function in main.py is fetching user_data and user_id using the controllers\\user_controller.py
    This function is also passing the user_data and user_id to the index.html template.
    """
    user_data = user_controller.get_users()
    user_id = user_controller.get_user_by_id(1)
    return templates.TemplateResponse("index.html", {"request": request, "user_data": user_data, "user_id": user_id})

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
