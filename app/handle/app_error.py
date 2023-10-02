from flask import jsonify

class AppError(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code

class CustomError:
    INVALID_IMAGE = {'code': "i01", 'message': 'Invalid image file format'}
    NO_IMAGE = {'code': "i02", 'message': 'No image file uploaded'}
    NO_DETECTION = {'code': "i03", 'message': 'Nothing was detected'}
    NO_FACE_NAME = {'code': "i04", 'message': "Face's name required"}
    DATABASE_IS_NONE = {'code': "d01", 'message': 'Can not connect to the database'}
    OUTPUT_TOO_LONG = {'code': "d02", 'message': 'Output data too large!!!'}
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
class NoFaceNameError(AppError):
    def __init__(self):
        super().__init__(CustomError.NO_FACE_NAME['message'], CustomError.NO_FACE_NAME['code'])
class DatabaseNoneError(AppError):
    def __init__(self):
        super().__init__(CustomError.DATABASE_IS_NONE['message'], CustomError.DATABASE_IS_NONE['code'])
class OutputTooLongError(AppError):
    def __init__(self):
        super().__init__(CustomError.OUTPUT_TOO_LONG['message'], CustomError.OUTPUT_TOO_LONG['code'])
def handle_generic_error(error):
    response = {'error': error.args[0], 'status_code': getattr(error, 'status_code', 500)}
    if error.args[0] == 'No image file uploaded' or error.args[0] == 'Nothing was detected' or error.args[0] == "Face's name required" :
        return jsonify(response), 404
    elif error.args[0] == 'Invalid image file format':
        return jsonify(response), 415
    elif error.args[0] == 'Can not connect to the database':
        return jsonify(response), 503
    elif error.args[0] == 'Output data too large!!!':
        return jsonify(response), 413