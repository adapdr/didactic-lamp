"""File contains endpoint router for '/preferences'"""
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

# ? Router Configuration
logger = getLogger(__name__)
router = APIRouter(
    prefix="/api/preferences",
    tags=["Preferences CRUD"],
    dependencies=[Security(Auth.basic)],
)

# ? Select Schema & Responses
Schema = Schema.Preferences
Responses = Responses.Preferences


# ? Router CRUD Endpoints
@router.options(
    path="/", operation_id="api.preferences.options", responses=Responses.options
)
async def preferences_options(service=Depends(Services.Preferences)):
    """Endpoint is used to find options for the `Preferences` router"""
    result = service.options()

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Response(headers={"allow": str(result)})


@router.post(
    path="/",
    operation_id="api.preferences.create",
    responses=Responses.create,
    status_code=201,
)
async def create_preferences(
    preferences: Schema.Preferences,
    background: BackgroundTasks,
    service=Depends(Services.Preferences),
):
    """Endpoint is used to create a `Preferences` entity"""
    result = service.create(preferences)

    # ? Is executed after the router has returned a response
    background.add_task(Tasks.get("preferences").do_after, entity="preferences")

    if not result:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)

    return result


@router.get(path="/", operation_id="api.preferences.listed", responses=Responses.listed)
async def retrieve_preferences_list(
    name: str = Query(None, description="Name of the Preferences Entity to retrieve"),
    page_nr: int = Query(1, description="Page number to retrieve"),
    limit: int = Query(10, description="Number of items to retrieve"),
    service=Depends(Services.Preferences),
):
    """Endpoint is used to retrieve a list of `Preferences` entities"""

    result = service.listed(name=name, limit=limit, page_nr=page_nr)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.get(
    path="/{uuid}",
    operation_id="api.preferences.retrieve",
    responses=Responses.retrieve,
)
async def retrieve_preferences(
    uuid: UUID = Path(
        None, description="Unique Identifier for the Preferences Entity to retrieve"
    ),
    service=Depends(Services.Preferences),
):
    """Endpoint is used to retrieve a `Preferences` entity"""

    result = service.retrieve(uuid)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.put(
    path="/{uuid}", operation_id="api.preferences.replace", responses=Responses.replace
)
async def replace_preferences(
    preferences: Schema.Preferences,
    uuid: str = Path(
        ..., description="Unique Identifier for the Preferences Entity to update"
    ),
    service=Depends(Services.Preferences),
):
    """Endpoint is used to replace a `Preferences` entity"""
    result = service.replace(uuid, preferences)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.patch(
    path="/{uuid}", operation_id="api.preferences.update", responses=Responses.update
)
async def update_preferences(
    preferences: Schema.Preferences,
    uuid: str = Path(
        ..., description="Unique Identifier for the Preferences Entity to update"
    ),
    service=Depends(Services.Preferences),
):
    """Endpoint is used to update a `Preferences` entity"""
    result = service.update(uuid, preferences)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.delete(
    path="/{uuid}",
    operation_id="api.preferences.delete",
    responses=Responses.delete,
    status_code=204,
)
async def delete_preferences(
    uuid: str = Path(
        ..., description="Unique Identifier for the Preferences Entity to delete"
    ),
    service=Depends(Services.Preferences),
):
    """Endpoint is used to delete a `Preferences` entity"""
    result = service.delete(uuid)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)
