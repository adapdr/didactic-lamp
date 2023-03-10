"""File contains the VendorsService class."""
from typing import List

from api.schema.vendors import Vendors, VendorsList
from databases.models import Models


class VendorsService:
    """Service class for the VendorsRouter."""

    def options(self):
        return ["HEAD", "OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE"]

    def create(self, data: Vendors):
        """Creates a `Vendors` Entity from data"""
        result = Models.vendors.create(data.with_secrets()).fresh()
        return Vendors.from_orm(result)

    def retrieve(self, uuid: str) -> Vendors:
        """Retrieves a `Vendors` Entity by uuid"""
        result = Models.vendors.find(uuid)
        return Vendors.from_orm(result)

    def listed(self, limit: int = 10, page_nr: int = 1, **kwargs) -> List[Vendors]:
        """Retrieves a `Vendors` Entity by uuid"""
        # ? Removes all empty kwarg pairs =)
        query = {key: value for key, value in kwargs.items() if value}
        result = Models.vendors.where(query).simple_paginate(limit, page_nr)
        return VendorsList(**result.serialize()).data

    def update(self, uuid: str, data: Vendors) -> Vendors:
        """Updates a `Vendors` Entity by uuid with data"""
        result = Models.vendors.where({"uuid": uuid}).update(data.dict()).get()
        return Vendors.from_orm(result)

    def replace(self, uuid: str, data: Vendors) -> Vendors:
        """Replaces a `Vendors` Entity by uuid with data"""
        self.delete(uuid)
        return self.create(data)

    def delete(self, uuid: str) -> Vendors:
        """Delete a `Vendors` Entity by uuid"""
        result = Models.vendors.delete(uuid)
        return Vendors.from_orm(result)

    def deleted(self, limit: int = 10, page_nr: int = 1, **kwargs) -> List[Vendors]:
        # ? Removes all empty kwarg pairs =)
        query = {key: value for key, value in kwargs.items() if value}
        query.update({"deleted_at": None})
        result = (
            Models.vendors.where(query).with_trashed().simple_paginate(limit, page_nr)
        )
        return VendorsList(**result.serialize()).data
