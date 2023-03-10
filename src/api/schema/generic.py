"""File contains generic models"""
from typing import List

from pydantic import BaseModel, Field


class Message(BaseModel):
    """Generic message model"""

    msg: str


class Meta(BaseModel):
    """Generic meta model"""

    count: str = Field(..., description="Total number of items in the list")
    current_page: int = Field(..., description="Current page of the list")
    next_page: int = Field(..., description="Next page of the list")
    previous_page: int = Field(..., description="Previous page of the list")


class Paginated(BaseModel):
    """Generic paginated model"""

    meta: Meta = Meta
    data: List[object] = Field(..., description="Data Entity object")


class GenericSchema:
    """Container class for all generic models"""

    Message: Message = Message
    MessageList: list[Message] = [Message]
    Paginated: Paginated = Paginated
