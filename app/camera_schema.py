from app.handle.app_error import InvalidImageError, NoImageError
import os
import configparser
# Get the current directory of your script
script_directory = os.path.dirname(os.path.realpath("config/config.ini"))

# Construct the relative path to config.ini
config_path = os.path.join(script_directory,'config.ini')
# Create a configuration object
config = configparser.ConfigParser()
config.read(config_path)
pass_test = False
image_file = None
def schema_test(image_file):
    if not image_file:
        raise NoImageError
    else:
        # Check if the uploaded file has a valid image extension
        allowed_extensions = config.get('face_function_config', 'path')
        filename, extension = os.path.splitext(image_file.filename)
        if extension[1:].lower() not in allowed_extensions:
            raise InvalidImageError
        else:
            pass_test = True
    return pass_test
