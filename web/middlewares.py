import json
import traceback

from aiohttp import web

from log_utils import LogFactory
from predictor.errors import PredictorError

log = LogFactory.make_log(__file__)


async def error_middleware(app, handler):
    def json_error(request, message, stack_trace=""):
        return web.Response(
            body=json.dumps({'error': message,
                             'stack_trace': stack_trace}).encode(
                'utf-8'),
            content_type='application/json')

    async def middleware_handler(request: web.Request):
        try:
            log.debug("Got request for {0}".format(request.rel_url))
            response = await handler(request)
        except PredictorError as ex:
            log.error("Unexpected Error")
            return json_error(request, ex.args[0], traceback.format_exc())
        else:
            log.debug("Request handled for {0}".format(request.rel_url))
            return response

    return middleware_handler
