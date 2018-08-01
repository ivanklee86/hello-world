import os
from flask import Flask, make_response, jsonify


def create_app(overwrite_db=None):
    app = Flask(__name__)

    from hello_flask import extensions
    from hello_flask import modules
    from hello_flask.config_flask import config_flask
    from hello_flask.helpers.requestid import requestid
    from hello_flask.extensions.sqlalchemy.create_db import create_db

    config_flask(app)
    if overwrite_db:
        app.config['SQLALCHEMY_DATABASE_URI'] = overwrite_db

    extensions.init_app(app)
    modules.init_app(app)

    create_db(app)

    @requestid
    @app.errorhandler(500)
    def internal_error(exception):
        app.logger.error(exception)
        return make_response(jsonify(exception), 500)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run()