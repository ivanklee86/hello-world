from app.extensions import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False)
    author = db.Column(db.String(120), unique=False)
    publisher = db.Column(db.String(120), unique=False)
    description = db.Column(db.String(80), unique=False)
    comment = db.Column(db.String(120), unique=False)
