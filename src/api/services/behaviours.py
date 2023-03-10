"""File contains the BehavioursService class."""
from typing import List

from api.schema.behaviours import Behaviours, BehavioursList
from databases.models import Models


class BehavioursService:
    """Service class for the BehavioursRouter."""

    def options(self):
        return ["HEAD", "OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE"]

    def create(self, data: Behaviours):
        """Creates a `Behaviours` Entity from data"""
        result = Models.behaviours.create(data.with_secrets()).fresh()
        return Behaviours.from_orm(result)

    def retrieve(self, uuid: str) -> Behaviours:
        """Retrieves a `Behaviours` Entity by uuid"""
        result = Models.behaviours.find(uuid)
        return Behaviours.from_orm(result)

    def listed(self, limit: int = 10, page_nr: int = 1, **kwargs) -> List[Behaviours]:
        """Retrieves a `Behaviours` Entity by uuid"""
        # ? Removes all empty kwarg pairs =)
        query = {key: value for key, value in kwargs.items() if value}
        result = Models.behaviours.where(query).simple_paginate(limit, page_nr)
        return BehavioursList(**result.serialize()).data

    def update(self, uuid: str, data: Behaviours) -> Behaviours:
        """Updates a `Behaviours` Entity by uuid with data"""
        result = Models.behaviours.where({"uuid": uuid}).update(data.dict()).get()
        return Behaviours.from_orm(result)

    def replace(self, uuid: str, data: Behaviours) -> Behaviours:
        """Replaces a `Behaviours` Entity by uuid with data"""
        self.delete(uuid)
        return self.create(data)

    def delete(self, uuid: str) -> Behaviours:
        """Delete a `Behaviours` Entity by uuid"""
        result = Models.behaviours.delete(uuid)
        return Behaviours.from_orm(result)

    def deleted(self, limit: int = 10, page_nr: int = 1, **kwargs) -> List[Behaviours]:
        # ? Removes all empty kwarg pairs =)
        query = {key: value for key, value in kwargs.items() if value}
        query.update({"deleted_at": None})
        result = (
            Models.behaviours.where(query).with_trashed().simple_paginate(limit, page_nr)
        )
        return BehavioursList(**result.serialize()).data
