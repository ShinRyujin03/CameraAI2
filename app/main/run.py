from app.routers.functions_routers import functions_router
from flask import Flask
from config import Config
app = Flask(__name__)
# Register the funtion_router blueprint
app.register_blueprint(functions_router, url_prefix='/functions')

if __name__ == '__main__':
    host = Config.host
    port = Config.port
    app.run(host=host, port=port, debug=True)