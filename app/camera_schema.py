from app.handle.app_error import InvalidImageError, NoImageError
from app.config.face_functions_config import Face_config
import os
pass_test = False
image_file = None
def schema_test(image_file):
    if not image_file:
        raise NoImageError
    else:
        # Check if the uploaded file has a valid image extension
        allowed_extensions = Face_config.path
        filename, extension = os.path.splitext(image_file.filename)
        if extension[1:].lower() not in allowed_extensions:
            raise InvalidImageError
        else:
            pass_test = True
    return pass_test
