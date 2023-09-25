# API Documentation

## Introduction
This documentation outlines the endpoints, requests, and responses for the Camera API. It also includes information about the database tables used to store the API responses.

## Base URL
`http://localhost:1102`

## Database Information
- **Database Host**: localhost or 127.0.0.1
- **Database Name**: metadata
- **Database User**: root
- **Database Password**: No password required

## Database Tables
### image Table
- **Fields**:
  - `id`: INT(11), NOT NULL, Primary Key, AUTO_INCREMENT
  - `image_name`: VARCHAR(255), NOT NULL
  - `image_file`: LONGBLOB, NOT NULL
  - `created_at`: TIMESTAMP, NOT NULL, Default: current_timestamp()
- **Description**: Stores image file after request as base64 file (`*.bin`).

### face_location Table
- **Fields**:
  - `id`: INT(11), NOT NULL, Primary Key, AUTO_INCREMENT
  - `image_name`: VARCHAR(255), NOT NULL
  - `face_location`: VARCHAR(255), NOT NULL
  - `created_at`: TIMESTAMP, NOT NULL, Default: current_timestamp()
- **Description**: Stores information about detected face locations.

### face_landmark Table
- **Fields**:
  - `id`: INT(11), NOT NULL, Primary Key, AUTO_INCREMENT
  - `image_name`: VARCHAR(255), NOT NULL
  - `bottom_lip`: VARCHAR(255), NOT NULL
  - `chin`: VARCHAR(255), NOT NULL
  - `left_eye`: VARCHAR(255), NOT NULL
  - `left_eyebrow`: VARCHAR(255), NOT NULL
  - `nose_bridge`: VARCHAR(255), NOT NULL
  - `nose_tip`: VARCHAR(255), NOT NULL
  - `right_eye`: VARCHAR(255), NOT NULL
  - `right_eyebrow`: VARCHAR(255), NOT NULL
  - `top_lip`: VARCHAR(255), NOT NULL
  - `created_at`: TIMESTAMP, NOT NULL, Default: current_timestamp()
- **Description**: Stores information about detected face landmarks.
### face_emotions Table
- **Fields**:
  - `id`: INT(11), NOT NULL, Primary Key, AUTO_INCREMENT
  - `image_name`: VARCHAR(255), NOT NULL
  - `face_location`: VARCHAR(255), NOT NULL
  - `created_at`: TIMESTAMP, NOT NULL, Default: current_timestamp()
  - `emotions` : VARCHAR(50), NOT NULL
  - `emotion_weights`: VARCHAR(255), NOT NULL
  - `created_at`: TIMESTAMP, NOT NULL, Default: current_timestamp()
  - 
### human_location Table
- **Fields**:
  - `id`: INT(11), NOT NULL, Primary Key, AUTO_INCREMENT
  - `image_name`: VARCHAR(255), NOT NULL
  - `human_location_boxes`: VARCHAR(500), NOT NULL
  - `human_location_weights`: VARCHAR(255), NOT NULL
  - `created_at`: TIMESTAMP, NOT NULL, Default: current_timestamp()
- **Description**: Stores information about detected human locations.

### detected_objects Table
- **Fields**:
  - `id`: INT(11), NOT NULL, Primary Key, AUTO_INCREMENT
  - `image_name`: VARCHAR(255), NOT NULL
  - `objects_name`: VARCHAR(50), NOT NULL
  - `objects_location_boxes`: VARCHAR(255), NOT NULL
  - `objects_location_weights`: VARCHAR(255), NOT NULL
  - `created_at`: TIMESTAMP, NOT NULL, Default: current_timestamp()
- **Description**: Stores information about detected objects.
## Model - Library
### Face detection and face landmarks detection
- **Library name**: face-recognition
- **Version**: 1.3.0
- **Install command line**:`pip install face-recognition`
- **import syntax**:`import face_recognition`
- **Project documentation**: https://pypi.org/project/face-recognition/

### Emotions recognition
- **Library name**: DeepFace
- **Version**: 0.0.79
- **Install command line**:`pip install deepface`
- **import syntax**:`from deepface import DeepFace`
- **Project documentation**: https://pypi.org/project/deepface/

### Human detection and Multiple objects detection
- **Model name**: YOLO
- **Version**: v8 nano
- **Install command line**:`pip install ultralytics` 
- **import syntax**:`from ultralytics import YOLO`
- **Project documentation**: https://docs.ultralytics.com/

## Schema
- **Datafield**: `image`(str)
- **Datatype**: `png`, `jpg`, `jpeg`(str) - Can be config at `config.ini`
- **Mandatory**: `True` (bool)

