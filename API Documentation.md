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
- **Description**: Stores image file after request as bytes strings file (`*.bin`).

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

### face_facial_attribute Table
- **Fields**:
  - `id`: INT(11), NOT NULL, Primary Key, AUTO_INCREMENT
  - `image_name`: VARCHAR(255), NOT NULL
  - `emotions` : VARCHAR(255), NOT NULL
  - `ages`: VARCHAR(255), NOT NULL
  - `gender`: VARCHAR(255), NOT NULL
  - `created_at`: TIMESTAMP, NOT NULL, Default: current_timestamp()
- **Description**: Stores information about detected face emotions.

### face_verified Table
- **Fields**:
  - `id`: INT(11), NOT NULL, Primary Key, AUTO_INCREMENT
  - `image_name`: VARCHAR(255), NOT NULL
  - `verify_status`: VARCHAR(255), NOT NULL
  - `created_at`: TIMESTAMP, NOT NULL, Default: current_timestamp()
- **Description**: Stores information about face verification status of the image with face's name.

### face_metadata Table
- **Fields**:
  - `id`: INT(11), NOT NULL, Primary Key, AUTO_INCREMENT
  - `image_name`: VARCHAR(255), NOT NULL
  - `image_file`: LONGBLOB, NULL
  - `face_name`: VARCHAR(255), NULL
  - `face_location`: VARCHAR(255), NULL
  - `emotions` : VARCHAR(255), NULL
  - `ages`: VARCHAR(255), NULL
  - `gender`: VARCHAR(255), NULL
  - `verify_status`: VARCHAR(255), NULL
  - `created_at`: TIMESTAMP, NOT NULL, Default: current_timestamp()
- **Description**: Summarizes and store the image's most important face metadata information from the `image` table, the `face_location` table, the `face_verified` table, and the `face_emotions` table.

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
  - `objects_name`: VARCHAR(255), NOT NULL
  - `objects_location_boxes`: VARCHAR(500), NOT NULL
  - `objects_location_weights`: VARCHAR(255), NOT NULL
  - `created_at`: TIMESTAMP, NOT NULL, Default: current_timestamp()
- **Description**: Stores information about multiple detected objects.

## Model - Library
### `face-recognition` library
- **Library name**: face-recognition
- **Version**: 1.3.0
- **Install command line**:`pip install face-recognition`
- **import syntax**:`import face_recognition`
- **Project documentation**: https://pypi.org/project/face-recognition/

### `DeepFace` library
- **Library name**: DeepFace
- **Version**: 0.0.79
- **Install command line**:`pip install deepface`
- **import syntax**:`from deepface import DeepFace`
- **Project documentation**: https://pypi.org/project/deepface/

### `Yolo v8 nano` model
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
- **Example Response**: 
  - [{ 
    - "detections": [{
      - "box": [
                        400.51749,
                        268.44345,
                        403.30487,
                        465.74261
                    ],
      - "weight": 0.92163 }],
    - "image_name": "mot-so-hinh-anh-ve-rei.jpg"},
    
    - {
         "message": "Human location metadata of mot-so-hinh-anh-ve-rei.jpg saved successfully"
     }
  - ]

### Multiple Objects Detection
- **Prefix**: `/m_objects`
- **Endpoint**: `m_objects_location`
- **Method**: POST
- **Description**: Detect object locations in images, classify into different categories
- **Example Response**:
    - [{ 
    - "detections": [{
      - "box": [
                        400.51749,
                        268.44345,
                        403.30487,
                        465.74261
                    ],
      - "object type": "person", "weight": 0.92163 },
    - {
      - "box": [
                        192.27647,
                        438.57233,
                        69.00922,
                        133.88718
                    ],
      - "object type": "bottle", "weight": 0.53189 }]
    - "image_name": "mot-so-hinh-anh-ve-rei.jpg"}, 
  - {
       "message": "Human location metadata of mot-so-hinh-anh-ve-rei.jpg saved successfully"
   }
  - ]
### Face Location
- **Prefix**:`/face`
- **Endpoint**: `/face_location`
- **Method**: POST
- **Description**: Detect face locations in images
- **Example Response**: 
  - [
     - {
        "face_locations": [
       [
                724,
                2853,
                1682,
                1895
            ]
    ],
      -  "image_name": "newjeans-hyein-4k-wallpaper-uhdpaper.com-8960g.jpg"
    },
    - {
    "message": "Face location metadata of newjeans-hyein-4k-wallpaper-uhdpaper.com-8960g.jpg saved successfully"}
  - ]

