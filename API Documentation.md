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
### face_location Table
- **Fields**:
  - `id`: INT, NOT NULL, Primary Key
  - `image_name`: VARCHAR(255), NOT NULL
  - `face_location`: VARCHAR(255), NOT NULL
  - `created_at`: TIMESTAMP, NOT NULL, Default: current_timestamp()
- **Description**: Stores information about detected face locations.

### face_landmark Table
- **Fields**:
  - `id`: INT, NOT NULL, Primary Key
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

### human_location Table
- **Fields**:
  - `id`: INT, NOT NULL, Primary Key
  - `image_name`: VARCHAR(255), NOT NULL
  - `human_location_boxes`: VARCHAR(500), NOT NULL
  - `human_location_weights`: VARCHAR(255), NOT NULL
  - `created_at`: TIMESTAMP, NOT NULL, Default: current_timestamp()
- **Description**: Stores information about detected human locations.

## Model - Library
### Face detection and face landmarks detection
- **Library name**: face-recognition
- **Version**: 1.3.0
- **Install command line**:`pip install face-recognition`
- **import syntax**:`import face_recognition`
- **Project documentation**: https://pypi.org/project/face-recognition/

### Human detection
- **Model name**: YOLO
- **Version**: v8 nano
- **Install command line**:`pip install ultralytics` 
- **import syntax**:`from ultralytics import YOLO`
- **Project documentation**: https://docs.ultralytics.com/

## Schema
- **Datafield**: `image`(str)
- **Datatype**: `png`, `jpg`, `jpeg`(str) - Can be config in `config.ini`
- **Mandatory**: `True` (bool)

## Endpoints
### Human Detection
- **Prefix**:`/objects`
- **Endpoint**: `/human_location`
- **Data**: `image`
- **Method**: POST
- **Description**: Detect human locations in images and save metadata to the database.
- **Response**: List of detected human locations.

### Face Location
- **Prefix**:`/face`
- **Endpoint**: `/face_location`
- **Data**: `image`
- **Method**: POST
- **Description**: Detect face locations in images and save metadata to the database.
- **Response**: List of detected face locations.

### Face Landmarks
- **Prefix**:`/face`
- **Endpoint**: `/face_landmarks`
- **Data**: `image`
- **Method**: POST
- **Description**: Encode face landmarks to an array and save metadata to the database.
- **Response**: List of encoded face landmarks.

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
  - Message: Can not connect to thw database

## Usage
### Human Detection
- To detect human locations, upload the `image` and make a POST request to `{prefix}` `/human_location`. The metadata will save in the `human_location Table`
- Results can be rounded to `n` numbers after the comma. `n` can be edited at the variable `round_result` (default `round_result = 3`)
- You can customize the `humman_detection` to other type of object detection by change the values of `label_class` (The object class at: https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco.yaml)
### Face Location
- To detect face locations, upload the `image` and make a POST request to `{prefix}` `/face_location`. The metadata will save in the `face_location Table`

### Face Landmarks
- To encode face landmarks, upload the `image` and make a POST request to `{prefix}` `/face_landmarks`. The metadata will save in the `face_landmarks Table`

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