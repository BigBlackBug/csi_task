from aiohttp import web

from predictor.routes import routes
from web import app

DEFAULT_PORT = 8080
if __name__ == '__main__':
    application = app.init(routes=routes)
    web.run_app(application, port=DEFAULT_PORT)
