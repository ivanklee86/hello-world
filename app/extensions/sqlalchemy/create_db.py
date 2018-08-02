from app.modules.entries.models import Entry
from app.extensions.sqlalchemy import db

def create_db(app):
    with app.app_context():
        db.create_all()