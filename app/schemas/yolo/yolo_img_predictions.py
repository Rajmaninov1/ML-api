from pydantic import BaseModel


class ImgCoords(BaseModel):
    x_min: float
    y_min: float
    x_max: float
    y_max: float


class Detection(BaseModel):
    detection_type: str
    confidence: float
    bbox: ImgCoords


class YoloImgPredictions(BaseModel):
    detections: list[Detection]
