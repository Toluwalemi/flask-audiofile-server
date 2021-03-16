from marshmallow import EXCLUDE

from src import ma
from src.api.models import Song, Participant, AudioBook


class SongSchema(ma.ModelSchema):
    class Meta:
        model = Song
        unknown = EXCLUDE


class PodcastSchema(ma.ModelSchema):
    class Meta:
        model = Song
        unknown = EXCLUDE


class ParticipantSchema(ma.ModelSchema):
    class Meta:
        model = Participant
        unknown = EXCLUDE


class AudioBookSchema(ma.ModelSchema):
    class Meta:
        model = AudioBook
        unknown = EXCLUDE
