from fastapi import FastAPI, APIRouter

from .predict import router as predict_router


def include_router(app: FastAPI):
    api_router = APIRouter()
    api_router.include_router(predict_router, prefix="/predict", tags=['Predictions'])
    app.include_router(api_router, prefix='/yolo')
