import logging

from fastapi import APIRouter, Request, Form
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter(prefix="/users")

logger = logging.getLogger(__name__)


@router.get("/")
async def home_page(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


@router.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    response = RedirectResponse(url="/home", status_code=status.HTTP_303_SEE_OTHER)

    return response