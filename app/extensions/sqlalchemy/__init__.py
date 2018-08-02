import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

def init_app(app):
    db.init_app(app)