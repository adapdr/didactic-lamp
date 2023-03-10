"""File contains endpoint router for '/vendors'"""
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
    prefix="/api/vendors", tags=["Vendors CRUD"], dependencies=[Security(Auth.basic)]
)

# ? Select Schema & Responses
Schema = Schema.Vendors
Responses = Responses.Vendors


# ? Router Endpoints
@router.options(path="/", operation_id="api.vendors.options", responses=Responses.options)
async def vendors_options(service=Depends(Services.Vendors)):
    """Endpoint is used to find options for the `Vendors` router"""
    result = service.options()

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Response(headers={"allow": str(result)})


@router.post(
    path="/",
    operation_id="api.vendors.create",
    responses=Responses.create,
    status_code=201,
)
async def create_vendors(
    vendors: Schema.Vendors,
    service=Depends(Services.Vendors),
):
    """Endpoint is used to create a `Vendors` entity"""
    result = service.create(vendors)

    if not result:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)

    return result


@router.get(path="/", operation_id="api.vendors.listed", responses=Responses.listed)
async def retrieve_vendors_list(
    name: str = Query(None, description="Name of the Vendors Entity to retrieve"),
    page_nr: int = Query(1, description="Page number to retrieve"),
    limit: int = Query(10, description="Number of items to retrieve"),
    service=Depends(Services.Vendors),
):
    """Endpoint is used to retrieve a list of `Vendors` entities"""

    result = service.listed(name=name, limit=limit, page_nr=page_nr)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.get(
    path="/deleted", operation_id="api.vendors.deleted", responses=Responses.listed
)
async def retrieve_deleted_vendors(
    name: str = Query(None, description="Name of the Vendors Entity to retrieve"),
    page_nr: int = Query(1, description="Page number to retrieve"),
    limit: int = Query(10, description="Number of items to retrieve"),
    service=Depends(Services.Vendors),
):
    """Endpoint is used to retrieve a list of `Vendors` entities"""

    result = service.deleted(name=name, limit=limit, page_nr=page_nr)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.get(
    path="/{uuid}",
    operation_id="api.vendors.retrieve",
    responses=Responses.retrieve,
)
async def retrieve_vendors(
    uuid: UUID = Path(
        None, description="Unique Identifier for the Vendors Entity to retrieve"
    ),
    service=Depends(Services.Vendors),
):
    """Endpoint is used to retrieve a `Vendors` entity"""

    result = service.retrieve(uuid)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.put(
    path="/{uuid}", operation_id="api.vendors.replace", responses=Responses.replace
)
async def replace_vendors(
    vendors: Schema.Vendors,
    uuid: str = Path(
        ..., description="Unique Identifier for the Vendors Entity to update"
    ),
    service=Depends(Services.Vendors),
):
    """Endpoint is used to replace a `Vendors` entity"""
    result = service.replace(uuid, vendors)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.patch(
    path="/{uuid}", operation_id="api.vendors.update", responses=Responses.update
)
async def update_vendors(
    vendors: Schema.Vendors,
    uuid: str = Path(
        ..., description="Unique Identifier for the Vendors Entity to update"
    ),
    service=Depends(Services.Vendors),
):
    """Endpoint is used to update a `Vendors` entity"""
    result = service.update(uuid, vendors)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.delete(
    path="/{uuid}",
    operation_id="api.vendors.delete",
    responses=Responses.delete,
    status_code=204,
)
async def delete_vendors(
    uuid: str = Path(
        ..., description="Unique Identifier for the Vendors Entity to delete"
    ),
    service=Depends(Services.Vendors),
):
    """Endpoint is used to delete a `Vendors` entity"""
    result = service.delete(uuid)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)
