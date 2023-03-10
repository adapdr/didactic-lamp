"""Module loads and contains API Services"""
from importlib import import_module
from pathlib import Path

from config.auto_loader import AutoLoader


class ServiceContainer:
    """Class is used as a container for all API Services"""

    def __init__(self) -> None:
        # ? Locate other services
        to_load: dict = {}
        for service in Path(AutoLoader().services_loaction).iterdir():
            if "__" in str(service):
                continue

            name = service.stem
            module_name = f"{AutoLoader().services_loaction}/{name}".replace("/", ".")
            service_container = getattr(
                import_module(module_name), f"{name.capitalize()}Service"
            )
            to_load.update({name.capitalize(): service_container})

        # ? Set all ServiceContainer properties
        for key, value in to_load.items():
            setattr(self, key, value)


Services = ServiceContainer()
