from flask import Blueprint, render_template, request
from wtforms import Form, IntegerField, validators
from flask_table import Table, Col
from app.helpers.requestid import requestid
from app.modules.entries.models import Entry

# pylint: disable=invalid-name
frontend_blueprint = Blueprint('frontend', __name__, url_prefix='/')

# pylint: disable=abstract-method
class Comments(Table):
    classes = ['table']
    id = Col('id')
    comment = Col('comment', )
    description = Col('description')

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
        return comments(form.comment_id.data)
    return render_template('search.html', form=form)

@requestid
@frontend_blueprint.route('/comments', methods=['GET'])
@frontend_blueprint.route('/comments/<id>', methods=['GET'])
def comments(comment_id=None):
    if not comment_id:
        entries = Entry.query.all()
    else:
        entries = Entry.query.filter(Entry.id == comment_id)

    table = Comments(entries)
    return render_template('search_results.html', table=table)
