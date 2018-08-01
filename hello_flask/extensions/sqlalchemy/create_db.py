from hello_flask.modules.entries.models import Entry
from hello_flask.extensions.sqlalchemy import db

def create_db(app):
    with app.app_context():
        db.create_all()