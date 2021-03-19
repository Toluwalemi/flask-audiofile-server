from src import db
from src.api.models import Song, AudioBook


def re_path(route, view, **kwargs):
    """
    Helper function used in src.api.routes.main_urls.py
    for routing URLs to the appropriate view functions
    """
    return view, route, kwargs


def add_song(name, duration):
    song = Song(
        name=name,
        duration=duration,
    )
    db.session.add(song)
    db.session.commit()
    return song


def add_audiobook(name, duration, author, narrator):
    audiobook = AudioBook(
        name=name,
        duration=duration,
        author=author,
        narrator=narrator
    )
    db.session.add(audiobook)
    db.session.commit()
    return audiobook
