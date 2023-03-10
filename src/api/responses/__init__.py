"""Module loads and contains API Responses"""
from importlib import import_module
from pathlib import Path

from config.auto_loader import AutoLoader


class ResponsesContainer:
    """Class is used as a container for all API Responses"""

    def __init__(self) -> None:
        # ? Locate all responses
        to_load: dict = {}
        for responses in Path(AutoLoader().responses_location).iterdir():
            if "__" in str(responses):
                continue
            name = responses.stem
            module = f"{AutoLoader().responses_location}/{name}".replace("/", ".")
            to_load.update(
                {
                    name.capitalize(): getattr(
                        import_module(module), f"{name.capitalize()}Responses"
                    )
                }
            )

        # ? Set all Responses properties
        for key, value in to_load.items():
            setattr(self, key, value)


Responses = ResponsesContainer()
