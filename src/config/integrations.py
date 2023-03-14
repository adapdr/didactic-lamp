"""File contains Integrations Config Container"""
from pydantic import BaseSettings, Field


class IntegrationsConfig(BaseSettings):
    """Integrations Config Container"""

    # ? Zapper.fi
    zapper_api_key: str = Field(None, description="Zapper API Key")

    class Config:
        """Internal configurations for the container"""

        env_file = ".env"
        env_prefix = "INT_"
        env_file_encoding = "utf-8"
        case_sensitive = False
