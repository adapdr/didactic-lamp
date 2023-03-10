"""Module loads and contains API Tasks"""
from importlib import import_module
from pathlib import Path

from config.auto_loader import AutoLoader


class TasksContainer:
    """Class is used as a container for all API Tasks"""

    def __init__(self) -> None:
        # ? Locate other schema's
        to_load: dict = {}
        for service in Path(AutoLoader().tasks_location).iterdir():
            if "__" in str(service):
                continue

            # ? Find required names & properties
            name = service.stem
            module_name = f"{AutoLoader().tasks_location}/{name}".replace("/", ".")
            to_load.update(
                {
                    name.capitalize(): getattr(
                        import_module(module_name), f"{name.capitalize()}Tasks"
                    )
                }
            )

        # ? Set all TasksContainer properties
        for key, value in to_load.items():
            setattr(self, key, value)


Tasks = TasksContainer()
