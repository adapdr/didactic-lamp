"""File contains the WalletsService class."""
from typing import List

from api.schema.wallets import Wallets, WalletsList
from databases.models import Models


class WalletsService:
    """Service class for the WalletsRouter."""

    def options(self):
        return ["HEAD", "OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE"]

    def create(self, data: Wallets):
        """Creates a `Wallets` Entity from data"""
        result = Models.wallets.create(data.with_secrets()).fresh()
        return Wallets.from_orm(result)

    def retrieve(self, uuid: str) -> Wallets:
        """Retrieves a `Wallets` Entity by uuid"""
        result = Models.wallets.find(uuid)
        return Wallets.from_orm(result)

    def listed(self, limit: int = 10, page_nr: int = 1, **kwargs) -> List[Wallets]:
        """Retrieves a `Wallets` Entity by uuid"""
        # ? Removes all empty kwarg pairs =)
        query = {key: value for key, value in kwargs.items() if value}
        result = Models.wallets.where(query).simple_paginate(limit, page_nr)
        return WalletsList(**result.serialize()).data

    def update(self, uuid: str, data: Wallets) -> Wallets:
        """Updates a `Wallets` Entity by uuid with data"""
        result = Models.wallets.where({"uuid": uuid}).update(data.dict()).get()
        return Wallets.from_orm(result)

    def replace(self, uuid: str, data: Wallets) -> Wallets:
        """Replaces a `Wallets` Entity by uuid with data"""
        self.delete(uuid)
        return self.create(data)

    def delete(self, uuid: str) -> Wallets:
        """Delete a `Wallets` Entity by uuid"""
        result = Models.wallets.delete(uuid)
        return Wallets.from_orm(result)

    def deleted(self, limit: int = 10, page_nr: int = 1, **kwargs) -> List[Wallets]:
        # ? Removes all empty kwarg pairs =)
        query = {key: value for key, value in kwargs.items() if value}
        query.update({"deleted_at": None})
        result = (
            Models.wallets.where(query).with_trashed().simple_paginate(limit, page_nr)
        )
        return WalletsList(**result.serialize()).data
