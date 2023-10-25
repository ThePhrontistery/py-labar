from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.business.controllers.user_controller import get_user_by_id, router as user_router
from app.business.controllers.user_controller import get_users

app = FastAPI()

# Configura Jinja2 para cargar plantillas desde el directorio 'templates'
templates = Jinja2Templates(directory="app/templates")

# Ruta principal para renderizar la plantilla HTML
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    user_data = get_users()
    user_id = get_user_by_id(2)
    return templates.TemplateResponse("index.html", {"request": request, "user_data": user_data, "user_id": user_id})

# Agrega el controlador de usuarios
app.include_router(user_router, prefix="/users", tags=["users"])