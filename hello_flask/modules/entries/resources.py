from flask import Blueprint, jsonify, make_response, current_app
from hello_flask.helpers.requestid import requestid
from .models import Entry

entries_blueprint = Blueprint('entries', __name__, url_prefix='/api/v1/entries')


@requestid
@entries_blueprint.route('', methods=['GET'])
def list_entries():
    entries = list(map(lambda x: x.as_dict(), Entry.query.all()))
    current_app.logger.info('Retrieved %d entries' % len(entries))
    return make_response(jsonify(entries), 200)
