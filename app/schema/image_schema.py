from app.handle.app_error import InvalidImageError, NoImageError
import os
import configparser
from pydantic import BaseModel, ValidationError

# Construct the relative path to config.ini
config_path = os.path.realpath("../config.ini")

# Create a configuration object
config = configparser.ConfigParser()
config.read(config_path)

class ImageFileSchema(BaseModel):
    datafield: str
    datatype: str
    mandatory: bool

def schema_test(image_file):
    pass_test = False
    if not image_file:  # mandatory
        raise NoImageError
    # Check if the uploaded file has a valid image extension
    allowed_extensions = config.get('function_config', 'path')  # data field - datatype
    filename, extension = os.path.splitext(image_file.filename)
    if extension[1:].lower() not in allowed_extensions:
        raise InvalidImageError

    try:
        # Validate the ImageFileSchema
        image_data = {
            'datafield': 'image',
            'datatype': extension[1:].lower(),
            'mandatory': True
        }
        ImageFileSchema(**image_data)
        pass_test = True
    except ValidationError:
        # Handle validation errors here
        pass_test = False
    return pass_test