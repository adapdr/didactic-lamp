"""File contains the CampaignsService class."""
from typing import List

from api.schema.campaigns import Campaigns, CampaignsList
from databases.models import Models


class CampaignsService:
    """Service class for the CampaignsRouter."""

    def options(self):
        return ["HEAD", "OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE"]

    def create(self, data: Campaigns):
        """Creates a `Campaigns` Entity from data"""
        result = Models.campaigns.create(data.with_secrets()).fresh()
        return Campaigns.from_orm(result)

    def retrieve(self, uuid: str) -> Campaigns:
        """Retrieves a `Campaigns` Entity by uuid"""
        result = Models.campaigns.find(uuid)
        return Campaigns.from_orm(result)

    def listed(self, limit: int = 10, page_nr: int = 1, **kwargs) -> List[Campaigns]:
        """Retrieves a `Campaigns` Entity by uuid"""
        # ? Removes all empty kwarg pairs =)
        query = {key: value for key, value in kwargs.items() if value}
        result = Models.campaigns.where(query).simple_paginate(limit, page_nr)
        return CampaignsList(**result.serialize()).data

    def update(self, uuid: str, data: Campaigns) -> Campaigns:
        """Updates a `Campaigns` Entity by uuid with data"""
        result = Models.campaigns.where({"uuid": uuid}).update(data.dict()).get()
        return Campaigns.from_orm(result)

    def replace(self, uuid: str, data: Campaigns) -> Campaigns:
        """Replaces a `Campaigns` Entity by uuid with data"""
        self.delete(uuid)
        return self.create(data)

    def delete(self, uuid: str) -> Campaigns:
        """Delete a `Campaigns` Entity by uuid"""
        result = Models.campaigns.delete(uuid)
        return Campaigns.from_orm(result)

    def deleted(self, limit: int = 10, page_nr: int = 1, **kwargs) -> List[Campaigns]:
        # ? Removes all empty kwarg pairs =)
        query = {key: value for key, value in kwargs.items() if value}
        query.update({"deleted_at": None})
        result = (
            Models.campaigns.where(query).with_trashed().simple_paginate(limit, page_nr)
        )
        return CampaignsList(**result.serialize()).data
