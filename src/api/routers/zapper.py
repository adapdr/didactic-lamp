"""File contains endpoint router for '/webhooks'"""
from logging import getLogger
from uuid import UUID

from fastapi import APIRouter, BackgroundTasks, Depends, Path, Query, Security, status
from fastapi.exceptions import HTTPException
from fastapi.responses import Response

from api.auth import Auth
from api.responses import Responses
from api.schema import Schema
from api.services import Services
from api.tasks import Tasks

# ! TODO: Add intergations & events

# ? Router Configuration
logger = getLogger(__name__)
router = APIRouter(
    prefix="/api/integrations/zapper",
)

# ? Select Schema & Responses
Schema = Schema.Webhooks
Responses = Responses.Webhooks

# ? Router Endpoints
@router.post(
    path="/",
    operation_id="api.webhooks.create",
    responses=Responses.create,
    status_code=201,
    tags=["Integrations"]
)
async def hook_something(
    webhooks: Schema.Webhooks,
    service=Depends(Services.Webhooks),
):
    """Endpoint is used as a callback hook for Zapper API"""
    result = service.create(webhooks)

    if not result:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)

    return Response("OK", status.HTTP_200_OK)
