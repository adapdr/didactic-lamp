"""File contains endpoint router for '/behaviours'"""
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
    prefix="/api/behaviours", tags=["Behaviours CRUD"], dependencies=[Security(Auth.basic)]
)

# ? Select Schema & Responses
Schema = Schema.Behaviours
Responses = Responses.Behaviours


# ? Router Endpoints
@router.options(path="/", operation_id="api.behaviours.options", responses=Responses.options)
async def behaviours_options(service=Depends(Services.Behaviours)):
    """Endpoint is used to find options for the `Behaviours` router"""
    result = service.options()

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Response(headers={"allow": str(result)})


@router.post(
    path="/",
    operation_id="api.behaviours.create",
    responses=Responses.create,
    status_code=201,
)
async def create_behaviours(
    behaviours: Schema.Behaviours,
    service=Depends(Services.Behaviours),
):
    """Endpoint is used to create a `Behaviours` entity"""
    result = service.create(behaviours)

    if not result:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)

    return result


@router.get(path="/", operation_id="api.behaviours.listed", responses=Responses.listed)
async def retrieve_behaviours_list(
    name: str = Query(None, description="Name of the Behaviours Entity to retrieve"),
    page_nr: int = Query(1, description="Page number to retrieve"),
    limit: int = Query(10, description="Number of items to retrieve"),
    service=Depends(Services.Behaviours),
):
    """Endpoint is used to retrieve a list of `Behaviours` entities"""

    result = service.listed(name=name, limit=limit, page_nr=page_nr)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.get(
    path="/deleted", operation_id="api.behaviours.deleted", responses=Responses.listed
)
async def retrieve_deleted_behaviours(
    name: str = Query(None, description="Name of the Behaviours Entity to retrieve"),
    page_nr: int = Query(1, description="Page number to retrieve"),
    limit: int = Query(10, description="Number of items to retrieve"),
    service=Depends(Services.Behaviours),
):
    """Endpoint is used to retrieve a list of `Behaviours` entities"""

    result = service.deleted(name=name, limit=limit, page_nr=page_nr)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.get(
    path="/{uuid}",
    operation_id="api.behaviours.retrieve",
    responses=Responses.retrieve,
)
async def retrieve_behaviours(
    uuid: UUID = Path(
        None, description="Unique Identifier for the Behaviours Entity to retrieve"
    ),
    service=Depends(Services.Behaviours),
):
    """Endpoint is used to retrieve a `Behaviours` entity"""

    result = service.retrieve(uuid)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.put(
    path="/{uuid}", operation_id="api.behaviours.replace", responses=Responses.replace
)
async def replace_behaviours(
    behaviours: Schema.Behaviours,
    uuid: str = Path(
        ..., description="Unique Identifier for the Behaviours Entity to update"
    ),
    service=Depends(Services.Behaviours),
):
    """Endpoint is used to replace a `Behaviours` entity"""
    result = service.replace(uuid, behaviours)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.patch(
    path="/{uuid}", operation_id="api.behaviours.update", responses=Responses.update
)
async def update_behaviours(
    behaviours: Schema.Behaviours,
    uuid: str = Path(
        ..., description="Unique Identifier for the Behaviours Entity to update"
    ),
    service=Depends(Services.Behaviours),
):
    """Endpoint is used to update a `Behaviours` entity"""
    result = service.update(uuid, behaviours)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.delete(
    path="/{uuid}",
    operation_id="api.behaviours.delete",
    responses=Responses.delete,
    status_code=204,
)
async def delete_behaviours(
    uuid: str = Path(
        ..., description="Unique Identifier for the Behaviours Entity to delete"
    ),
    service=Depends(Services.Behaviours),
):
    """Endpoint is used to delete a `Behaviours` entity"""
    result = service.delete(uuid)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)
