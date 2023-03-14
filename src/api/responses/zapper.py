"""File contains responses for the '/zapper' endpoint router"""
from fastapi import status

from api.integrations.zapper.schema import Model

from .generic import GenericResponses


class ZapperResponses:
    """Class contains zapper responses"""

    retrieve = {
        status.HTTP_200_OK: {
            "model": Model,
            "description": "Wallet data successfully retrieved from Zapper API",
            "headers": {
                "content-length": {"description": "Content Length", "type": "int"},
                "date": {"description": "Response Date", "type": "Datetime"},
                "server": {"description": "API Server", "type": "string"},
            },
        },
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }
