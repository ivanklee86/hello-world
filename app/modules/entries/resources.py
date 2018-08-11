# pylint: disable=no-else-return
from flask import Blueprint, jsonify, make_response, current_app, request
from app.helpers.requestid import requestid
from app.extensions.sqlalchemy import db
from .models import Entry

# pylint: disable=invalid-name
entries_blueprint = Blueprint('entries', __name__, url_prefix='/api/v1/entries')


@requestid
@entries_blueprint.route('', methods=['GET'])
def list_entries():
    entries = list(map(lambda x: x.as_dict(), Entry.query.all()))
    current_app.logger.info('Retrieved %d entries' % len(entries))
    return make_response(jsonify(entries), 200)

@requestid
@entries_blueprint.route('', methods=['POST'])
def add_entry():
    content = request.json
    entry = Entry()
    entry.description = content['description']
    entry.comment = content['comment']
    db.session.add(entry)
    db.session.commit()
    current_app.logger.info('Added entry: %s' % entry.as_dict())
    return make_response(jsonify(entry.as_dict()), 200)

@requestid
@entries_blueprint.route('/<list_id>', methods=['GET'])
def list_entry(list_id):
    entry = Entry.query.get(list_id)
    if entry:
        current_app.logger.info('Entry found for id %s: %s' % (list_id, entry.as_dict()))
        return make_response(jsonify(entry.as_dict()), 200)
    else:
        current_app.logger.info('Entry not found for id %s' % list_id)
        return make_response(jsonify(''), 404)


@requestid
@entries_blueprint.route('/<list_id>', methods=['POST'])
def update_entry(list_id):
    content = request.json
    content.pop('id', None)
    db.session.query(Entry).filter_by(id=list_id).update(content)
    entry = Entry.query.get(list_id)
    if entry:
        db.session.commit()
        current_app.logger.info('Updated entry %s with data: %s' % (list_id, content))
        return make_response(jsonify(entry.as_dict()), 200)
    else:
        current_app.logger.info('Entry not found for id %s' % list_id)
        return make_response(jsonify(''), 404)

@requestid
@entries_blueprint.route('/<list_id>', methods=['DELETE'])
def remove_entry(list_id):
    entry = Entry.query.get(list_id)
    if entry:
        db.session.delete(entry)
        db.session.commit()
        current_app.logger.info('Removed entry: %s', entry.as_dict())
        return make_response(jsonify(entry.as_dict()), 200)
    else:
        current_app.logger.info('Entry not found for id %s' % list_id)
        return make_response(jsonify(''), 404)
