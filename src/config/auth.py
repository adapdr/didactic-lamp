"""File contains Auth Config Container"""
from pydantic import BaseSettings, Field


class AuthConfig(BaseSettings):
    """Auth Config Container"""

    username: str = Field("admin", description="Basic Auth Username")
    password: str = Field("admin", description="Basic Auth Password")

    class Config:
        """Internal configurations for the container"""

        env_file = ".env"
        env_prefix = "AUTH_"
        env_file_encoding = "utf-8"
        case_sensitive = False
