from app.routers.face_functions_routers import face_router
from app.routers.human_detection_routers import objects_router
from flask import Flask,jsonify
from app.config.db_config import Config
from app.handle.app_error import handle_generic_error


app = Flask(__name__)
# Register the custom error handlers
app.register_error_handler(Exception, handle_generic_error)

# Register the funtion_router blueprint
app.register_blueprint(face_router, url_prefix='/face')
app.register_blueprint(objects_router, url_prefix='/objects')
if __name__ == '__main__':
    host = Config.host
    port = Config.port
    app.run(host=host, port=port, debug=True)