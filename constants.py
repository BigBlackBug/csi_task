import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
__CLASSIFIER_DIR = os.path.join(BASE_DIR, "classifiers")
if not os.path.exists(__CLASSIFIER_DIR):
    os.mkdir(__CLASSIFIER_DIR)


def make_classifier_path(filename):
    return os.path.join(__CLASSIFIER_DIR, filename)
