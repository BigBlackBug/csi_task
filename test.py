import os
import pickle

from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

import constants
from predictor import predictor
from predictor.routes import routes
from web import app


class MainTestCase(AioHTTPTestCase):
    async def get_application(self):
        return app.init(routes=routes, loop=self.loop)

    def get_classifier(self):
        return pickle.load(
            open(os.path.join(constants.BASE_DIR, 'test_data',
                              'test_classifier.pickle'), 'rb'))

    @unittest_run_loop
    async def test_classifier_empty_vector(self):
        with self.assertRaises(ValueError):
            await predictor.predict([], classifier=self.get_classifier())

    @unittest_run_loop
    async def test_classifier_none_classifier(self):
        with self.assertRaises(ValueError):
            await predictor.predict([1, 2, 3, 4], classifier=None)

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
