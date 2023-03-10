"""File contains endpoint router for '/users'"""
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
    prefix="/api/users", tags=["Users CRUD"], dependencies=[Security(Auth.basic)]
)

# ? Select Schema & Responses
Schema = Schema.Users
Responses = Responses.Users


# ? Router Endpoints
@router.options(path="/", operation_id="api.users.options", responses=Responses.options)
async def users_options(service=Depends(Services.Users)):
    """Endpoint is used to find options for the `Users` router"""
    result = service.options()

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Response(headers={"allow": str(result)})


@router.post(
    path="/",
    operation_id="api.users.create",
    responses=Responses.create,
    status_code=201,
)
async def create_users(
    users: Schema.Users,
    background: BackgroundTasks,
    service=Depends(Services.Users),
):
    """Endpoint is used to create a `Users` entity"""
    result = service.create(users)

    # ? Is executed after the router has returned a response
    background.add_task(Tasks.Users.do_after, entity=result)

    if not result:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)

    return result


@router.get(path="/", operation_id="api.users.listed", responses=Responses.listed)
async def retrieve_users_list(
    name: str = Query(None, description="Name of the Users Entity to retrieve"),
    page_nr: int = Query(1, description="Page number to retrieve"),
    limit: int = Query(10, description="Number of items to retrieve"),
    service=Depends(Services.Users),
):
    """Endpoint is used to retrieve a list of `Users` entities"""

    result = service.listed(name=name, limit=limit, page_nr=page_nr)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.get(
    path="/deleted", operation_id="api.users.deleted", responses=Responses.listed
)
async def retrieve_deleted_users(
    name: str = Query(None, description="Name of the Users Entity to retrieve"),
    page_nr: int = Query(1, description="Page number to retrieve"),
    limit: int = Query(10, description="Number of items to retrieve"),
    service=Depends(Services.Users),
):
    """Endpoint is used to retrieve a list of `Users` entities"""

    result = service.deleted(name=name, limit=limit, page_nr=page_nr)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.get(
    path="/{uuid}",
    operation_id="api.users.retrieve",
    responses=Responses.retrieve,
)
async def retrieve_users(
    uuid: UUID = Path(
        None, description="Unique Identifier for the Users Entity to retrieve"
    ),
    service=Depends(Services.Users),
):
    """Endpoint is used to retrieve a `Users` entity"""

    result = service.retrieve(uuid)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.put(
    path="/{uuid}", operation_id="api.users.replace", responses=Responses.replace
)
async def replace_users(
    users: Schema.Users,
    uuid: str = Path(
        ..., description="Unique Identifier for the Users Entity to update"
    ),
    service=Depends(Services.Users),
):
    """Endpoint is used to replace a `Users` entity"""
    result = service.replace(uuid, users)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.patch(
    path="/{uuid}", operation_id="api.users.update", responses=Responses.update
)
async def update_users(
    users: Schema.Users,
    uuid: str = Path(
        ..., description="Unique Identifier for the Users Entity to update"
    ),
    service=Depends(Services.Users),
):
    """Endpoint is used to update a `Users` entity"""
    result = service.update(uuid, users)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.delete(
    path="/{uuid}",
    operation_id="api.users.delete",
    responses=Responses.delete,
    status_code=204,
)
async def delete_users(
    uuid: str = Path(
        ..., description="Unique Identifier for the Users Entity to delete"
    ),
    service=Depends(Services.Users),
):
    """Endpoint is used to delete a `Users` entity"""
    result = service.delete(uuid)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)
