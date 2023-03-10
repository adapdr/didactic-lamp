"""File contains endpoint router for '/traits'"""
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
    prefix="/api/traits", tags=["Traits CRUD"], dependencies=[Security(Auth.basic)]
)

# ? Select Schema & Responses
Schema = Schema.Traits
Responses = Responses.Traits


# ? Router Endpoints
@router.options(path="/", operation_id="api.traits.options", responses=Responses.options)
async def traits_options(service=Depends(Services.Traits)):
    """Endpoint is used to find options for the `Traits` router"""
    result = service.options()

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Response(headers={"allow": str(result)})


@router.post(
    path="/",
    operation_id="api.traits.create",
    responses=Responses.create,
    status_code=201,
)
async def create_traits(
    traits: Schema.Traits,
    service=Depends(Services.Traits),
):
    """Endpoint is used to create a `Traits` entity"""
    result = service.create(traits)

    if not result:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)

    return result


@router.get(path="/", operation_id="api.traits.listed", responses=Responses.listed)
async def retrieve_traits_list(
    name: str = Query(None, description="Name of the Traits Entity to retrieve"),
    page_nr: int = Query(1, description="Page number to retrieve"),
    limit: int = Query(10, description="Number of items to retrieve"),
    service=Depends(Services.Traits),
):
    """Endpoint is used to retrieve a list of `Traits` entities"""

    result = service.listed(name=name, limit=limit, page_nr=page_nr)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.get(
    path="/deleted", operation_id="api.traits.deleted", responses=Responses.listed
)
async def retrieve_deleted_traits(
    name: str = Query(None, description="Name of the Traits Entity to retrieve"),
    page_nr: int = Query(1, description="Page number to retrieve"),
    limit: int = Query(10, description="Number of items to retrieve"),
    service=Depends(Services.Traits),
):
    """Endpoint is used to retrieve a list of `Traits` entities"""

    result = service.deleted(name=name, limit=limit, page_nr=page_nr)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.get(
    path="/{uuid}",
    operation_id="api.traits.retrieve",
    responses=Responses.retrieve,
)
async def retrieve_traits(
    uuid: UUID = Path(
        None, description="Unique Identifier for the Traits Entity to retrieve"
    ),
    service=Depends(Services.Traits),
):
    """Endpoint is used to retrieve a `Traits` entity"""

    result = service.retrieve(uuid)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.put(
    path="/{uuid}", operation_id="api.traits.replace", responses=Responses.replace
)
async def replace_traits(
    traits: Schema.Traits,
    uuid: str = Path(
        ..., description="Unique Identifier for the Traits Entity to update"
    ),
    service=Depends(Services.Traits),
):
    """Endpoint is used to replace a `Traits` entity"""
    result = service.replace(uuid, traits)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.patch(
    path="/{uuid}", operation_id="api.traits.update", responses=Responses.update
)
async def update_traits(
    traits: Schema.Traits,
    uuid: str = Path(
        ..., description="Unique Identifier for the Traits Entity to update"
    ),
    service=Depends(Services.Traits),
):
    """Endpoint is used to update a `Traits` entity"""
    result = service.update(uuid, traits)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.delete(
    path="/{uuid}",
    operation_id="api.traits.delete",
    responses=Responses.delete,
    status_code=204,
)
async def delete_traits(
    uuid: str = Path(
        ..., description="Unique Identifier for the Traits Entity to delete"
    ),
    service=Depends(Services.Traits),
):
    """Endpoint is used to delete a `Traits` entity"""
    result = service.delete(uuid)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)
