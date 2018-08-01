from flask import Blueprint, jsonify, make_response, current_app, request
from hello_flask.helpers.requestid import requestid
from hello_flask.extensions.sqlalchemy import db
from .models import Entry

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
@entries_blueprint.route('/<id>', methods=['GET'])
def list_entry(id):
    entry = Entry.query.get(id)
    if entry:
        current_app.logger.info('Entry found for id %s: %s' % (id, entry.as_dict()))
        return make_response(jsonify(entry.as_dict()), 200)
    else:
        current_app.logger.info('Entry not found for id %s' % id)
        return make_response(jsonify(''), 404)


@requestid
@entries_blueprint.route('/<id>', methods=['POST'])
def update_entry(id):
    content = request.json
    content.pop('id', None)
    db.session.query(Entry).filter_by(id=id).update(content)
    entry = Entry.query.get(id)
    if entry:
        db.session.commit()
        current_app.logger.info('Updated entry %s with data: %s' % (id, content))
        return make_response(jsonify(entry.as_dict()), 200)
    else:
        current_app.logger.info('Entry not found for id %s' % id)
        return make_response(jsonify(''), 404)

@requestid
@entries_blueprint.route('/<id>', methods=['DELETE'])
def remove_entry(id):
    entry = Entry.query.get(id)
    if entry:
        db.session.delete(entry)
        db.session.commit()
        current_app.logger.info('Removed entry: %s', entry.as_dict())
        return make_response(jsonify(entry.as_dict()), 200)
    else:
        current_app.logger.info('Entry not found for id %s' % id)
        return make_response(jsonify(''), 404)