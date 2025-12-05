from fastapi import FastAPI
from fastapi.routing import APIRoute

from .config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)