# pylint: disable=no-else-return
from flask import Blueprint, jsonify, make_response, current_app, request
from app.helpers.requestid import requestid
from app.extensions.sqlalchemy import db
from .models import Entry
from .schema import EntrySchema

# pylint: disable=invalid-name
entries_blueprint = Blueprint('entries', __name__, url_prefix='/api/v1/entries')
ENTRY_SCHEMA = EntrySchema()
ENTRIES_SCHEMA = EntrySchema(many=True)

@requestid
@entries_blueprint.route('', methods=['GET'])
def list_entries():
    entries = Entry.query.all()
    result = ENTRIES_SCHEMA.dump(entries)
    return make_response(jsonify(result.data), 200)

@requestid
@entries_blueprint.route('', methods=['POST'])
def add_entry():
    entry_from_request = ENTRY_SCHEMA.load(request.json)
    print(entry_from_request.data)
    entry = Entry(description=entry_from_request.data.description,
                  comment=entry_from_request.data.comment)
    db.session.add(entry)
    db.session.commit()
    inserted_record = ENTRY_SCHEMA.dump(entry).data
    current_app.logger.info('Added entry: %s' % inserted_record)
    return make_response(jsonify(inserted_record), 200)

@requestid
@entries_blueprint.route('/<list_id>', methods=['GET'])
def list_entry(list_id):
    found_entry = ENTRY_SCHEMA.dump(Entry.query.get(list_id)).data

    if found_entry:
        current_app.logger.info('Entry found for id %s: %s' % (list_id, found_entry))
        return make_response(jsonify(found_entry), 200)
    else:
        current_app.logger.info('Entry not found for id %s' % list_id)
        return make_response(jsonify(''), 404)


@requestid
@entries_blueprint.route('/<list_id>', methods=['POST'])
def update_entry(list_id):
    # Check to see if object exists.
    Entry.query.get_or_404(list_id)

    # Create query, discarding optional values.
    (entry_from_request, _) = ENTRY_SCHEMA.load(request.json)
    (update, _) = ENTRY_SCHEMA.dump(entry_from_request)
    update = {k: v for k, v in update.items() if v is not None}

    # Update row.
    Entry.query.filter_by(id=list_id).update(update)
    db.session.commit()

    updated_entry = ENTRY_SCHEMA.dump(db.session.query(Entry).get(list_id)).data
    current_app.logger.info('Updated entry %s with data: %s' % (list_id, updated_entry))
    return make_response(jsonify(updated_entry), 200)

@requestid
@entries_blueprint.route('/<list_id>', methods=['DELETE'])
def remove_entry(list_id):
    # Check to see if object exists.
    entry = Entry.query.get_or_404(list_id)
    db.session.delete(entry)
    db.session.commit()
    current_app.logger.info('Removed entry: %s', list_id)
    return ('', 204)
