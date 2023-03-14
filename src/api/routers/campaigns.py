"""File contains endpoint router for '/campaigns'"""
from logging import getLogger
from uuid import UUID

from fastapi import APIRouter, Depends, Path, Query, Security, status
from fastapi.exceptions import HTTPException
from fastapi.responses import Response

from api.auth import Auth
from api.responses import Responses
from api.schema import Schema
from api.services import Services

# ! TODO: Add intergations & events

# ? Router Configuration
logger = getLogger(__name__)
router = APIRouter(
    prefix="/api/campaigns", tags=["Campaigns CRUD"], dependencies=[Security(Auth.basic)]
)

# ? Select Schema & Responses
Schema = Schema.Campaigns
Responses = Responses.Campaigns


# ? Router Endpoints
@router.options(path="/", operation_id="api.campaigns.options", responses=Responses.options)
async def campaigns_options(service=Depends(Services.Campaigns)):
    """Endpoint is used to find options for the `Campaigns` router"""
    result = service.options()

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Response(headers={"allow": str(result)})


@router.post(
    path="/",
    operation_id="api.campaigns.create",
    responses=Responses.create,
    status_code=201,
)
async def create_campaigns(
    campaigns: Schema.Campaigns,
    service=Depends(Services.Campaigns),
):
    """Endpoint is used to create a `Campaigns` entity"""
    result = service.create(campaigns)

    if not result:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)

    return result


@router.get(path="/", operation_id="api.campaigns.listed", responses=Responses.listed)
async def retrieve_campaigns_list(
    name: str = Query(None, description="Name of the Campaigns Entity to retrieve"),
    page_nr: int = Query(1, description="Page number to retrieve"),
    limit: int = Query(10, description="Number of items to retrieve"),
    service=Depends(Services.Campaigns),
):
    """Endpoint is used to retrieve a list of `Campaigns` entities"""

    result = service.listed(name=name, limit=limit, page_nr=page_nr)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.get(
    path="/deleted", operation_id="api.campaigns.deleted", responses=Responses.listed
)
async def retrieve_deleted_campaigns(
    name: str = Query(None, description="Name of the Campaigns Entity to retrieve"),
    page_nr: int = Query(1, description="Page number to retrieve"),
    limit: int = Query(10, description="Number of items to retrieve"),
    service=Depends(Services.Campaigns),
):
    """Endpoint is used to retrieve a list of `Campaigns` entities"""

    result = service.deleted(name=name, limit=limit, page_nr=page_nr)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.get(
    path="/{uuid}",
    operation_id="api.campaigns.retrieve",
    responses=Responses.retrieve,
)
async def retrieve_campaigns(
    uuid: UUID = Path(
        None, description="Unique Identifier for the Campaigns Entity to retrieve"
    ),
    service=Depends(Services.Campaigns),
):
    """Endpoint is used to retrieve a `Campaigns` entity"""

    result = service.retrieve(uuid)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.put(
    path="/{uuid}", operation_id="api.campaigns.replace", responses=Responses.replace
)
async def replace_campaigns(
    campaigns: Schema.Campaigns,
    uuid: str = Path(
        ..., description="Unique Identifier for the Campaigns Entity to update"
    ),
    service=Depends(Services.Campaigns),
):
    """Endpoint is used to replace a `Campaigns` entity"""
    result = service.replace(uuid, campaigns)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.patch(
    path="/{uuid}", operation_id="api.campaigns.update", responses=Responses.update
)
async def update_campaigns(
    campaigns: Schema.Campaigns,
    uuid: str = Path(
        ..., description="Unique Identifier for the Campaigns Entity to update"
    ),
    service=Depends(Services.Campaigns),
):
    """Endpoint is used to update a `Campaigns` entity"""
    result = service.update(uuid, campaigns)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.delete(
    path="/{uuid}",
    operation_id="api.campaigns.delete",
    responses=Responses.delete,
    status_code=204,
)
async def delete_campaigns(
    uuid: str = Path(
        ..., description="Unique Identifier for the Campaigns Entity to delete"
    ),
    service=Depends(Services.Campaigns),
):
    """Endpoint is used to delete a `Campaigns` entity"""
    result = service.delete(uuid)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)