### Face Landmarks
- **Prefix**:`/face`
- **Endpoint**: `/face_landmarks`
- **Method**: POST
- **Description**: Encode face landmarks to an array
- **Response**:
  - [{
      -  "image_name": "1655923786906.jpeg",
      -  "landmarks": [...] ` (Avg: 5000 - 50000 line of face landmark) `
    - {
        "message": "Face metadata of 1655923786906.jpeg saved successfully"
    }
  - ]

### Facial Attribute Recognition
- **Prefix**:`/face`
- **Endpoint**: `/facial_attribute_recognition`
- **Method**: POST
- **Description**: Recognize ages, gender and emotions and save emotions metadata to the database.
- **Example Response**:
  - [{
     -   "age": [
            "27 - 32"
        ],
    -    "emotions": [
            "neutral"
        ],
    -    "gender": [
            "Woman"
        ],
    -    "image_name": "210328-IU-Coin-LILAC-at-Inkigayo-documents-72.jpeg"
    },
      - {
          "message": "Face emotions metadata of 210328-IU-Coin-LILAC-at-Inkigayo-documents-72.jpeg saved successfully"
  - }]

### Face Verification
- **Prefix**:`/face`
- **Endpoint**: `/face_verify`
- **Method**: POST
- **Description**: Get the `image_data` from the `image` table as `known_face`, compare `known_face` with `unknown_face` and save face verification status and face's name to the database.
- **Example Response**:
  - {
    - "Name": "Rei",
    - "face_verification": "verified",
    - "image_name": "mot-so-hinh-anh-ve-rei.jpg"
  - }

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
- **NO_FACE_NAME**
  - HTTP Code: `404 Not Found`
  - Code: "i04" 
  - Message: Face's name required
### Database code status - dXX
- **DATABASE_IS_NONE**
  - HTTP Code: `503 Service Unavailable`
  - Code: "d01"
  - Message: Can not connect to the database
- **OUTPUT_TOO_LONG**
  - HTTP Code: `413 Payload Too Large`
  - Code: "d02"
  - Message: Output data too large!!!

## Usage
### Human Detection
- To detect human locations, upload the `image` and make a POST request to `{prefix}` `/human_location`. 
- The image will save in `image` table
- The metadata will save in `human_location` table
- Results can be rounded to `n` numbers after the comma. `n` can be edited at the variable `round_result`
- You can customize the `humman_detection` to other type of object detection by change the values of `label_class` (The object class at: https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco.yaml)

### Multiple Objects Detection
- To detect objects, upload the `image` and make a POST request to `{prefix}` `/objects_location`. 
- The image will save in `image` table
- The metadata will save in `detected_objects` table
- Results can be rounded to `n` numbers after the comma. `n` can be edited at the variable `round_result`
- The list of object can be detected at: https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco.yaml

### Face Location
- To detect face locations, upload the `image` and make a POST request to `{prefix}` `/face_location`.
- The image will save in `image` table
- The metadata will save in `face_location` table

### Face Landmarks
- To encode face landmarks, upload the `image` and make a POST request to `{prefix}` `/face_landmarks`. 
- The image will save in `image` table
- The metadata will save in `face_landmarks` table

### Facial Attribute Recognition
- To recognize face facial attribute, upload the `image` and make a POST request to `{prefix}` `/facial_attribute_recognition`. 
- The image will save in `image` table
- The metadata will save in `face_facial_attribute` table
- The list of emotions can be detected: `angry`, `disgust`, `fear`, `happy`, `sad`, `surprise`, `neutral`
- The algorithm returns a range of numbers predicting the age of the image
- The gender will return `Man` or `Woman` only

### Face Verification
- To verify face, upload the `image`, input the `face_name` and make a POST request to `{prefix}` `/face_verify`. 
- The face verification status and face's name will save in `face_verified` table
- The `compare_face_tolerance` is max acceptable distance. It can be config in `config.ini`
- The `fast_compare_face_tolerance` is min accepted's distance. It can be config in `config.ini`
- The face verification status will return `not verified` or `verified` only

## Config
### [db_config]
- host = 0.0.0.0
- port = 1102
- db_host = localhost
- db_user = root
- db_password = []
- db_name = metadata

### [db_limit_config]
- face_locations = 250
- landmarks = 250
- face_name = 250
- objects_detected_boxes = 490
- emotions = 250

### [function_config]
- path = png, jpg, jpeg
- face_prefix = /face
- objects_prefix = /objects
- multiple_objects_prefix = /m_objects
- compare_face_tolerance = 0.42
- fast_compare_face_tolerance = 0.23
- upsample_image = 1

### [human_detection_config]
- model_path = model/yolov8n.pt
- round_result = 5
- label_class = 0

### [objects_detection_config]
- model_path =../../model/yolov8n.pt
- round_result = 5