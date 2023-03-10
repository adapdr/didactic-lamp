"""File contains endpoint router for '/wallets'"""
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
    prefix="/api/wallets", tags=["Wallets CRUD"], dependencies=[Security(Auth.basic)]
)

# ? Select Schema & Responses
Schema = Schema.Wallets
Responses = Responses.Wallets


# ? Router Endpoints
@router.options(path="/", operation_id="api.wallets.options", responses=Responses.options)
async def wallets_options(service=Depends(Services.Wallets)):
    """Endpoint is used to find options for the `Wallets` router"""
    result = service.options()

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Response(headers={"allow": str(result)})


@router.post(
    path="/",
    operation_id="api.wallets.create",
    responses=Responses.create,
    status_code=201,
)
async def create_wallets(
    wallets: Schema.Wallets,
    service=Depends(Services.Wallets),
):
    """Endpoint is used to create a `Wallets` entity"""
    result = service.create(wallets)

    if not result:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)

    return result


@router.get(path="/", operation_id="api.wallets.listed", responses=Responses.listed)
async def retrieve_wallets_list(
    name: str = Query(None, description="Name of the Wallets Entity to retrieve"),
    page_nr: int = Query(1, description="Page number to retrieve"),
    limit: int = Query(10, description="Number of items to retrieve"),
    service=Depends(Services.Wallets),
):
    """Endpoint is used to retrieve a list of `Wallets` entities"""

    result = service.listed(name=name, limit=limit, page_nr=page_nr)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.get(
    path="/deleted", operation_id="api.wallets.deleted", responses=Responses.listed
)
async def retrieve_deleted_wallets(
    name: str = Query(None, description="Name of the Wallets Entity to retrieve"),
    page_nr: int = Query(1, description="Page number to retrieve"),
    limit: int = Query(10, description="Number of items to retrieve"),
    service=Depends(Services.Wallets),
):
    """Endpoint is used to retrieve a list of `Wallets` entities"""

    result = service.deleted(name=name, limit=limit, page_nr=page_nr)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.get(
    path="/{uuid}",
    operation_id="api.wallets.retrieve",
    responses=Responses.retrieve,
)
async def retrieve_wallets(
    uuid: UUID = Path(
        None, description="Unique Identifier for the Wallets Entity to retrieve"
    ),
    service=Depends(Services.Wallets),
):
    """Endpoint is used to retrieve a `Wallets` entity"""

    result = service.retrieve(uuid)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.put(
    path="/{uuid}", operation_id="api.wallets.replace", responses=Responses.replace
)
async def replace_wallets(
    wallets: Schema.Wallets,
    uuid: str = Path(
        ..., description="Unique Identifier for the Wallets Entity to update"
    ),
    service=Depends(Services.Wallets),
):
    """Endpoint is used to replace a `Wallets` entity"""
    result = service.replace(uuid, wallets)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.patch(
    path="/{uuid}", operation_id="api.wallets.update", responses=Responses.update
)
async def update_wallets(
    wallets: Schema.Wallets,
    uuid: str = Path(
        ..., description="Unique Identifier for the Wallets Entity to update"
    ),
    service=Depends(Services.Wallets),
):
    """Endpoint is used to update a `Wallets` entity"""
    result = service.update(uuid, wallets)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.delete(
    path="/{uuid}",
    operation_id="api.wallets.delete",
    responses=Responses.delete,
    status_code=204,
)
async def delete_wallets(
    uuid: str = Path(
        ..., description="Unique Identifier for the Wallets Entity to delete"
    ),
    service=Depends(Services.Wallets),
):
    """Endpoint is used to delete a `Wallets` entity"""
    result = service.delete(uuid)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)
