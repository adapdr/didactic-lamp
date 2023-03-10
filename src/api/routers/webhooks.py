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
    prefix="/api/webhooks", tags=["Webhooks CRUD"], dependencies=[Security(Auth.basic)]
)

# ? Select Schema & Responses
Schema = Schema.Webhooks
Responses = Responses.Webhooks


# ? Router Endpoints
@router.options(path="/", operation_id="api.webhooks.options", responses=Responses.options)
async def webhooks_options(service=Depends(Services.Webhooks)):
    """Endpoint is used to find options for the `Webhooks` router"""
    result = service.options()

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Response(headers={"allow": str(result)})


@router.post(
    path="/",
    operation_id="api.webhooks.create",
    responses=Responses.create,
    status_code=201,
)
async def create_webhooks(
    webhooks: Schema.Webhooks,
    service=Depends(Services.Webhooks),
):
    """Endpoint is used to create a `Webhooks` entity"""
    result = service.create(webhooks)

    if not result:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)

    return result


@router.get(path="/", operation_id="api.webhooks.listed", responses=Responses.listed)
async def retrieve_webhooks_list(
    name: str = Query(None, description="Name of the Webhooks Entity to retrieve"),
    page_nr: int = Query(1, description="Page number to retrieve"),
    limit: int = Query(10, description="Number of items to retrieve"),
    service=Depends(Services.Webhooks),
):
    """Endpoint is used to retrieve a list of `Webhooks` entities"""

    result = service.listed(name=name, limit=limit, page_nr=page_nr)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.get(
    path="/deleted", operation_id="api.webhooks.deleted", responses=Responses.listed
)
async def retrieve_deleted_webhooks(
    name: str = Query(None, description="Name of the Webhooks Entity to retrieve"),
    page_nr: int = Query(1, description="Page number to retrieve"),
    limit: int = Query(10, description="Number of items to retrieve"),
    service=Depends(Services.Webhooks),
):
    """Endpoint is used to retrieve a list of `Webhooks` entities"""

    result = service.deleted(name=name, limit=limit, page_nr=page_nr)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.get(
    path="/{uuid}",
    operation_id="api.webhooks.retrieve",
    responses=Responses.retrieve,
)
async def retrieve_webhooks(
    uuid: UUID = Path(
        None, description="Unique Identifier for the Webhooks Entity to retrieve"
    ),
    service=Depends(Services.Webhooks),
):
    """Endpoint is used to retrieve a `Webhooks` entity"""

    result = service.retrieve(uuid)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.put(
    path="/{uuid}", operation_id="api.webhooks.replace", responses=Responses.replace
)
async def replace_webhooks(
    webhooks: Schema.Webhooks,
    uuid: str = Path(
        ..., description="Unique Identifier for the Webhooks Entity to update"
    ),
    service=Depends(Services.Webhooks),
):
    """Endpoint is used to replace a `Webhooks` entity"""
    result = service.replace(uuid, webhooks)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.patch(
    path="/{uuid}", operation_id="api.webhooks.update", responses=Responses.update
)
async def update_webhooks(
    webhooks: Schema.Webhooks,
    uuid: str = Path(
        ..., description="Unique Identifier for the Webhooks Entity to update"
    ),
    service=Depends(Services.Webhooks),
):
    """Endpoint is used to update a `Webhooks` entity"""
    result = service.update(uuid, webhooks)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.delete(
    path="/{uuid}",
    operation_id="api.webhooks.delete",
    responses=Responses.delete,
    status_code=204,
)
async def delete_webhooks(
    uuid: str = Path(
        ..., description="Unique Identifier for the Webhooks Entity to delete"
    ),
    service=Depends(Services.Webhooks),
):
    """Endpoint is used to delete a `Webhooks` entity"""
    result = service.delete(uuid)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)
