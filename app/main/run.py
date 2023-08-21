from routers.routers import app
from config import Config
if __name__ == '__main__':
    host = Config.host
    port = Config.port
    app.run(host=host, port=port, debug=True)