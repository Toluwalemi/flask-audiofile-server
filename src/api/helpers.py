from src import db
from src.api.models import Song


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
