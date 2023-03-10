"""
Main Application file

Used as target when running the ASGI server
ex: `uvicorn main:app --reload` from `src/`
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.routers import APIRouters
from config import Config

# Initialize application with configs
app = FastAPI(**Config.Api.dict())

# Mount & serve the frontend
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Add the routers
[app.include_router(router) for router in APIRouters]
