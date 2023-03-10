"""File contains response model/schema for the `Wallets` table"""
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, SecretStr


class Wallets(BaseModel):
    """Model for a `Wallets` object"""

    # ? References
    uuid: UUID = Field(description="Unique IDentifier", default_factory=uuid4)
    user_id: UUID = Field(..., description="User IDentifier")

    # ? Data properties
    name: Optional[str] = Field("MyWallet", description="")
    adderss: SecretStr = Field("", description="The wallet address")

    # ? Timestamps
    __created_at__: str = Field(..., description="When the record was created")
    __updated_at__: str = Field(..., description="When the record was last updated")
    __deleted_at__: str = Field(..., description="When the record was deleted")

    class Config:
        """Internal pydantic config"""
        orm_mode = True

    def with_secrets(self):
        """Return a copy of the model with secrets"""
        return self.copy(
            update={
                "password": self.password.get_secret_value(),
                "salt": self.salt.get_secret_value(),
            }
        ).dict()


class WalletsList(BaseModel):
    """Model for a `Wallets` object"""

    data: List[Wallets]


class WalletsSchema:
    """Container holding all Wallets Schema"""

    Wallets = Wallets
    WalletsList = List[Wallets]
