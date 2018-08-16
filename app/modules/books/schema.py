from app.extensions import ma
from .models import Book

class BookSchema(ma.ModelSchema):
    class Meta:
        model = Book
