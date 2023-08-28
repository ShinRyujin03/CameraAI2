from app.routers.face_functions_routers import face_router
from app.routers.object_function_routers import objects_router
from flask import Flask
from app.config.db_config import Config
app = Flask(__name__)
# Register the funtion_router blueprint
app.register_blueprint(face_router, url_prefix='/face')
app.register_blueprint(objects_router, url_prefix='/objects')
if __name__ == '__main__':
    host = Config.host
    port = Config.port
    app.run(host=host, port=port, debug=True)