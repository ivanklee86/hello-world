# pylint: disable=no-else-return
from flask import Blueprint, jsonify, make_response, current_app, request
from app.helpers.requestid import requestid
from app.extensions.sqlalchemy import db
from .models import Book
from .schema import BookSchema

# pylint: disable=invalid-name
books_blueprint = Blueprint('books', __name__, url_prefix='/api/v1/books')
BOOK_SCHEMA = BookSchema()
BOOK_SCHEMAS = BookSchema(many=True)

@requestid
@books_blueprint.route('', methods=['GET'])
def list_books():
    books = Book.query.all()
    result = BOOK_SCHEMAS.dump(books)
    return make_response(jsonify(result.data), 200)

@requestid
@books_blueprint.route('', methods=['POST'])
def add_entry():
    (entry_from_request, _) = BOOK_SCHEMA.load(request.json)
    (update, _) = BOOK_SCHEMA.dump(entry_from_request)
    book = Book(**update)
    db.session.add(book)
    db.session.commit()
    inserted_record = BOOK_SCHEMA.dump(book).data
    current_app.logger.info('Added entry: %s' % inserted_record)
    return make_response(jsonify(inserted_record), 200)

@requestid
@books_blueprint.route('/<list_id>', methods=['GET'])
def list_entry(list_id):
    found_book = BOOK_SCHEMA.dump(Book.query.get(list_id)).data

    if found_book:
        current_app.logger.info('Entry found for id %s: %s' % (list_id, found_book))
        return make_response(jsonify(found_book), 200)
    else:
        current_app.logger.info('Entry not found for id %s' % list_id)
        return make_response(jsonify(''), 404)


@requestid
@books_blueprint.route('/<list_id>', methods=['POST'])
def update_entry(list_id):
    # Check to see if object exists.
    Book.query.get_or_404(list_id)

    # Create query, discarding optional values.
    (entry_from_request, _) = BOOK_SCHEMA.load(request.json)
    (update, _) = BOOK_SCHEMA.dump(entry_from_request)
    update = {k: v for k, v in update.items() if v is not None}

    # Update row.
    Book.query.filter_by(id=list_id).update(update)
    db.session.commit()

    updated_book = BOOK_SCHEMA.dump(db.session.query(Book).get(list_id)).data
    current_app.logger.info('Updated entry %s with data: %s' % (list_id, updated_book))
    return make_response(jsonify(updated_book), 200)

@requestid
@books_blueprint.route('/<list_id>', methods=['DELETE'])
def remove_book(list_id):
    # Check to see if object exists.
    entry = Book.query.get_or_404(list_id)
    db.session.delete(entry)
    db.session.commit()
    current_app.logger.info('Removed entry: %s', list_id)
    return ('', 204)
