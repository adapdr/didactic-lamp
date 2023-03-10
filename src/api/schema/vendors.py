"""File contains response model/schema for the `Vendors` table"""
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Vendors(BaseModel):
    """Model for a `Vendors` object"""

    # ? References
    uuid: UUID = Field(description="Unique IDentifier", default_factory=uuid4)
    name: Optional[str] = Field(description="Name of the vendor")

    # ? Timestamps
    __created_at__: str = Field(..., description="When the record was created")
    __updated_at__: str = Field(..., description="When the record was last updated")
    __deleted_at__: str = Field(..., description="When the record was deleted")

    class Config:
        """Internal pydantic config"""
        orm_mode = True


class VendorsList(BaseModel):
    """Model for a `Vendors` object"""

    data: List[Vendors]


class VendorsSchema:
    """Container holding all Vendors Schema"""

    Vendors = Vendors
    VendorsList = List[Vendors]
