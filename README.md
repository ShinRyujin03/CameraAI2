# API Documentation

## Table of Contents

- [Introduction](#introduction)
- [Quick Guide](#quick-guide)
    - [Pre-requisites](#pre-requisites)
    - [Installation](#installation)
    - [Running the Application](#running-the-application)
    - [API Usage](#api-usage)
- [Default Database Information ](#default-database-information)
- [Database Tables](#database-tables)
    - [`image` Table](#image-table)
    - [`face_location` Table](#face_location-table)
    - [`face_landmark` Table](#face_landmark-table)
    - [`face_facial_attribute` Table](#face_facial_attribute-table)
    - [`face_verified` Table](#face_verified-table)
    - [`face_metadata` Table](#face_metadata-table)
    - [`human_location` Table](#human_location-table)
    - [`detected_objects` Table](#detected_objects-table)
- [Model - Library](#model---library)
    - [`face-recognition` library](#face-recognition-library)
    - [`DeepFace` library](#deepface-library)
    - [`Yolo v8 nano` model](#yolo-v8-nano-model)
- [Image Schema](#image-schema)
- [Endpoints](#endpoints)
    - [Human Detection](#human-detection)
    - [Multiple Objects Detection](#multiple-objects-detection)
    - [Face Location](#face-location)
    - [Face Landmarks](#face-landmarks)
    - [Facial Attribute Recognition](#facial-attribute-recognition)
    - [Face Verification](#face-verification)
    - [Name Recognition](#name-recognition)
- [Endpoint Usage](#endpoint-usage)
- [Results visualize test](#results-visualize-test)
    - [Face Location Test](#face-location-test)
    - [Number of Face Image Test](#number-of-face-image-test)
- [Error Handle](#error-handle)
    - [Image code status - iXX](#image-code-status---ixx)
    - [Face name code status - fXX](#face-name-code-status---fxx)
    - [Database code status - dXX](#database-code-status---dxx)
- [Config](#config)

## Introduction

- The CameraAI2 project is a computer vision application designed to perform various tasks such as face detection,
  recognition, and object detection.
- This documentation outlines the endpoints, requests, and responses for this API with quick guide to help you set up
  and run the project. It also includes information about the database tables used to store the API responses.

## Quick Guide

### Pre-requisites

- Python: Python 3 (recommend: 3.10+)
### Installation

1. Clone the project from the repository:

    ```bash
    git clone https://github.com/ShinRyujin03/CameraAI2.git
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3.10 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database by run SQL script:
    ```
   database/metadata.sql
    ```

### Running the Application

1. Start the application using the provided run script:

    ```
    /app/main/run.py
    ```

2. The application will start, and you can now access the API at `http://localhost:1102` or http://127.0.0.1:1102.

### API Usage

#### Sending Requests

- Use tools like `curl`, `Postman`, or your preferred HTTP client to send requests to the API endpoints.
  See the [Endpoint Usage](#endpoint-usage) for more information

![Ảnh màn hình 2023-11-01 lúc 14.49.21.png](database/image/README.md%20image/API%20input.png)

#### Sending Image Files

- When sending image files, ensure they are in one of the supported formats: PNG, JPG, or JPEG. You can configure it
  at `path` in `config.ini`

#### API Responses

- The API returns JSON responses containing the requested data or error messages.
  See the [Endpoints](#endpoints) and [Error Handle](#error-handle) for more information

## Default Database Information

- **Database Host**: localhost or 127.0.0.1
- **Database Port**: 1102
- **Database Name**: metadata
- **Database User**: root
- **Database Password**: No password required

## Database Tables

### image Table

- **Fields**:
    - `id`: INT(11), NOT NULL, Primary Key, AUTO_INCREMENT
    - `image_name`: VARCHAR(255), NOT NULL
    - `image_file`: MEDIUMBLOB, NOT NULL
    - `created_at`: TIMESTAMP, NOT NULL, Default: current_timestamp()
- **Description**: Stores image file after request as bytes strings file (`*.bin`).

### face_location Table

- **Fields**:
    - `id`: INT(11), NOT NULL, Primary Key, AUTO_INCREMENT
    - `image_name`: VARCHAR(255), NOT NULL
    - `face_location`: VARCHAR(255), NOT NULL
    - `created_at`: TIMESTAMP, NOT NULL, Default: current_timestamp()
- **Description**: Stores results of the `face detection` endpoint.

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
- **Description**: Stores results of the `face landmarks detection` endpoint.

### face_facial_attribute Table

- **Fields**:
    - `id`: INT(11), NOT NULL, Primary Key, AUTO_INCREMENT
    - `image_name`: VARCHAR(255), NOT NULL
    - `emotions` : VARCHAR(255), NOT NULL
    - `ages`: VARCHAR(255), NOT NULL
    - `gender`: VARCHAR(255), NOT NULL
    - `created_at`: TIMESTAMP, NOT NULL, Default: current_timestamp()
- **Description**: Stores results of the `facial attribute recognition` endpoint.

### face_verified Table

- **Fields**:
    - `id`: INT(11), NOT NULL, Primary Key, AUTO_INCREMENT
    - `image_name`: VARCHAR(255), NOT NULL
    - `verify_status`: VARCHAR(255), NOT NULL
    - `created_at`: TIMESTAMP, NOT NULL, Default: current_timestamp()
- **Description**: Stores results of the `face verification` endpoint

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
- **Description**: Summarizes and store the image's most important face metadata information from the `image` table,
  the `face_location` table, the `face_verified` table, and the `face_facial_attribute` table.

### human_location Table

- **Fields**:
    - `id`: INT(11), NOT NULL, Primary Key, AUTO_INCREMENT
    - `image_name`: VARCHAR(255), NOT NULL
    - `human_location_boxes`: VARCHAR(500), NOT NULL
    - `human_location_weights`: VARCHAR(255), NOT NULL
    - `created_at`: TIMESTAMP, NOT NULL, Default: current_timestamp()
- **Description**: Stores results of the `human detection` endpoint

### detected_objects Table

- **Fields**:
    - `id`: INT(11), NOT NULL, Primary Key, AUTO_INCREMENT
    - `image_name`: VARCHAR(255), NOT NULL
    - `objects_name`: VARCHAR(255), NOT NULL
    - `objects_location_boxes`: VARCHAR(500), NOT NULL
    - `objects_location_weights`: VARCHAR(255), NOT NULL
    - `created_at`: TIMESTAMP, NOT NULL, Default: current_timestamp()
- **Description**: Stores results of the `multiple objects detection` endpoint

## Model - Library

### `face-recognition` library

- **Library name**: face-recognition
- **Version**: 1.3.0
- **Install command line**:
    ```bash
    pip install face-recognition
    ```
- **import syntax**:
    ```python lines
    import face_recognition
    ```
- **Project documentation**: https://pypi.org/project/face-recognition/

### `DeepFace` library

- **Library name**: DeepFace
- **Version**: 0.0.79
- **Install command line**:
    ```bash
    pip install deepface
    ```
- **import syntax**:
    ```python lines
    from deepface import DeepFace
    ```
- **Project documentation**: https://pypi.org/project/deepface/

### `Yolo v8 nano` model

- **Model name**: YOLO
- **Version**: v8 nano
- **Install command line**:
    ```bash
    pip install ultralytics
    ```
- **import syntax**:
    ```python lines
    from ultralytics import YOLO
    ```
- **Project documentation**: https://docs.ultralytics.com/

## Image Schema

- **Datafield**: `image`
- **Datatype**: `png`, `jpg`, `jpeg` (str)
- **Mandatory**: `True` (bool)

## Endpoints

- Postman
  workspace: https://www.postman.com/technical-observer-13837837/workspace/cameraai/collection/29180513-362c36ef-6fd3-4f9f-aa98-0976c5cbdb80?action=share&creator=29180513

### Human Detection

- **Prefix**:`/objects`
- **Endpoint**: `/human_location`
- **Method**: POST
- **Description**: Detect human locations in images
- **Example Response**:
    - ***Input***
      ```
      image: "images.jpeg"
      ```
      ![Jiwoo%20md.png](/database/image/README.md%20image/Jiwoo%20md.png)
    - ***Output***
      ```json lines
      [
        {
            "detections": [
                {
                    "box": [
                        1065.94641,
                        717.97485,
                        1340.47827,
                        1270.15039
                    ],
                    "weight": 0.86508
                }
            ],
            "image_name": "Jiwoo.jpg"
        },
        {
            "message": "Human location metadata of Jiwoo.jpg saved successfully"
        }
      ]
        ```
    - ***Back-end messenger***
      ```
      0: 448x640 1 person, 1 laptop, 1 teddy bear, 385.0ms
      Speed: 17.0ms preprocess, 385.0ms inference, 36.6ms postprocess per image at shape (1, 3, 448, 640)
      ```

### Multiple Objects Detection

- **Prefix**: `/m_objects`
- **Endpoint**: `m_objects_location`
- **Method**: POST
- **Description**: Detect object locations in images, classify into different categories
- **Example Response**:
    - ***Input***
      ```
      image: "images.jpeg"
      ```
      ![Ảnh màn hình 2023-11-01 lúc 14.38.03.png](/database/image/README.md%20image/Jiwoo%20md.png)
    - ***Output***
      ```json lines
      [
        {
            "detections": [
                {
                    "box": [
                        1065.94641,
                        717.97485,
                        1340.47827,
                        1270.15039
                    ],
                    "object type": "person",
                    "weight": 0.86508
                },
                {
                    "box": [
                        1101.8562,
                        1254.60352,
                        313.31927,
                        214.42932
                    ],
                    "object type": "teddy bear",
                    "weight": 0.58707
                },
                {
                    "box": [
                        363.354,
                        1222.16138,
                        289.47791,
                        266.88342
                    ],
                    "object type": "laptop",
                    "weight": 0.35285
                }
            ],
            "image_name": "Jiwoo.jpg"
        },
        {
            "message": "Objects detection metadata of Jiwoo.jpg saved successfully"
        }
      ]
      ```
    - ***Back-end messenger***
      ```
      0: 448x640 1 person, 1 laptop, 1 teddy bear, 385.0ms
      Speed: 17.0ms preprocess, 385.0ms inference, 36.6ms postprocess per image at shape (1, 3, 448, 640)
      ```

### Face Location

- **Prefix**:`/face`
- **Endpoint**: `/face_location`
- **Method**: POST
- **Description**: Detect face locations in images
- **Example Response**:
    - ***Input***
      ```
      image: "images.jpeg"
      ```
      ![Ảnh màn hình 2023-11-01 lúc 14.29.14.png](/database/image/README.md%20image/Kazuha%202.png)
    - ***Output***
      ```json lines
      [
        {
            "face_locations": [
                [
                    72,
                    137,
                    146,
                    63
                ]
            ],
            "image_name": "images.jpeg"
        },
        {
            "message": "Face location metadata of images.jpeg saved successfully"
        }
      ]
      ```
    - ***Back-end messenger***
      ```
      Image name: images.jpeg
      Location model used: hog
      ```

### Face Landmarks

- **Prefix**:`/face`
- **Endpoint**: `/face_landmarks`
- **Method**: POST
- **Description**: Encode face landmarks to an array
- **Example Response**:
    - ***Input***
      ```
       image: "ITZY-CHECKMATE-Album-Scans-Yeji-ver-documents-11.jpeg"
      ```
      ![Ảnh màn hình 2023-11-01 lúc 14.23.56.png](database/image/README.md%20image/Yeji%20md.png)
    - ***Output***
   ```json lines
   [
     {
         "image_name": "ITZY-CHECKMATE-Album-Scans-Yeji-ver-documents-11.jpeg",
         "landmarks": [...] //Avg: 5000 - 50000 line of face landmarks
     },
     {
         "message": "Face landmarks of ITZY-CHECKMATE-Album-Scans-Yeji-ver-documents-11.jpeg saved successfully"
     }
   ]
    ```

### Facial Attribute Recognition

- **Prefix**:`/face`
- **Endpoint**: `/facial_attribute_recognition`
- **Method**: POST
- **Description**: Recognize ages, gender and emotions of the image and save these results to the database.
- **Example Response**:
    - ***Input***
      ```
      image: "Wonyoung.jpg"
      ```
      ![Wonyoung md.png](database/image/README.md%20image/Wonyoung%20md.png)
    - ***Output***
       ```json lines
      [
          {
              "age": [
                  "19 - 24"
              ],
              "emotions": [
                  "happy"
              ],
              "gender": [
                  "Woman"
              ],
              "image_name": "Wonyoung.jpg"
          },
          {
              "message": "Face facial attribute metadata of Wonyoung.jpg saved successfully"
          }
      ]
       ```

### Face Verification

- **Prefix**:`/face`
- **Endpoint**: `/face_verify`
- **Method**: POST
- **Description**: Get the `image_file` from the `image` table as `known_face`, compare this `known_face`
  with `unknown_face` and save face verification status and face name to the database.
- **Example Response**:
    - ***Input***
      ```
      face_name: Haewon
      image: "IMG_0587.JPG"
      ```
      ![Ảnh màn hình 2023-11-01 lúc 14.03.30.png](database/image/README.md%20image/Haewon%20md.png)
    - ***Output***
      ```json lines
      {
      "Name": "Haewon",
      "face_verification": "verified",
      "image_name": "IMG_0587.JPG"
      }
      ```
    - ***Back-end messenger***
      ```
      Image name: IMG_0587.JPG
      Known face nums: 178
      Location model used: hog
      Accuracy: High
      Min distance: 0.33201442482600557
      Number of loaded face: 161
      ```

### Name Recognition

- **Prefix**:`/face`
- **Endpoint**: `/face_name_recognition`
- **Method**: POST
- **Description**: Get the `image_file` and `face_name` from the `face_metadata` table as `known_face`, compare
  this `known_face` with `unknown_face` to predict the unknown face name with the corresponding level of accuracy.
- **Example Response**:
    - ***Input***
      ```
      image: "IMG_3716.JPG"
      ```
      ![Rei md.png](/database/image/README.md%20image/Rei%20md.png)
    - ***Output***
      ```json lines
      {
          "accuracy": "Medium",
          "image_name": "IMG_3716.JPG",
          "recognized_face_name": "Rei"
      }
      ```
    - ***Back-end messenger***
      ```
      Image name: IMG_3716.JPG
      Location model used: hog
      high_accuracy_name: None
      medium_accuracy_name: Rei
      low_accuracy_name: None
      Accuracy: Medium
      Min distance: 0.34526925581139395
      ```

## Endpoint Usage

### Human Detection

- To detect human locations, upload the `image` and make a POST request to `{prefix}` `/human_location`.
- The image will save in `image` table
- The metadata will save in `human_location` table
- Results can be rounded to `n` numbers after the comma. `n` can be configuring at the variable `round_result`
- The results are in `xywh` format
- You can configure the `humman_detection` to other type of object detection by change the values of `label_class` (The
  list of object class can be detected
  at: https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco.yaml)

### Multiple Objects Detection

- To detect objects, upload the `image` and make a POST request to `{prefix}` `/objects_location`.
- The image will save in `image` table
- The metadata will save in `detected_objects` table
- Results can be rounded to `n` numbers after the comma. `n` can be configuring at the variable `round_result`
- The results are in `xywh` format
- The list of object can be detected
  at: https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco.yaml

### Face Location

- To detect face locations, upload the `image` and make a POST request to `{prefix}` `/face_location`.
- The image will save in `image` table
- The results are in `xyxy` format
- The metadata will save in `face_location` table

### Face Landmarks

- To encode face landmarks, upload the `image` and make a POST request to `{prefix}` `/face_landmarks`.
- The image will save in `image` table
- The metadata will save in `face_landmarks` table

### Facial Attribute Recognition

- To recognize face facial attribute, upload the `image` and make a POST request
  to `{prefix}` `/facial_attribute_recognition`.
- The image will save in `image` table
- The metadata will save in `face_facial_attribute` table
- The list of emotions can be detected: `angry`, `disgust`, `fear`, `happy`, `sad`, `surprise`, `neutral`
- The algorithm returns a range of numbers predicting the age of the image, It can be configuring at the
  variable `ages_range`
- If the predicted age is different from the actual age, you can minimize the error by configuring `ages_bias`
  in `config.ini`
- Ages calculation formula:
    - age_min = `face['age']` +  `ages_bias`
    - age_max = age_min +  `ages_range`
- The gender will return `Man` or `Woman` only

### Face Verification

- To verify face, upload the `image`, input the `face_name` and make a POST request to `{prefix}` `/face_verify`.
- The face verification status and valid face name will save in `face_verified` table
- The level of accuracy can be configuring in `config.ini`, has 3 level of accuracy are `high`(>98%), `medium`(>=85%)
  and `low`(>60%)
- The face verification status will return `verified` when in `high` level of accuracy only
- The elapsed time can be configuring at `verification_elapsed_time` variable in `config.ini`  (Default = 1m)

### Name Recognition

- To recognize face name, upload the `image` and make a POST request to `{prefix}` `/face_name_recognition`.
- The level of accuracy can be configuring in `config.ini`, has 3 level of accuracy are `high`(>98%), `medium`(>=85%)
  and `low`(>60%)
- The elapsed time can be configuring at `recognition_elapsed_time` variable in `config.ini`  (Default = 45s)

## Results visualize test

### Face Location Test

- **Description**: The Face Location Test is designed to draw rectangles around faces in images to visualize the results of the `face_location` endpoint. Below is the visual representation of the test:
- **Example Result**:
    - ***Input***
       ```  
       image = "image/yujin 4.jpeg"
       face_locations = [(73, 128, 135, 66)] 
       ```
    - ***Output***:    
      ![Ảnh màn hình 2023-11-01 lúc 15.47.52.png](database/image/README.md%20image/Yujin%20md.png)

### Number of Face Image Test

- **Description**:
    - The Number of Face Image Test analyzes the frequency of different face names detected in the dataset. It calculates the occurrence of each face name and provides insights into the distribution. The test also determines the pass and fail counts based on a predefined threshold.
    - The number of images per `face_name` in the database should be greater than or equal
      to `number_of_face_required` (recommended >= 4) to get the highest accuracy
    - You can do the test by running the `numb_face_name_test.py` program at:
    ```bash
    app/services/test/numb_face_name_test.py
    ```

- **Example Result**:
    ```
    Passed faces: Sumin (4 times), Yuna (8 times), Yeji (7 times), Jennie (5 times), NaNa (4 times), Rosé (13 times), Jisoo (5 times), Jiwoo (8 times), Sakura (7 times), Irene (4 times), IU (14 times), Kazuha (6 times), Wonyoung (10 times), Ryujin (10 times), Lisa (11 times), Yujin (7 times), Rei (9 times)
    Failed faces: Lily (2 times), Nayeon (2 times), Test Img (1 times), Chaeyeon (1 times), Hyein (2 times), Lia (3 times), Minji (2 times), Haerin (1 times), Yuqi (2 times), ITZY (2 times), Joy (2 times), Chaeryeong (3 times), Hanni (2 times), IVE (1 times), Haewon (2 times), Tsuki (2 times), Eunchae (3 times), Soyeon (1 times)
    Face Pass: 14
    Face Fail: 21
    ```
  ![Figure_1.png](database/image/README.md%20image/Figure.png)

## Error Handle

### Image code status - iXX

- **INVALID_IMAGE**
    - HTTP Code: `415 Unsupported Media Type`
    - Code: "i01"
    - Message: Invalid image file format. Supported formats are PNG, JPG, and JPEG.
- **NO_IMAGE**
    - HTTP Code: `404 Not Found`
    - Code: "i02"
    - Message: Image not found. Please upload a valid image file.
- **NO_DETECTION**
    - HTTP Code: `404 Not Found`
    - Code: "i03"
    - Message: No face detected in the image. Please upload an image with a visible face.

### Face name code status - fXX

- **NO_FACE_NAME**
    - HTTP Code: `404 Not Found`
    - Code: "f01"
    - Message: Face name not found. Please provide a valid name for the face.
- **INVALID_FACE_NAME**
    - HTTP Code: `406 Not Acceptable`
    - Code: "f02"
    - Message: Invalid image face name. Please provide a valid name for the face.

### Database code status - dXX

- **DATABASE_IS_NONE**
    - HTTP Code: `503 Service Unavailable`
    - Code: "d01"
    - Message: Unable to establish a connection with the database. Please try again later.
- **OUTPUT_TOO_LONG**
    - HTTP Code: `413 Payload Too Large`
    - Code: "d02"
    - Message: Output size exceeds the maximum allowed limit. Please upload a less complex image.

## Config

### [db_config]

```ini
host = 0.0.0.0
port = 1102
db_host = localhost
db_user = root
db_password =
db_name = metadata
```

### [db_limit_config]

```ini
face_locations = 250
landmarks = 250
face_name = 250
objects_detected_boxes = 490
emotions = 250
```

[function_config]
```ini
path = png, jpg, jpeg
face_prefix = /face
objects_prefix = /objects
multiple_objects_prefix = /m_objects
```

[face_detection_config]
```ini
upsample_image = 1
```

[age_config]
```ini
ages_bias = -9
ages_range = 5
```
[verification_config]
```ini
low_accuracy_verification = 0.48
medium_accuracy_verification = 0.44
high_accuracy_verification = 0.35
verification_elapsed_time = 60
delta_dist = 0.03
```

[name_recognition_config]
```ini
low_accuracy_recognition = 0.46
medium_accuracy_recognition = 0.42
high_accuracy_recognition = 0.33
recognition_elapsed_time = 45
increase_time = 10
delta_distance_to_high_accuracy(-) = 0.03
delta_distance_to_high_accuracy(+) = 0.02
number_of_face_required = 4
```

### [human_detection_config]

```ini
model_path = ../../model/yolov8n.pt
round_result = 5
label_class = 0
```

### [objects_detection_config]

```ini
model_path = ../../model/yolov8n.pt
round_result = 5
```

