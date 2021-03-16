from flask_testing import TestCase

from src import app, db


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('src.config.TestingConfig')
        return app

    def setUp(self):
        """Setup for each test function called"""
        db.create_all()
        db.session.commit()

    def tearDown(self):
        """Teardown for each test function called"""
        db.session.remove()
        db.drop_all()
