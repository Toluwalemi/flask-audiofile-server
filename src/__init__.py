import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# instantiate the app

app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(app)


class TimestampMixin(object):
    uploaded_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(),
                           server_onupdate=db.func.now())


class DurationMixin(object):
    duration = db.Column(db.Integer, nullable=False)


class Song(TimestampMixin, DurationMixin, db.Model):
    """Model to store details of Audio File Type 'Song'. """
    id = db.Column(db.Integer,
                   primary_key=True, nullable=False,
                   autoincrement=True, unique=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name, duration):
        self.name = name

    def __repr__(self):
        return f"{__class__.__name__}({self.name}"


class Podcast(TimestampMixin, db.Model):
    """Model to store details of Audio File Type 'Podcast'. """
    id = db.Column(db.Integer,
                   primary_key=True, nullable=False,
                   autoincrement=True, unique=True)
    name = db.Column(db.String(100), nullable=False)
    host = db.Column(db.String(100), nullable=False)
    participants = db.relationship("Participant",
                                   backref=db.backref('podcast', uselist=False))

    def __init__(self, name, host, participants):
        self.name = name
        self.host = host
        self.participants = list(map(Participant, participants))

    def __repr__(self):
        return f"{__class__.__name__}({self.name}"


class Participant(TimestampMixin, db.Model):
    """Model to store a list of strings for participants which
    is needed in Podcast model. """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    podcast_id = db.Column(db.ForeignKey('podcast.id',
                                         ondelete='CASCADE',
                                         onupdate='CASCADE'),
                           nullable=True)


class AudioBook(TimestampMixin, db.Model):
    """Model to store details of Audio File Type 'AudioBook'. """
    id = db.Column(db.Integer,
                   primary_key=True, nullable=False,
                   autoincrement=True, unique=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    narrator = db.Column(db.String(100), nullable=False)

    def __init__(self, title, author, duration):
        self.name = title
        self.author = author

    def __repr__(self):
        return f"{__class__.__name__}({self.name}"


@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
