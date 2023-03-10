"""File contains response model/schema for the `Webhooks` table"""
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field, AnyHttpUrl, Json


class Webhooks(BaseModel):
    """Model for a `Webhooks` object"""

    # ? References
    uuid: UUID = Field(description="Unique IDentifier", default_factory=uuid4)
    vendor_id: UUID = Field(..., description="Vendor IDentifier")

    # ? Data properties
    name: Optional[str] = Field(..., description="Webhook Name")
    hook_url: AnyHttpUrl = Field(..., description="Webhook URL")
    meta: Optional[Json] = Field(None, description="Webhook Meta")

    # ? Timestamps
    __created_at__: datetime = Field(None, description="When the webhook was created")
    __updated_at__: datetime = Field(
        None, description="When the webhook was last updated"
    )
    __deleted_at__: datetime = Field(None, description="When the webhook was deleted")

    class Config:
        """Internal pydantic config"""
        orm_mode = True


class WebhooksList(BaseModel):
    """Model for a `Webhooks` object"""

    data: List[Webhooks]


class WebhooksSchema:
    """Container holding all Webhooks Schema"""

    Webhooks = Webhooks
    WebhooksList = List[Webhooks]
