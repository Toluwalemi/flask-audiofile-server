from flask import Blueprint, jsonify

audio_blueprint = Blueprint('audio', __name__)


@audio_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
