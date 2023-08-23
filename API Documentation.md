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
#### Detect Human Location
- **Endpoint**: `/functions/human_location`
- **Query Params**: `img_path`
- **Method**: GET
- **Description**: Detect human locations in images.
- **Response**: List of detected human locations.

#### Human Detection Database
- **Endpoint**: `/database/save_human_location`
- **Query Params**: `img_path`
- **Method**: POST
- **Description**: Save detected human locations to the database.
- **Response**: Success message.

### Face Location
#### Detect Face Location
- **Endpoint**: `/functions/face_location`
- **Query Params**: `img_path`
- **Method**: GET
- **Description**: Detect face locations in images.
- **Response**: List of detected face locations.

#### Face Location Database
- **Endpoint**: `/database/save_face_location`
- **Query Params**: `img_path`
- **Method**: POST
- **Description**: Save detected face locations to the database.
- **Response**: Success message.

### Face Landmarks
#### Encode Face to Array
- **Endpoint**: `/functions/face_landmarks`
- **Query Params**: `img_path`
- **Method**: GET
- **Description**: Encode face landmarks to an array.
- **Response**: List of encoded face landmarks.

#### Face Landmark Database
- **Endpoint**: `/database/save_face_landmark`
- **Query Params**: `img_path`
- **Method**: POST
- **Description**: Save encoded face landmarks to the database.
- **Response**: Success message.

## Usage

### Human Detection
- To detect human locations, input the query params `img_path` and make a GET request to `/functions/human_location`.
- To save detected human locations to the database, input the query params `img_path` and make a POST request to `/database/save_human_location`.

### Face Location
- To detect face locations, input the query params `img_path` and make a GET request to `/functions/face_location`.
- To save detected face locations to the database, input the query params `img_path` and make a POST request to `/database/save_face_location`.

### Face Landmarks
- To encode face landmarks, input the query params `img_path` and make a GET request to `/functions/face_landmarks`.
- To save encoded face landmarks to the database, input the query params `img_path` and make a POST request to `/database/save_face_landmark`.

## Variables
- `baseUrl`: `http://localhost:1102`
- `db_host` ='localhost'
- `db_user` = 'root'
- `db_name` = "metadata"!