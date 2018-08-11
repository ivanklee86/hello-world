from flask import Blueprint, jsonify, make_response
from app.helpers.requestid import requestid

# pylint: disable=invalid-name
status_blueprint = Blueprint('status', __name__, url_prefix='/api/v1/status')

@requestid
@status_blueprint.route('', methods=['GET'])
def status():
    return make_response(jsonify('OK'), 200)
