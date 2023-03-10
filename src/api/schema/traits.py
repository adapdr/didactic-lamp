"""File contains response model/schema for the `Traits` table"""
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, SecretStr


class Traits(BaseModel):
    """Model for a `Traits` object"""

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


class TraitsList(BaseModel):
    """Model for a `Traits` object"""

    data: List[Traits]


class TraitsSchema:
    """Container holding all Traits Schema"""

    Traits = Traits
    TraitsList = List[Traits]
