from app.routers.face_functions_routers import face_router
from app.routers.human_detection_routers import objects_router
from flask import Flask
import configparser
from app.handle.app_error import handle_generic_error
import os

# Get the current directory of your script
script_directory = os.path.dirname(os.path.realpath("config/config.ini"))

# Construct the relative path to config.ini
config_path = os.path.join(script_directory,'config.ini')

# Create a configuration object
config = configparser.ConfigParser()
config.read(config_path)

app = Flask(__name__)
# Register the custom error handlers
app.register_error_handler(Exception, handle_generic_error)

# Register the funtion_router blueprint
app.register_blueprint(face_router, url_prefix=config.get('function_config', 'face_prefix'))
app.register_blueprint(objects_router, url_prefix= config.get('function_config', 'objects_prefix'))
if __name__ == '__main__':
    host = config.get('db_config', 'host')
    port = config.getint('db_config', 'port')
    app.run(host=host, port=port, debug=True)