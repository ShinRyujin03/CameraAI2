import logging

from flask import jsonify


class AppError(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code


class CustomError:
    INVALID_IMAGE = {'code': "i01", 'message': 'Invalid image file format. Supported formats are PNG, JPG, and JPEG.'}
    NO_IMAGE = {'code': "i02", 'message': 'Image not found. Please upload a valid image file.'}
    NO_DETECTION = {'code': "i03",
                    'message': 'No face detected in the image. Please upload an image with a visible face.'}
    FILE_UNREACHABLE = {'code': "i04", 'message': 'Image unreachable. Make sure the file exists and is accessible.'}

    NO_FACE_NAME = {'code': "f01", 'message': "Face name not found. Please provide a valid name for the face."}
    INVALID_FACE_NAME = {'code': "f02", 'message': "Invalid image face name. Please provide a valid name for the face."}
    DATABASE_IS_NONE = {'code': "d01",
                        'message': 'Unable to establish a connection with the database. Please try again later.'}
    OUTPUT_TOO_LONG = {'code': "d02",
                       'message': 'Output size exceeds the maximum allowed limit. Please upload a less complex image.'}
    # Add more custom errors as needed


class NoDetection(AppError):
    def __init__(self):
        super().__init__(CustomError.NO_DETECTION['message'], CustomError.NO_DETECTION['code'])


class InvalidImageError(AppError):
    def __init__(self):
        super().__init__(CustomError.INVALID_IMAGE['message'], CustomError.INVALID_IMAGE['code'])


class NoImageError(AppError):
    def __init__(self):
        super().__init__(CustomError.NO_IMAGE['message'], CustomError.NO_IMAGE['code'])


class FileUnreachable(AppError):
    def __init__(self):
        super().__init__(CustomError.FILE_UNREACHABLE['message'], CustomError.FILE_UNREACHABLE['code'])


class NoFaceNameError(AppError):
    def __init__(self):
        super().__init__(CustomError.NO_FACE_NAME['message'], CustomError.NO_FACE_NAME['code'])


class InvalidFaceNameError(AppError):
    def __init__(self):
        super().__init__(CustomError.INVALID_FACE_NAME['message'], CustomError.INVALID_FACE_NAME['code'])


class DatabaseNoneError(AppError):
    def __init__(self):
        super().__init__(CustomError.DATABASE_IS_NONE['message'], CustomError.DATABASE_IS_NONE['code'])


class OutputTooLongError(AppError):
    def __init__(self):
        super().__init__(CustomError.OUTPUT_TOO_LONG['message'], CustomError.OUTPUT_TOO_LONG['code'])


def handle_generic_error(error):
    response = {'error': error.args[0], 'status_code': getattr(error, 'status_code', 500)}
    if error.args[0] == 'Face name not found. Please provide a valid name for the face.' or error.args[
        0] == 'Image not found. Please upload a valid image file.' or error.args[
        0] == "No face detected in the image. Please upload an image with a visible face.":
        logging.critical("404 Not Found")
        return jsonify(response), 404
    elif error.args[0] == 'Image unreachable. Make sure the file exists and is accessible.':
        logging.critical("405 Method Not Allowed")
        return jsonify(response), 405
    elif error.args[0] == 'Invalid image face name. Please provide a valid name for the face.':
        logging.critical("406 Not Acceptable")
        return jsonify(response), 406
    elif error.args[0] == 'Invalid image file format. Supported formats are PNG, JPG, and JPEG.':
        logging.critical("415 Unsupported Media Type")
        return jsonify(response), 415
    elif error.args[0] == 'Unable to establish a connection with the database. Please try again later.':
        logging.critical("503 Service Unavailable")
        return jsonify(response), 503
    elif error.args[0] == 'Output size exceeds the maximum allowed limit. Please upload a less complex image.':
        logging.critical("413 Payload Too Large")
        return jsonify(response), 413
