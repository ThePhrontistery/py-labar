from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

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
    user_id = user_controller.get_user_by_id(4)
    return templates.TemplateResponse("index.html", {"request": request, "user_data": user_data, "user_id": user_id})