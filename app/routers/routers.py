from fastapi import FastAPI

from .yolo.router import include_router as yolo_include_router


def add_routers(app: FastAPI) -> None:
    yolo_include_router(app)
