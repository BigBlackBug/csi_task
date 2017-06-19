import sys

from aiohttp import web

from predictor.routes import routes
from web import app

DEFAULT_PORT = 8080
if __name__ == '__main__':
    application = app.init(routes=routes)

    port = DEFAULT_PORT
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    web.run_app(application, port=port)
