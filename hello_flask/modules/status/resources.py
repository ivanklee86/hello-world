from flask import Blueprint, jsonify, make_response
from hello_flask.helpers.requestid import requestid

status_blueprint = Blueprint('status', __name__, url_prefix='/api/v1/status')

@requestid
@status_blueprint.route('', methods=['GET'])
def status():
    return make_response(jsonify('OK'), 200)
