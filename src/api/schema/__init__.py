"""Module loads and contains API Schema"""
from importlib import import_module
from pathlib import Path

from config.auto_loader import AutoLoader


class SchemaContainer:
    """Class is used as a container for all API Schemas"""

    def __init__(self) -> None:
        # ? Locate other schema's
        to_load: dict = {}
        for schema in Path(AutoLoader().schema_location).iterdir():
            if any(["__" in str(schema), "generic" in str(schema)]):
                continue

            # ? Find required names & properties
            name = schema.stem
            module_name = f"{AutoLoader().schema_location}/{name}".replace("/", ".")
            schema_container = getattr(
                import_module(module_name), f"{name.capitalize()}Schema"
            )
            to_load.update({name.capitalize(): schema_container})

        # ? Set all SchemaContainer properties
        for key, value in to_load.items():
            setattr(self, key, value)


Schema = SchemaContainer()
