from flask import jsonify, request
from flask_classful import FlaskView

from src import db
from src.api.models import Song


class AudioView(FlaskView):
    """Class-based views for HTTP Methods: POST, GET, PUT & DELETE"""

    def post(self):
        new_audio = {}
        post_data = request.get_json()
        if post_data['audioFileType'] == 'song':
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
