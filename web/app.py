import asyncio

from aiohttp import web

from web.middlewares import error_middleware


def init(routes, loop=asyncio.get_event_loop()):
    app = web.Application(loop=loop)
    app.middlewares.extend([error_middleware])
    for route in routes:
        app.router.add_route(route[0], route[1], route[2], name=route[3])

    return app
