from app.extensions import ma
from .models import Book

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
