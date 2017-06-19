import numpy as np

from log_utils import LogFactory
from predictor.errors import PredictorError

log = LogFactory.make_log(__file__)


async def predict(input_vector, classifier):
    """
    predicts which class input vector belongs to
    according to the supplied classifier
    :param input_vector:
    :param classifier:
    :return: class number
    """
    log.debug("Preparing input data {}".format(input_vector))
    x = np.array(input_vector)
    x = x.reshape(1, -1)
    # TODO prediction can take a long time
    # in the future should be refactored into a Future (lol)
    log.debug("Running prediction on vector {}".format(input_vector))
    classes_found = classifier.predict(x)
    log.debug("Found {} classes".format(classes_found))
    n_classes = len(classes_found)
    if n_classes == 0:
        raise PredictorError("No classes have been detected")
    elif n_classes > 1:
        raise PredictorError(
            "Only one class is expected to be detected, "
            "instead got: {}".format(n_classes))
    return classes_found[0]
