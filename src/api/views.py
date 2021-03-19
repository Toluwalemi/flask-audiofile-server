import sqlalchemy
from flask import jsonify, request
from flask_classful import FlaskView
from sqlalchemy import exc

from src import db
from src.api.models import Song, AudioBook, Podcast


class AudioView(FlaskView):
    """Class-based views for HTTP Methods: POST, GET, PUT & DELETE"""

    def post(self):
        new_song = {}
        post_data = request.get_json()
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        if not post_data:
            return jsonify(response_object), 400

        if post_data['audioFileType'] == 'song':
            new_song['audioFileMetadata'] = {'name': post_data.get('audioFileMetadata').get('name'),
                                             'duration': post_data.get('audioFileMetadata').get('duration')
                                             }
            name = new_song['audioFileMetadata'].get('name')
            duration = new_song['audioFileMetadata'].get('duration')
            try:
                song = Song.query.filter_by(name=name).first()
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
            except:
                return jsonify(response_object), 500

        if post_data['audioFileType'] == 'audiobook':
            new_song['audioFileMetadata'] = {'name': post_data.get('audioFileMetadata').get('name'),
                                             'duration': post_data.get('audioFileMetadata').get('duration'),
                                             'author': post_data.get('audioFileMetadata').get('author'),
                                             'narrator': post_data.get('audioFileMetadata').get('narrator'),
                                             }
            name = new_song['audioFileMetadata'].get('name')
            duration = new_song['audioFileMetadata'].get('duration')
            author = new_song['audioFileMetadata'].get('author')
            narrator = new_song['audioFileMetadata'].get('author')
            try:
                audiobook = AudioBook.query.filter_by(name=name).first()
                if not audiobook:
                    db.session.add(AudioBook(name=name, duration=duration, author=author, narrator=narrator))
                    db.session.commit()
                    response_object['status'] = 'success'
                    response_object['message'] = f'{name} was added!'
                    return jsonify(response_object), 200
                else:
                    response_object['message'] = 'This audiobook already exists.'
                    return jsonify(response_object), 400
            except ValueError:
                return jsonify(response_object), 400
            except exc.IntegrityError as e:
                db.session.rollback()
                return jsonify(response_object), 400
            except:
                return jsonify(response_object), 500

        if post_data['audioFileType'] == 'podcast':
            new_song['audioFileMetadata'] = {'name': post_data.get('audioFileMetadata').get('name'),
                                             'duration': post_data.get('audioFileMetadata').get('duration'),
                                             'host': post_data.get('audioFileMetadata').get('host'),
                                             'participants': post_data.get('audioFileMetadata').get('participants'),
                                             }
            print(new_song)
            name = new_song['audioFileMetadata'].get('name')
            duration = new_song['audioFileMetadata'].get('duration')
            host = new_song['audioFileMetadata'].get('host')
            participants = new_song['audioFileMetadata'].get('participants')
            print(participants)
            try:
                podcast = Podcast.query.filter_by(name=name).first()
                if not podcast:
                    db.session.add(Podcast(name=name, duration=duration, host=host, participants=participants))
                    db.session.commit()
                    response_object['status'] = 'success'
                    response_object['message'] = f'{name} was added!'
                    return jsonify(response_object), 200
                else:
                    response_object['message'] = 'This audiobook already exists.'
                    return jsonify(response_object), 400
            except ValueError:
                return jsonify(response_object), 400
            except exc.IntegrityError as e:
                db.session.rollback()
                return jsonify(response_object), 400
            # except BaseException as e:
            #     print(e)
            #     return jsonify(response_object), 500

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

        if audioFileType == 'audiobook':
            response_object = {
                'status': 'success',
                'data': {
                    'audiobooks': [audiobook.to_json() for audiobook in AudioBook.query.all()]
                }
            }
            return jsonify(response_object), 200


class AudioItemView(FlaskView):
    """Class-based views to get a single audioFileType"""

    def get(self, audioFileType, audioFileID):
        response_object = {
            'status': 'fail',
            'message': 'Does not exist'
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

        if audioFileType == 'audiobook':
            try:
                audiobook = AudioBook.query.filter_by(id=audioFileID).first()
                if not audiobook:
                    return jsonify(response_object), 400
                else:
                    response_object = {
                        'status': 'success',
                        'data': {
                            'id': audiobook.id,
                            'name': audiobook.name,
                            'duration': audiobook.duration
                        }
                    }
                    return jsonify(response_object), 200
            except ValueError:
                return jsonify(response_object), 400
            except:
                return jsonify(response_object), 500

    def patch(self, audioFileType, audioFileID):
        """Update json"""
        response_object = {
            'status': 'success',
            'message': 'Updated!'
        }
        post_data = request.get_json()
        if audioFileType == 'song':
            song = Song.query.get(audioFileID)
            if post_data.get('audioFileMetadata').get('name'):
                song.name = post_data['audioFileMetadata']['name']
            if post_data.get('audioFileMetadata').get('duration'):
                song.duration = post_data['audioFileMetadata']['duration']
            db.session.add(song)
            db.session.commit()

            return response_object, 200

        if audioFileType == 'audiobook':
            audiobook = AudioBook.query.get(audioFileID)
            if post_data.get('audioFileMetadata').get('name'):
                audiobook.name = post_data['audioFileMetadata']['name']
            if post_data.get('audioFileMetadata').get('duration'):
                audiobook.duration = post_data['audioFileMetadata']['duration']
            if post_data.get('audioFileMetadata').get('duration'):
                audiobook.duration = post_data['audioFileMetadata']['author']
            if post_data.get('audioFileMetadata').get('duration'):
                audiobook.duration = post_data['audioFileMetadata']['narrator']
            db.session.add(audiobook)
            db.session.commit()

            return response_object, 200

    def delete(self, audioFileType, audioFileID):
        """Delete a particular id"""
        if audioFileType == 'song':
            try:
                song = Song.query.filter_by(id=audioFileID).first_or_404()
                db.session.delete(song)
                db.session.commit()
                return jsonify({"status": "deleted"}), 200
            except sqlalchemy.orm.exc.NoResultFound:
                return jsonify({"detail": "No result found"}), 400
            except:
                return jsonify({"detail": "No result found"}), 500

        if audioFileType == 'audiobook':
            try:
                audiobook = AudioBook.query.filter_by(id=audioFileID).first_or_404()
                db.session.delete(audiobook)
                db.session.commit()
                return jsonify({"status": "deleted"}), 200
            except sqlalchemy.orm.exc.NoResultFound:
                return jsonify({"detail": "No result found"}), 400
            except:
                return jsonify({"detail": "No result found"}), 500
