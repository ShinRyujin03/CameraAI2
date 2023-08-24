# API Documentation

## Introduction
This documentation outlines the endpoints, requests, and responses for the Camera API. It also includes information about the database tables used to store the API responses.

## Base URL
`http://localhost:1102`

## Database Information
- **Database Host**: localhost or 127.0.0.1
- **Database Name**: metadata
- **Database User**: root
- **Database Password**: No password require

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
  - `human_location_boxes`: VARCHAR(255), NOT NULL
  - `human_location_weights`: VARCHAR(255), NOT NULL
  - `created_at`: TIMESTAMP, NOT NULL, Default: current_timestamp()
- **Description**: Stores information about detected human locations.

## Model Library
- **Library name**: face-recognition
- **Version**: 1.3.0
- **Install command line**: `pip install face-recognition`
- **Library Project description**: https://pypi.org/project/face-recognition/

## Endpoints

### Human Detection
- **Endpoint**: `/functions/human_location`
- **Data**: `image`
- **Method**: POST
- **Description**: Detect human locations in images and save metadata to the database.
- **Response**: List of detected human locations.

### Face Location
- **Endpoint**: `/functions/face_location`
- **Data**: `image`
- **Method**: POST
- **Description**: Detect face locations in images and save metadata to the database.
- **Response**: List of detected face locations.

### Face Landmarks
- **Endpoint**: `/functions/face_landmarks`
- **Data**: `image`
- **Method**: POST
- **Description**: Encode face landmarks to an array and save metadata to the database.
- **Response**: List of encoded face landmarks.

## Usage

### Human Detection
- To detect human locations, upload the `image` and make a POST request to `/functions/human_location`. The metadata will save in the `human_location Table`

### Face Location
- To detect face locations, upload the `image` and make a POST request to `/functions/face_location`. The metadata will save in the `face_location Table`

### Face Landmarks
- To encode face landmarks, upload the `image` and make a POST request to `/functions/face_landmarks`. The metadata will save in the `face_landmarks Table`
## Variables
- `baseUrl`: `http://localhost:1102`
- `db_host` = `localhost`
- `db_user` = `root`
- `db_name` = `metadata`