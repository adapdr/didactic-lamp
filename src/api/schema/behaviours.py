"""File contains response model/schema for the `Behaviours` table"""
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Behaviours(BaseModel):
    """Model for a `Behaviours` object"""

    # ? References
    uuid: UUID = Field(description="Unique IDentifier", default_factory=uuid4)
    user_id: UUID = Field(..., description="User IDentifier")

    # ? Timestamps
    __created_at__: str = Field(..., description="When the record was created")
    __updated_at__: str = Field(..., description="When the record was last updated")
    __deleted_at__: str = Field(..., description="When the record was deleted")

    class Config:
        """Internal pydantic config"""
        orm_mode = True


class BehavioursList(BaseModel):
    """Model for a `Behaviours` object"""

    data: List[Behaviours]


class BehavioursSchema:
    """Container holding all Behaviours Schema"""

    Behaviours = Behaviours
    BehavioursList = List[Behaviours]
