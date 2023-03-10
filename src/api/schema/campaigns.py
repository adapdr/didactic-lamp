"""File contains response model/schema for the `Campaigns` table"""
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field


class Campaigns(BaseModel):
    """Model for a `Campaigns` object"""

    # ? References
    uuid: UUID = Field(description="Unique IDentifier", default_factory=uuid4)
    vendor_id: UUID = Field(..., description="Vendor IDentifier")

    # ? Data properties
    name: Optional[str] = Field(..., description="Webhook Name")

    # ? Timestamps
    __created_at__: datetime = Field(None, description="When the webhook was created")
    __updated_at__: datetime = Field(
        None, description="When the webhook was last updated"
    )
    __deleted_at__: datetime = Field(None, description="When the webhook was deleted")

    class Config:
        """Internal pydantic config"""
        orm_mode = True


class CampaignsList(BaseModel):
    """Model for a `Campaigns` object"""

    data: List[Campaigns]


class CampaignsSchema:
    """Container holding all Campaigns Schema"""

    Campaigns = Campaigns
    CampaignsList = List[Campaigns]
