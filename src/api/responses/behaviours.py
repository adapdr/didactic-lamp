"""File contains responses for the '/behaviours' endpoint router"""
from typing import List

from fastapi import status

from api.schema import Schema

from .generic import GenericResponses

Schema = Schema.Behaviours


class BehavioursResponses:
    """Class contains behaviours responses"""

    options = {
        status.HTTP_200_OK: {
            "content": None,
            "description": "Behaviours router options successfully retrieved",
            "headers": {
                "allow": {
                    "description": "Allowed methods for the Behaviours router",
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
            "model": Schema.Behaviours,
            "description": "Behaviours successfully retrieved",
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
            "model": List[Schema.Behaviours],
            "description": "BehavioursList successfully retrieved",
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
            "model": Schema.Behaviours,
            "description": "Behaviours successfully created",
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
            "model": Schema.Behaviours,
            "description": "Behaviours successfully updated",
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
            "model": Schema.Behaviours,
            "description": "Behaviours successfully replaced",
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
            "description": "Behaviours successfully deleted",
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
