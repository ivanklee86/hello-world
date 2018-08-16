from flask import Blueprint, render_template, request
from wtforms import Form, IntegerField, validators
from flask_table import Table, Col
from app.helpers.requestid import requestid
from app.modules.books.models import Book

# pylint: disable=invalid-name
frontend_blueprint = Blueprint('frontend', __name__, url_prefix='/')

# pylint: disable=abstract-method
class Comments(Table):
    classes = ['table']
    id = Col('id')
    title = Col('title')
    author = Col('author')
    publisher = Col('publisher')
    description = Col('description')
    comment = Col('comment', )

class SearchForm(Form):
    comment_id = IntegerField("Id", [validators.Optional()])

@requestid
@frontend_blueprint.route('', methods=['GET'])
def index_page():
    return render_template('home.html')

@requestid
@frontend_blueprint.route('/search', methods=['GET', 'POST'])
def search_page():
    form = SearchForm(request.form)
    if request.method == 'POST' and form.validate():
        return book_results(form.comment_id.data)
    return render_template('search.html', form=form)

@requestid
@frontend_blueprint.route('/comments', methods=['GET'])
@frontend_blueprint.route('/comments/<id>', methods=['GET'])
def book_results(comment_id=None):
    if not comment_id:
        books = Book.query.all()
    else:
        books = Book.query.filter(Book.id == comment_id)

    table = Comments(books)
    return render_template('search_results.html', table=table)