## Endpoints
### Human Detection
- **Prefix**:`/objects`
- **Endpoint**: `/human_location`
- **Method**: POST
- **Description**: Detect human locations in images
- **Response**: 
  - `{'image_name', 'detections': [{'box', 'weight'}`
  - "Human location metadata of `image_name` saved successfully"

### Multiple Objects Detection
- **Prefix**: `/m_objects`
- **Endpoint**: `m_objects_location`
- **Method**: POST
- **Description**: Detect object locations in images, classify into different categories
- **Response**:
  - `{'image_name', 'detections': [{'object type', 'box', 'weight'}`
  - "Multiple objects location metadata of `image_name` saved successfully"

### Face Location
- **Prefix**:`/face`
- **Endpoint**: `/face_location`
- **Method**: POST
- **Description**: Detect face locations in images
- **Response**: 
  - `{'image_name', face_locations'}`
  - "Face location metadata of `image_name` saved successfully"

### Face Landmarks
- **Prefix**:`/face`
- **Endpoint**: `/face_landmarks`
- **Method**: POST
- **Description**: Encode face landmarks to an array
- **Response**:
  - `{'image_name', 'landmarks'}`
  - "Face metadata of `image_name` saved successfully"

### Emotions Recognition
- **Prefix**:`/face`
- **Endpoint**: `/emotions_recognition`
- **Method**: POST
- **Description**: Get the `face_locations` metadata of the images, recognize emotions and save emotions metadata to the database.
- **Response**:
  - `{'image_name','face_locations','emotions':[{'dominant_emotion': face['dominant_emotion'], 'emotion_weights': face['emotion']}`
  - "Face emotions metadata of `image_name` saved successfully"

## Error Handle
### Image code status - iXX
- **INVALID_IMAGE** 
  - HTTP Code: `415 Unsupported Media Type`
  - Code: "i01"
  - Message: Invalid image file format
- **NO_IMAGE**
  - HTTP Code: `404 Not Found`
  - Code: "i02"
  - Message: No image file uploaded
- **NO_DETECTION**
  - HTTP Code: `404 Not Found`
  - Code: "i03" 
  - Message: Nothing was detected
### Database code status - dXX
- **DATABASE_IS_NONE**
  - HTTP Code: `503 Service Unavailable`
  - Code: "d01"
  - Message: Can not connect to the database
- **OUTPUT_TOO_LONG**
  - HTTP Code: `413 Payload Too Large`
  - Code: "d02"
  - Message: Output data  too large!!!

## Usage
### Human Detection
- To detect human locations, upload the `image` and make a POST request to `{prefix}` `/human_location`. 
- The image will save in `image` table
- The metadata will save in `human_location` table
- Results can be rounded to `n` numbers after the comma. `n` can be edited at the variable `round_result` (default `round_result = 3`)
- You can customize the `humman_detection` to other type of object detection by change the values of `label_class` (The object class at: https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco.yaml)

### Multiple Objects Detection
- To detect objects, upload the `image` and make a POST request to `{prefix}` `/objects_location`. 
- The image will save in `image` table
- The metadata will save in `detected_objects` table
- Results can be rounded to `n` numbers after the comma. `n` can be edited at the variable `round_result` (default `round_result = 3`)
- The list of object can be detected at: https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco.yaml

### Face Location
- To detect face locations, upload the `image` and make a POST request to `{prefix}` `/face_location`.
- The image will save in `image` table
- The metadata will save in `face_location` table

### Face Landmarks
- To encode face landmarks, upload the `image` and make a POST request to `{prefix}` `/face_landmarks`. 
- The image will save in `image` table
- The metadata will save in `face_landmarks` table

### Emotions Recognition
- To recognize face emotions, upload the `image` and make a POST request to `{prefix}` `/emotions_recognition`. 
- The image will save in `image` table
- The metadata will save in `face_emotions` table
- The list of emotions can be detected: `angry`, `disgust`, `fear`, `happy`, `sad`, `surprise`, `neutral`

## Config
### [db_config]
- host = 0.0.0.0
- port = 1102
- db_host = localhost
- db_user = root
- db_password = []
- db_name = metadata
### [function_config]
- path = png, jpg, jpeg
- face_prefix = /face
- objects_prefix = /objects
### [human_detection_config]
- model_path = model/yolov8n.pt
- round_result = 3
- label_class = 0
[objects_detection_config]
- model_path =../../model/yolov8n.pt
- round_result = 3