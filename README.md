# API Documentation

## Table of Contents

- [Introduction](#introduction)
- [Quick Guide](#quick-guide)
    - [Pre-requisites](#pre-requisites)
    - [Installation](#installation)
    - [Running the Application](#running-the-application)
    - [API Usage](#api-usage)
    - [Training and Testing image guide](#training-and-testing-image-guide)
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
- [Function Endpoints](#function-endpoints)
    - [Human Detection](#human-detection)
    - [Multiple Objects Detection](#multiple-objects-detection)
    - [Face Location](#face-location)
    - [Face Landmarks](#face-landmarks)
    - [Facial Attribute Recognition](#facial-attribute-recognition)
    - [Face Verification](#face-verification)
    - [Name Recognition](#name-recognition)
- [Endpoint Usage](#endpoint-usage)
- [Testing Endpoints](#testing-endpoints)
    - [Image Test (binary to image)](#image-test-binary-to-image)
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
4. Create a database with name is 'metadata'

5. Set up the database by run SQL script:
    ```
   database/metadata.sql
    ```

### Running the Application
- Please replace `path_to_the_project` with your actual path
1. Set the environment variable on each device:
    ```bash
    export CAMERA_AI_PATH=path_to_the_project/CameraAI2
    ```
2. Start the application using the provided run script:

    ```bash
    cd path_to_the_project/CameraAI2
    python app/main/main.py
    ```

3. The application will start, and you can now access the API at http://localhost:1102 or http://127.0.0.1:1102.

### API Usage

#### Sending Requests

- Use tools like `curl`, `Postman`, or your preferred HTTP client to send requests to the API endpoints.
  See the [Endpoint Usage](#endpoint-usage) for more information

- Each requests can handling multiple image files (except [Face Verification Endpoint](#face-verification))

![Ảnh màn hình 2023-11-01 lúc 14.49.21.png](database/README.md%20image/API%20input.png)

#### Sending Image Files

- When sending image files, ensure they are in one of the supported formats: PNG, JPG, or JPEG.

#### API Responses

- The API returns JSON responses containing the requested data or error messages.
  See the [Function Endpoints](#function-endpoints) and [Error Handle](#error-handle) for more information

### Training and Testing image guide
- This guide is use for [Face Verification Endpoint](#face-verification)  and [Name Recognition Endpoint](#name-recognition) only
#### Training Image
- The path of `Training Image` folder is
    ```
    model/Training image
    ```
- You can request to either the  [Face Location Endpoint](#face-location) or [Facial Attribute Recognition Endpoint](#facial-attribute-recognition) in order to include the image in the database then type the person's name (sub-folder name) in the `face_name` column.
#### Testing Image
- The path of `Testing Image` folder is
    ```
    app/services/test/Testing image
    ```
- Thís folder used to test accuracy of [Face Verification Endpoint](#face-verification) and [Name Recognition Endpoint](#name-recognition) 
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
    - `image_name`: VARCHAR(255), Primary Key, NOT NULL
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

## Function Endpoints

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
      ![Jiwoo%20md.png](/database/README.md%20image/Jiwoo%20md.png)
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
      ![Ảnh màn hình 2023-11-01 lúc 14.38.03.png](/database/README.md%20image/Jiwoo%20md.png)
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
      ![Ảnh màn hình 2023-11-01 lúc 14.29.14.png](/database/README.md%20image/Kazuha%202.png)
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
      ![Ảnh màn hình 2023-11-01 lúc 14.23.56.png](database/README.md%20image/Yeji%20md.png)
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
      ![Wonyoung md.png](database/README.md%20image/Wonyoung%20md.png)
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
      ![Ảnh màn hình 2023-11-01 lúc 14.03.30.png](database/README.md%20image/Haewon%20md.png)
    - ***Output***
      ```json lines
      [
          {
              "Accuracy": "High",
              "Name": "Haewon",
              "face_verification": "verified",
              "image_name": "IMG_0587.JPG"
          },
          {
              "message": "Image IMG_0587.JPG saved successfully"
          }
      ]
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
      ![Rei md.png](/database/README.md%20image/Rei%20md.png)
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

- To detect human locations, upload the `image` and make a POST request to `{url}/object/human_location`.
- The image will save in `image` table
- The metadata will save in `human_location` table
- Results can be rounded to `n` numbers after the comma. `n` can be configuring at the variable `round_result`
- The results are in `xywh` format
- You can configure the `humman_detection` to other type of object detection by change the values of `label_class` (The
  list of object class can be detected
  at: https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco.yaml)

### Multiple Objects Detection

- To detect objects, upload the `image` and make a POST request to `{url}/m_object/objects_location`.
- The image will save in `image` table
- The metadata will save in `detected_objects` table
- Results can be rounded to `n` numbers after the comma. `n` can be configuring at the variable `round_result`
- The results are in `xywh` format
- The list of object can be detected
  at: https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco.yaml

### Face Location

- To detect face locations, upload the `image` and make a POST request to `{url}/face/face_location`.
- The image will save in `image` table
- The results are in `xyxy` format
- The metadata will save in `face_location` table

### Face Landmarks

- To encode face landmarks, upload the `image` and make a POST request to `{url}/face/face_landmarks`.
- The image will save in `image` table
- The metadata will save in `face_landmarks` table

### Facial Attribute Recognition

- To recognize face facial attribute, upload the `image` and make a POST request
  to `{url}/face/facial_attribute_recognition`.
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

- To verify face, upload the `image`, input the `face_name` and make a POST request to `{url}/face/face_verify`.
- The face verification status and valid face name will save in `face_verified` table
- The level of accuracy can be configuring in `config.ini`, has 4 level of accuracy are `high`, `medium-high` `medium-low`
  and `low`
- The face verification status will return `verified` when in `high` or `medium-high` level of accuracy
- The image will save in the database when in `high` level of accuracy only
- The elapsed time can be configuring at `verification_elapsed_time` variable in `config.ini` (Default = 1m)
- Accuracy level rule:
  - `Low` level : `min_distance` < `medium_accuracy_verification`
  - `Medium-low` level: (`high_accuracy_verification` + `delta_distance`) < `min_distance` <= `medium_accuracy_verification`
  - `Medium-high` level: `high_accuracy_verification` < `min_distance` <= (`high_accuracy_verification` + `delta_distance`)
  - `High` level: `min_distance` <= `high_accuracy_verification`
### Name Recognition

- To recognize face name, upload the `image` and make a POST request to `{url}/face/face_name_recognition`.
- The level of accuracy can be configuring in `config.ini`, has 3 level of accuracy are `high`, `medium`
  and `low`
- The image will save in the database when in `high` level of accuracy only
- The elapsed time for each input image can be configuring at `recognition_elapsed_time` variable in `config.ini` (Minimum elapsed time by default is 75 seconds and up to 90 seconds for each image (15 seconds added) if `high_distance`-`delta(-)`<`min_distance`<`high_distance`+`delta(+)`)
- Accuracy level rule:
  - `Low` level : `min_distance` < `medium_accuracy_recognition`
  - `Medium` level: `high_accuracy_recognition` < `min_distance` <= `medium_accuracy_recognition`
  - `High` level: `min_distance` <= `high_accuracy_recognition`

## Testing Endpoints
- **Prefix**:`/test`

### Image Test (binary to image)
- **Description**: This test is used to convert bytes strings file (`*.bin`) into image
- **Endpoint**: `/binary_to_image`
- **Method**: POST
- **Example Result**:
    - ***Input***
       ```  
       file = "face_metadata-image_file.bin"
       zoom = 0.5
       ```
    - ***Output***:    
      ![Ảnh màn hình 2023-11-01 lúc 15.47.52.png](database/README.md%20image/Test%20output.png)

### Face Location Test
- **Description**: The Face Location Test is designed to draw rectangles around faces in images to visualize the results of the `face_location` endpoint.
- **Endpoint**: `/draw_face_locations`
- **Method**: POST
- **Example Result**: 
    - ***Input*** 
       ```  
       image = "yujin 4.jpeg"
       face_locations = 73, 128, 135, 66 
       zoom = 2
       ```
    - ***Output***:    
      ![Ảnh màn hình 2023-11-01 lúc 15.47.52.png](database/README.md%20image/Yujin%20md.png)

### Number of Face Image Test

- **Description**:
    - The Number of Face Image Test analyzes the frequency of different face names detected in the dataset. It calculates the occurrence of each face name and provides insights into the distribution. The test also determines the pass and fail counts based on a predefined threshold.
    - The number of images per `face_name` in the database should be greater than or equal
      to `number_of_face_required` (recommended >= 4) to get the highest accuracy
- **Endpoint**: `/plot_face_names_histogram`
- **Method**: GET
- **Example Result**:
    ```
    Passed faces: Rosé (13 times), Jennie (5 times), Ryujin (13 times), Chaeryeong (5 times), NaNa (4 times), Lisa (11 times), Kazuha (6 times), Eunchae (4 times), Yeji (8 times), Irene (4 times), Rei (14 times), Yujin (7 times), IU (14 times), Sumin (4 times), Jisoo (5 times), Jiwoo (8 times), Wonyoung (10 times), Yuna (8 times), Sakura (8 times)
    Failed faces: Haewon (3 times), Minji (2 times), ITZY (2 times), Haerin (1 times), Miyeon (1 times), Joy (2 times), Test Img (1 times), Soyeon (1 times), Lia (3 times), Nayeon (2 times), Chaeyeon (1 times), Yuqi (2 times), Hyein (2 times), Hanni (2 times), Lily (2 times), Danielle (1 times), Tsuki (2 times), IVE (1 times)
    Face Pass: 15
    Face Fail: 22
    ```
  ![Figure_1.png](database/README.md%20image/Figure.png)

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
- **FILE_UNREACHABLE**
    - HTTP Code: `405 Method Not Allowed`
    - Code: "i04"
    - Message: Image unreachable. Make sure the file exists and is accessible.


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
```ini
[db_config]
host = 0.0.0.0
port = 1102
db_host = localhost
db_user = root
db_password =
db_name = metadata

[db_limit_config]
face_locations = 250
landmarks = 250
face_name = 250
objects_detected_boxes = 490
emotions = 250

[function_config]
face_prefix = /face
objects_prefix = /objects
multiple_objects_prefix = /m_objects
test_prefix = /test

[face_detection_config]
upsample_image = 1

[age_config]
ages_bias = -9
ages_range = 5

[verification_config]
low_accuracy_verification = 0.49
medium_accuracy_verification = 0.45
high_accuracy_verification = 0.37
verification_elapsed_time = 60
delta_distance = 0.035

[name_recognition_config]
low_accuracy_recognition = 0.43
medium_accuracy_recognition = 0.38
high_accuracy_recognition = 0.33
recognition_elapsed_time = 75
increase_time = 15
delta_distance_to_high_accuracy(-) = 0.15
delta_distance_to_high_accuracy(+) = 0.03
number_of_face_required = 4

[human_detection_config]
model_path = ../../model/yolov8n.pt
round_result = 5
label_class = 0

[objects_detection_config]
model_path = ../../model/yolov8n.pt
round_result = 5
```
