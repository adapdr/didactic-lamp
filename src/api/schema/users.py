"""
File contains response model/schema for the `Users` table
"""
from random import choice
from secrets import token_urlsafe
from typing import List, Optional
from uuid import UUID, uuid4

from faker import Faker
from pydantic import BaseModel, EmailStr, Field, SecretStr

fake = Faker()
fake_age = fake.random_int(min=25, max=55)
fake_name = fake.name()
fake_email = f"{fake_name.lower().replace(' ', '_')}{fake_age}@example.com"


class Users(BaseModel):
    """Model for a `Users` object"""

    # ? References
    uuid: UUID = Field(description="Unique IDentifier", default_factory=uuid4)

    # ? Data properties
    name: str = Field(fake_name, description="Who to say users to")
    email: EmailStr = Field(fake_email, description="User email")
    age: Optional[int] = Field(fake_age, description="User age")
    gender: Optional[str] = Field(
        choice(["Male", "Female", "Nonbinary"]),
        description="User gender identification",
    )

    # ? Private properties
    password: SecretStr = Field(token_urlsafe(16), description="User password")
    salt: SecretStr = Field(token_urlsafe(128), description="Salt for password")

    # ? Timestamps
    __created_at__: str = Field(..., description="When the record was created")
    __updated_at__: str = Field(..., description="When the record was last updated")
    __deleted_at__: str = Field(..., description="When the record was deleted")

    class Config:
        orm_mode = True

    def with_secrets(self):
        """Return a copy of the model with secrets"""
        return self.copy(
            update={
                "password": self.password.get_secret_value(),
                "salt": self.salt.get_secret_value(),
            }
        ).dict()


class UsersList(BaseModel):
    """Model for a `Users` object"""

    data: List[Users]


class UsersSchema:
    """Container holding all Users Schema"""

    Users = Users
    UsersList = List[Users]
