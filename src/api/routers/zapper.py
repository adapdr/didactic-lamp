"""File contains endpoint router for '/zapper'"""
from logging import getLogger
from uuid import UUID

from fastapi import APIRouter, Depends, Path, Query, Security, status
from fastapi.exceptions import HTTPException

from api.auth import Auth
from api.responses import Responses
from api.integrations import Integrations


# ? Router Configuration
logger = getLogger(__name__)
router = APIRouter(
    prefix="/api/integrations/zapper-api", tags=["Integrations"], dependencies=[Security(Auth.basic)]
)

# ? Select Schema & Responses
Responses = Responses.Zapper


@router.get(
    path="/{address}",
    operation_id="api.integrations.zapper.retrieve",
    responses=Responses.retrieve,
)
async def lookup_wallet_address(
    address: str = Path(
        None, description="Wallet to Lookup"
    ),
    integration=Depends(Integrations.Zapper),
):
    """Endpoint is used to lookup a users `wallet` on Zapper"""

    result = await integration.balances_apps(addresses=[address])

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result
