from flask import jsonify, request
from flask_classful import FlaskView
from sqlalchemy import exc

from src import db
from src.api.models import Song


class AudioView(FlaskView):
    """Class-based views for HTTP Methods: POST, GET, PUT & DELETE"""

    def post(self):
        new_audio = {}
        post_data = request.get_json()
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        if not post_data:
            return jsonify(response_object), 400

        if post_data['audioFileType'] == 'song':
            new_audio['audioFileMetadata'] = {'name': post_data.get('audioFileMetadata').get('name'),
                                              'duration': post_data.get('audioFileMetadata').get('duration')
                                              }
            # print(new_audio)
            name = new_audio['audioFileMetadata'].get('name')
            duration = new_audio['audioFileMetadata'].get('duration')
            try:
                song = Song.query.filter_by(name=name).first()
                print(song)
                if not song:
                    db.session.add(Song(name=name, duration=duration))
                    db.session.commit()
                    response_object['status'] = 'success'
                    response_object['message'] = f'{name} was added!'
                    return jsonify(response_object), 200
                else:
                    response_object['message'] = 'This song already exists.'
                    return jsonify(response_object), 400
            except ValueError:
                return jsonify(response_object), 400
            except exc.IntegrityError as e:
                db.session.rollback()
                return jsonify(response_object), 400

    def get(self, audioFileType):
        """Get all users"""
        if audioFileType == 'song':
            response_object = {
                'status': 'success',
                'data': {
                    'songs': [song.to_json() for song in Song.query.all()]
                }
            }
            return jsonify(response_object), 200


class AudioItemView(FlaskView):
    """Class-based views to get a single audioFileType"""

    def get(self, audioFileType, audioFileID):
        response_object = {
            'status': 'fail',
            'message': 'Song does not exist'
        }
        if audioFileType == 'song':
            try:
                song = Song.query.filter_by(id=audioFileID).first()
                if not song:
                    return jsonify(response_object), 400
                else:
                    response_object = {
                        'status': 'success',
                        'data': {
                            'id': song.id,
                            'name': song.name,
                            'duration': song.duration
                        }
                    }
                    return jsonify(response_object), 200
            except ValueError:
                return jsonify(response_object), 400
            except:
                return jsonify(response_object), 500
