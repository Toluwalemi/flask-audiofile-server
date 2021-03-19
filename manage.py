import unittest

import coverage
from flask.cli import FlaskGroup

from src import db, create_app
from src.api.models import Song

COV = coverage.coverage(
    branch=True,
    include='src/api/*',
    omit=[
        'src/api/tests/*',
        'src/config.py',
    ]
)
COV.start()

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def test():
    """Runs the tests without code coverage."""
    tests = unittest.TestLoader().discover('src/api/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@cli.command()
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('src/api/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    return 1


# @cli.command()
# def seed_db():
#     """Seeds the database."""
#     db.session.add(Song(name='hold_me_down', duration=180))
#     db.session.add(Song(name='pull_me_up', duration=220))
#     db.session.commit()


if __name__ == '__main__':
    cli()
