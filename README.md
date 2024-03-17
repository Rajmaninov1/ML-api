## FastAPI ML Model Server README

### Introduction
This FastAPI application serves as a REST API for utilizing multiple machine learning models, primarily focused on object detection tasks. The current version, 1.0.0, integrates YOLOv8 for detecting objects in images. 

### Usage
1. **Installation**: Clone this repository and install the required dependencies.
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    pip install -r requirements.txt
    ```

2. **Starting the Server**: Run main.py.

    - The server will start on `http://localhost:8000` by default.

3. **Using the API**: 
    - Endpoint: `/yolo/predict/img`
    - Method: `POST`
    - Input: 
        - Content-Type: `multipart/form-data`
        - Body: Image file (`image/jpeg`, `image/png`, etc.)
    - Output:
        - JSON response containing detected objects in the image.
    
    Example using `curl`:
    ```bash
    curl -X POST -F "file=@/path/to/image.jpg" http://localhost:8000/yolo/predict/img
    ```

### Endpoint
- **Path**: `/yolo/predict/img`
- **Method**: POST
- **Description**: Detects objects in the provided image using YOLOv8.
- **Request Body**:
    - **Content-Type**: `multipart/form-data`
    - **Body**: Image file (`image/jpeg`, `image/png`, etc.)
- **Response**:
    - **Content-Type**: `application/json`
    - **Body**: JSON response containing detected objects.

### Example Response
```json
{
  "detections": [
    {
      "detection_type": "car",
      "confidence": 0.95,
      "bbox": {
        "x_min": 249.17129516601562,
        "y_min": 698.0484008789062,
        "x_max": 424.1062927246094,
        "y_max": 883.6032104492188
      }
    },
    {
      "detection_type": "person",
      "confidence": 0.88,
      "bbox": {
        "x_min": 1261.3177490234375,
        "y_min": 629.70947265625,
        "x_max": 1375.2801513671875,
        "y_max": 888.2861328125
      }
    },
    ...
  ]
}
```

### Dependencies
- FastAPI
- uvicorn
- Pydantic
- YOLOv8 (pretrained weights)

### Future Work
- Integration of more machine learning models for various tasks.
- Improved error handling and logging.
- API documentation generation using Swagger UI or Redoc.

### Contributors
- Rajmaninov1
- 8.8tolosajulian@gmail.com

### License
This project is licensed under the [MIT License](LICENSE).