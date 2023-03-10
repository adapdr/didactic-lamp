"""
File contains response model/schema for the `Preferences` table
"""
from typing import List
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Preferences(BaseModel):
    """Model for a `Preferences` object"""

    # ? References
    uuid: UUID = Field(description="Unique IDentifier", default_factory=uuid4)
    user_id: UUID = Field(..., description="User IDentifier")

    # ? Data properties
    toggle_email: bool = Field(True, description="Toggle email")
    toggle_notifications: bool = Field(True, description="Toggle notifications")

    # ? Timestamps
    __created_at__: str = Field(..., description="When the record was created")
    __updated_at__: str = Field(..., description="When the record was last updated")

    class Config:
        """Internal pydantic config"""
        orm_mode = True


class PreferencesList(BaseModel):
    """Model for a `Preferences` object"""

    data: List[Preferences]


class PreferencesSchema:
    """Container holding all Preferences Schema"""

    Preferences = Preferences
