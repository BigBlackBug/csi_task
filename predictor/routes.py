from predictor import handlers

routes = [
    ('POST', '/predict', handlers.predict, 'predict'),
    ('POST', '/upload_classifier', handlers.upload_classifier,
     'upload_classifier')
]
