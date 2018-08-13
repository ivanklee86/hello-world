from flask_marshmallow import Marshmallow

# pylint: disable=invalid-name
ma = Marshmallow()


def init_app(app):
    ma.init_app(app)
