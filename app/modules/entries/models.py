from app.extensions import db

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), unique=False)
    comment = db.Column(db.String(120), unique=False)

    def as_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'comment': self.comment
        }