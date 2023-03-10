"""File contains the TraitsService class."""
from typing import List

from api.schema.traits import Traits, TraitsList
from databases.models import Models


class TraitsService:
    """Service class for the TraitsRouter."""

    def options(self):
        return ["HEAD", "OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE"]

    def create(self, data: Traits):
        """Creates a `Traits` Entity from data"""
        result = Models.traits.create(data.with_secrets()).fresh()
        return Traits.from_orm(result)

    def retrieve(self, uuid: str) -> Traits:
        """Retrieves a `Traits` Entity by uuid"""
        result = Models.traits.find(uuid)
        return Traits.from_orm(result)

    def listed(self, limit: int = 10, page_nr: int = 1, **kwargs) -> List[Traits]:
        """Retrieves a `Traits` Entity by uuid"""
        # ? Removes all empty kwarg pairs =)
        query = {key: value for key, value in kwargs.items() if value}
        result = Models.traits.where(query).simple_paginate(limit, page_nr)
        return TraitsList(**result.serialize()).data

    def update(self, uuid: str, data: Traits) -> Traits:
        """Updates a `Traits` Entity by uuid with data"""
        result = Models.traits.where({"uuid": uuid}).update(data.dict()).get()
        return Traits.from_orm(result)

    def replace(self, uuid: str, data: Traits) -> Traits:
        """Replaces a `Traits` Entity by uuid with data"""
        self.delete(uuid)
        return self.create(data)

    def delete(self, uuid: str) -> Traits:
        """Delete a `Traits` Entity by uuid"""
        result = Models.traits.delete(uuid)
        return Traits.from_orm(result)

    def deleted(self, limit: int = 10, page_nr: int = 1, **kwargs) -> List[Traits]:
        # ? Removes all empty kwarg pairs =)
        query = {key: value for key, value in kwargs.items() if value}
        query.update({"deleted_at": None})
        result = (
            Models.traits.where(query).with_trashed().simple_paginate(limit, page_nr)
        )
        return TraitsList(**result.serialize()).data
