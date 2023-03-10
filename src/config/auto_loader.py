"""File contains Auto-Loader Configurations"""
from pydantic import BaseSettings, Field


class AutoLoader(BaseSettings):
    """API Config Container"""

    routers_location: str = Field("api/routers")
    schema_location: str = Field("api/schema")
    responses_location: str = Field("api/responses")
    services_loaction: str = Field("api/services")
    tasks_location: str = Field("api/tasks")
    models_location: str = Field("databases/models")

    class Config:
        """Internal configurations for the container"""

        env_file = ".env"
        env_prefix = "AUTO_LOADER_"
        env_file_encoding = "utf-8"
        case_sensitive = False
