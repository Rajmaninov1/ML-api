from fastapi import APIRouter, status as fapi_status, UploadFile
from fastapi.responses import ORJSONResponse

from config.settings import settings
from predictors.yolo import yolo_predict_img
from schemas.yolo.yolo_img_predictions import YoloImgPredictions

router = APIRouter()


@router.post(
    '/img',
    response_class=ORJSONResponse,
    response_model=YoloImgPredictions,
    status_code=fapi_status.HTTP_200_OK,
)
async def post_yolo_predict_img(file: UploadFile):
    image_bytes = await file.read()
    detections = await yolo_predict_img(image_bytes)
    return YoloImgPredictions(detections=detections)
