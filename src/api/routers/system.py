"""File contains system endpoint router and template controller"""
from logging import getLogger

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from api.responses import Responses

# ? Setup Router
logger = getLogger(__name__)
templates = Jinja2Templates(directory="frontend/templates")
router = APIRouter(
    tags=["System"],
)

# ? Select Schema & Responses
Responses = Responses.System


# ? Router endpoints
@router.get(
    path="/",
    operation_id="api.system.index",
    status_code=200,
    responses=Responses.index,
)
async def index(request: Request):
    """
    Serves front-end templates
    """
    return templates.TemplateResponse("pages/index.html", {"request": request})
