from app.extensions import ma
from .models import Entry

class EntrySchema(ma.ModelSchema):
    class Meta:
        model = Entry
