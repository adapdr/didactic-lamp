"""Module loads and contains API Routers"""
from importlib import import_module
from pathlib import Path
from typing import List

from fastapi import APIRouter

from config.auto_loader import AutoLoader

APIRouters: List[APIRouter] = []

# ? Add routers from ROUTERS_LOCATION -> ROUTERS
for router in Path(AutoLoader().routers_location).iterdir():
    if "__" in str(router):
        continue

    APIRouters.append(import_module(f"api.routers.{router.stem}").router)
