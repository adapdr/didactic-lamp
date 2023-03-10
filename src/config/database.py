"""
File contains DATABASE configurations
"""
from pathlib import Path
from typing import Union

from masoniteorm.connections import ConnectionResolver
from pydantic import BaseSettings, Field, root_validator


class Database(BaseSettings):
    """
    Partial used by the DatabaseConfig container providing
    the main configuration used to initilize the DB.
    """

    host: str = Field(None)
    port: int = Field(None)
    database: Union[str, Path] = Field(...)

    driver: str = Field(...)
    driver_default: str = Field(...)
    log_queries: bool = Field(None)

    user: str = Field(...)
    password: str = Field(...)
    root_user: str = Field(None)
    root_password: str = Field(None)

    class Config:
        """
        Internal configuration for the container
        """

        env_file = ".env"
        env_prefix = "DB_"
        env_file_encoding = "utf-8"
        case_sensitive = False


class DatabaseConfig(BaseSettings):
    """
    Container for all Database configs
    """

    databases: dict = Database()

    @root_validator()
    def parse_to_orm_format(cls, values):
        """
        Organizing the settings in the way expected by the ORM.

        This is is a non-breaking constraint of the current version
        and will be addressed in a future release.
        """
        _copy: dict = values.copy()
        _default = _copy["databases"].pop("driver_default")
        values["databases"] = {
            "default": _default,
            _default: _copy["databases"],
        }
        return values


DB = ConnectionResolver().set_connection_details(DatabaseConfig().databases)
