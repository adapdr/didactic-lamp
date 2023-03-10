"""File contains the WebhooksService class."""
from typing import List

from api.schema.webhooks import Webhooks, WebhooksList
from databases.models import Models


class WebhooksService:
    """Service class for the WebhooksRouter."""

    def options(self):
        return ["HEAD", "OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE"]

    def create(self, data: Webhooks):
        """Creates a `Webhooks` Entity from data"""
        result = Models.webhooks.create(data.with_secrets()).fresh()
        return Webhooks.from_orm(result)

    def retrieve(self, uuid: str) -> Webhooks:
        """Retrieves a `Webhooks` Entity by uuid"""
        result = Models.webhooks.find(uuid)
        return Webhooks.from_orm(result)

    def listed(self, limit: int = 10, page_nr: int = 1, **kwargs) -> List[Webhooks]:
        """Retrieves a `Webhooks` Entity by uuid"""
        # ? Removes all empty kwarg pairs =)
        query = {key: value for key, value in kwargs.items() if value}
        result = Models.webhooks.where(query).simple_paginate(limit, page_nr)
        return WebhooksList(**result.serialize()).data

    def update(self, uuid: str, data: Webhooks) -> Webhooks:
        """Updates a `Webhooks` Entity by uuid with data"""
        result = Models.webhooks.where({"uuid": uuid}).update(data.dict()).get()
        return Webhooks.from_orm(result)

    def replace(self, uuid: str, data: Webhooks) -> Webhooks:
        """Replaces a `Webhooks` Entity by uuid with data"""
        self.delete(uuid)
        return self.create(data)

    def delete(self, uuid: str) -> Webhooks:
        """Delete a `Webhooks` Entity by uuid"""
        result = Models.webhooks.delete(uuid)
        return Webhooks.from_orm(result)

    def deleted(self, limit: int = 10, page_nr: int = 1, **kwargs) -> List[Webhooks]:
        # ? Removes all empty kwarg pairs =)
        query = {key: value for key, value in kwargs.items() if value}
        query.update({"deleted_at": None})
        result = (
            Models.webhooks.where(query).with_trashed().simple_paginate(limit, page_nr)
        )
        return WebhooksList(**result.serialize()).data
