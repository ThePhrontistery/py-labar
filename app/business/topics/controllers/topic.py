import logging

from fastapi import APIRouter, Request, Form, status, Depends
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from app.business.topics.services.topic import TopicService

templates = Jinja2Templates(directory="templates")
router = APIRouter(prefix="/topics")

logger = logging.getLogger(__name__)
