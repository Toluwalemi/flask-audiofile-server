from flask import Blueprint, jsonify, request

from src import db
from src.api.models import Song

audio_blueprint = Blueprint('audio', __name__)


@audio_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


@audio_blueprint.route('/audio', methods=['POST'])
def add_audio_type():
    file_type = 'song'
    new_audio = {}
    if file_type:
        post_data = request.get_json()
        new_audio['audioFileType'] = file_type
        new_audio['audioFileMetadata'] = {'name': post_data.get('audioFileMetadata').get('name'),
                                          'duration': post_data.get('audioFileMetadata').get('duration')
                                          }
        name = new_audio['audioFileMetadata'].get('name')
        duration = new_audio['audioFileMetadata'].get('duration')
        db.session.add(Song(name=name, duration=duration))
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': f'{name} was added!'
        }
        return jsonify(response_object), 200

# class Audio(MethodView):
#     # route_base = '/v1'
#
#     def post(self):
#         audioFileType = 'song'
#         if audioFileType:
#             post_data = request.get_json()
#             audioFileMetadata = {}
#             audioFileMetadata['name'] = post_data.get('name')
#             audioFileMetadata['duration'] = post_data.get('duration')
#             db.session.add(Song(name=audioFileMetadata['name'], duration=audioFileMetadata['duration']))
#             db.session.commit()
#             return 200
