from . import logging
from .sqlalchemy import db


def init_app(app):
    extensions = [
            logging,
            db,
    ]

    for extension in extensions:
        extension.init_app(app)
