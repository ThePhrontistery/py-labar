import logging
import uuid
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, Request, Form, Response
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from app.business.users.services.user import UserService

templates = Jinja2Templates(directory="templates")
router = APIRouter(prefix="/users")

logger = logging.getLogger(__name__)


@router.get("/")
async def home_page(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})
