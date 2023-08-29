from flask import jsonify

class AppError(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code

class CustomError:
    INVALID_IMAGE = {'code': "i01", 'message': 'Invalid image file format'}
    NO_IMAGE = {'code': "i02", 'message': 'No image file uploaded'}
    DATABASE_IS_NONE = {'code': "d01", 'message': 'Can not connect database'}
    # Add more custom errors as needed

class InvalidImageError(AppError):
    def __init__(self):
        super().__init__(CustomError.INVALID_IMAGE['message'], CustomError.INVALID_IMAGE['code'])

class NoImageError(AppError):
    def __init__(self):
        super().__init__(CustomError.NO_IMAGE['message'], CustomError.NO_IMAGE['code'])
class DatabaseNoneError(AppError):
    def __init__(self):
        super().__init__(CustomError.DATABASE_IS_NONE['message'], CustomError.DATABASE_IS_NONE['code'])
def handle_generic_error(error):
    response = {'error': error.args[0], 'status_code': getattr(error, 'status_code', 500)}
    return jsonify(response)
