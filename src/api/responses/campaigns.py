"""File contains responses for the '/campaigns' endpoint router"""
from typing import List

from fastapi import status

from api.schema import Schema

from .generic import GenericResponses

Schema = Schema.Campaigns


class CampaignsResponses:
    """Class contains campaigns responses"""

    options = {
        status.HTTP_200_OK: {
            "content": None,
            "description": "Campaigns router options successfully retrieved",
            "headers": {
                "allow": {
                    "description": "Allowed methods for the Campaigns router",
                    "type": "List[string]",
                }
            },
        },
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }

    retrieve = {
        status.HTTP_200_OK: {
            "model": Schema.Campaigns,
            "description": "Campaigns successfully retrieved",
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

    listed = {
        status.HTTP_200_OK: {
            "model": List[Schema.Campaigns],
            "description": "CampaignsList successfully retrieved",
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

    create = {
        status.HTTP_201_CREATED: {
            "model": Schema.Campaigns,
            "description": "Campaigns successfully created",
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

    update = {
        status.HTTP_200_OK: {
            "model": Schema.Campaigns,
            "description": "Campaigns successfully updated",
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

    replace = {
        status.HTTP_200_OK: {
            "model": Schema.Campaigns,
            "description": "Campaigns successfully replaced",
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

    delete = {
        status.HTTP_204_NO_CONTENT: {
            "content": None,
            "description": "Campaigns successfully deleted",
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
