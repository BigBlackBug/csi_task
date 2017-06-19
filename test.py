import os
import pickle

from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

import constants
from predictor import predictor


class MainTestCase(AioHTTPTestCase):
    """
    No more tests today! I know I should have tested the service itself via
    an HTTPClient or whatever or mocked out the requests but that would take
    another hour. And I'm getting closer to my 2 hour limit, so not now :)
    """
    async def get_application(self):
        return web.Application()

    def get_classifier(self):
        return pickle.load(
            open(os.path.join(constants.BASE_DIR, 'test_data',
                              'test_classifier.pickle'), 'rb'))

    @unittest_run_loop
    async def test_classifier_no_error(self):
        """
        I know that's a genius test, but there's nothing else we can test here.
        I can't test the outcomes of the method
        """
        try:
            await predictor.predict([
                5.1, 3.5, 1.4, 0.2
            ], classifier=self.get_classifier())
        except Exception:
            self.fail("predictor threw an error")

