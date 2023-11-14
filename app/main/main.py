import sys
import os

project_path = os.environ.get('CAMERA_AI_PATH')

if project_path is not None:
    sys.path.append(project_path)
else:
    print("Error: Environment variable CAMERA_AI_PATH not set.")

import configparser
import logging
import os
from flask import Flask
from app.handle.app_error import handle_generic_error
from app.routers.face_routers import face_router
from app.routers.human_detection_routers import objects_router
from app.routers.multiple_objects_detection_routers import multiple_objects_router


# Construct the relative path to config.ini
config_path = os.path.realpath("../config.ini")
# Create a configuration object
config = configparser.ConfigParser()
config.read(config_path)

app = Flask(__name__)
# Register the custom error handlers
app.register_error_handler(Exception, handle_generic_error)

# Register the funtion_router blueprint
app.register_blueprint(face_router, url_prefix=config.get('function_config', 'face_prefix'))
app.register_blueprint(objects_router, url_prefix=config.get('function_config', 'objects_prefix'))
app.register_blueprint(multiple_objects_router,
                       url_prefix=config.get('function_config', 'multiple_objects_prefix'))

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    host = config.get('db_config', 'host')
    port = config.getint('db_config', 'port')
    app.run(host=host, port=port, debug=True)
