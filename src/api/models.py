from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import validates

from src import db


class TimestampMixin(object):
    """Model mixin for created and updated"""
    uploaded_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(),
                           server_onupdate=db.func.now())


class DurationMixin(object):
    """Model mixin for Duration"""
    duration = db.Column(db.Integer, nullable=False)

    @validates('duration')
    def validate_duration(self, key, duration):
        if duration < 1:
            raise ValueError('The duration must be a positive number')
        return duration


class Song(TimestampMixin, DurationMixin, db.Model):
    """Model to store details of Audio File Type 'Song'. """
    id = db.Column(db.Integer,
                   primary_key=True, nullable=False,
                   autoincrement=True, unique=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __repr__(self):
        return f"{__class__.__name__}({self.id}, " \
               f"{self.name}, {self.duration}, {self.uploaded_at})"

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'duration': self.duration,
            'uploaded_at': self.uploaded_at
        }


class Podcast(TimestampMixin, DurationMixin, db.Model):
    """Model to store details of Audio File Type 'Podcast'. """
    id = db.Column(db.Integer,
                   primary_key=True, nullable=False,
                   autoincrement=True, unique=True)
    name = db.Column(db.String(100), nullable=False)
    host = db.Column(db.String(100), nullable=False)
    participants = db.Column(JSON)

    def __init__(self, name, duration, host, participants):
        self.name = name
        self.duration = duration
        self.host = host
        self.participants = participants

    def __repr__(self):
        return f"{__class__.__name__}({self.name}, {self.duration}\
         {self.host}, {self.participants['fullname']})"

    @validates('participants')
    def validate_participants(self, key, participants):
        if participants is not None:
            for participant in participants['fullname']:
                if len(participant) > 100:
                    raise ValueError('String cannot be more than 100 characters')
            if len(participants['fullname']) > 10:
                raise ValueError('Maximum of 10 participants possible')
            return participants


class AudioBook(TimestampMixin, DurationMixin, db.Model):
    """Model to store details of Audio File Type 'AudioBook'. """
    id = db.Column(db.Integer,
                   primary_key=True, nullable=False,
                   autoincrement=True, unique=True)
    name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    narrator = db.Column(db.String(100), nullable=False)

    def __init__(self, name, duration, author, narrator):
        self.name = name
        self.author = author
        self.duration = duration
        self.narrator = narrator

    def __repr__(self):
        return f"{__class__.__name__}({self.name}, {self.author}, \
         {self.duration}, {self.narrator}"

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'duration': self.duration,
            'author': self.author,
            'narrator': self.narrator,
            'uploaded_at': self.uploaded_at
        }
