from . import logging
from .sqlalchemy import db
from .marshmallow import ma

def init_app(app):
    extensions = [
        logging,
        db,
        ma
    ]

    for extension in extensions:
        extension.init_app(app)
