"""
Flask app factory
"""
from flask import Flask, make_response, jsonify


def create_app(overwrite_db=None):
    """
    Flask app factory method.

    :param overwrite_db: URI for local SQLITE DB, used for tests.
    :return:
    """
    app = Flask(__name__)

    from app import extensions
    from app import modules
    from app.config_flask import config_flask
    from app.helpers.requestid import requestid
    from app.extensions.sqlalchemy.create_db import create_db

    config_flask(app)
    if overwrite_db:
        app.config['SQLALCHEMY_DATABASE_URI'] = overwrite_db

    extensions.init_app(app)
    modules.init_app(app)

    if overwrite_db:
        create_db(app)

    # Error handling method
    # pylint: disable=unused-variable
    @requestid
    @app.errorhandler(500)
    def internal_error(exception):
        app.logger.error(exception)
        return make_response(jsonify(exception), 500)

    return app
