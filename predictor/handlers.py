import os
import pickle

from aiohttp import web

import constants
from log_utils import LogFactory
from predictor import predictor
from predictor.errors import PredictorError

log = LogFactory.make_log(__file__)


def _load_classifier(name):
    classifier_path = constants.make_classifier_path(name)
    if not os.path.exists(classifier_path):
        raise PredictorError(
            "Selected classifier '{}' doesn't exist".format(name))
    return pickle.load(open(classifier_path, 'rb'))


async def predict(request):
    json_data = await request.json()
    # TODO add input_data validation
    classifier_name = json_data['classifier_name']
    source_data = json_data['data']
    input_vector = list(source_data.values())

    log.debug("Loading classifier: {}".format(classifier_name))
    classifier = _load_classifier(classifier_name)
    result_class = await predictor.predict(input_vector, classifier)
    return web.json_response({"class": str(result_class)})


async def upload_classifier(request: web.Request):
    """
    saves a new classifier model
    :param request:
    :return:
    """
    reader = await request.multipart()
    part = await reader.next()

    if part is None:
        raise PredictorError("No file was found in the request data")
    filename = part.filename
    if filename is not None:
        file_bytes = await part.read()
        # TODO handle duplicates
        log.info("Saving a new classifier '{}'".format(filename))
        with open(constants.make_classifier_path(filename), 'wb') as f:
            f.write(file_bytes)
        log.info("Classifier '{}' has been "
                 "successfully saved".format(filename))
    else:
        raise PredictorError("Request contains invalid file. "
                             "Check filename property")
    return web.Response()
