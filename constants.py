import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
__CLASSIFIER_DIR = os.path.join(BASE_DIR, "classifiers")


def make_classifier_path(filename):
    return os.path.join(__CLASSIFIER_DIR, filename)
