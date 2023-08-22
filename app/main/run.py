from routers.funtion_routers import funtion_router
from routers.database_routers import database_router
from flask import Flask
from config import Config
app = Flask(__name__)
# Register the funtion_router blueprint
app.register_blueprint(funtion_router, url_prefix='/functions')

# Register the database_router blueprint
app.register_blueprint(database_router, url_prefix='/database')
if __name__ == '__main__':
    host = Config.host
    port = Config.port
    app.run(host=host, port=port, debug=True)