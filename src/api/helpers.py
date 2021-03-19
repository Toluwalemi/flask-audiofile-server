from src import db
from src.api.models import Song, AudioBook, Podcast


def re_path(route, view, **kwargs):
    """
    Helper function used in src.api.routes.main_urls.py
    for routing URLs to the appropriate view functions
    :param route: url -> str
    :param view: view func -> function
    :param kwargs: extra dicts
    :return:
    """
    return view, route, kwargs


def add_song(name, duration):
    """
    Helper function to add a song to db
    :param name: song's name -> str
    :param duration: length of the song -> int
    :return: song
    """
    song = Song(
        name=name,
        duration=duration,
    )
    db.session.add(song)
    db.session.commit()

    return song


def add_audiobook(name, duration, author, narrator):
    """
    Helper function to add an audiobook to database
    :param name: name of audiobook -> str
    :param duration: length of audiobook -> int
    :param author: name of author -> str
    :param narrator: name of narrator -> str
    :return: audiobook
    """
    audiobook = AudioBook(
        name=name,
        duration=duration,
        author=author,
        narrator=narrator
    )
    db.session.add(audiobook)
    db.session.commit()

    return audiobook


def add_podcast(name, duration, host, participants=None):
    podcast = Podcast(
        name=name,
        duration=duration,
        host=host,
        participants=participants
    )
    db.session.add(podcast)
    db.session.commit()

    return podcast
