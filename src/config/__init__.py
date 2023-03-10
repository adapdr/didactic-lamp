"""
Module contains standardized config loader and management.
This is implemented using Pydantic for type safety and docker secerts support.
"""
from importlib import import_module
from pathlib import Path

from pydantic import BaseSettings


class ConfigContainer:
    """Class is used as a container for all Configs"""

    def __init__(self) -> None:
        # ? Locate other schema's
        to_load: dict = {}
        for schema in Path("config").iterdir():
            if any(
                [
                    "__" in str(schema),
                    schema.stem == "auto_loader",
                    isinstance(schema, BaseSettings),
                ]
            ):
                continue

            # ? Find required names & properties
            name = schema.stem
            module_name = f"{'config'}/{name}".replace("/", ".")
            schema_container = getattr(
                import_module(module_name), f"{name.capitalize()}Config"
            )

            to_load.update({name.capitalize(): schema_container()})  # ! <--- will work

        # ? Set all SchemaContainer properties
        for key, value in to_load.items():
            setattr(self, key, value)


Config = ConfigContainer()
