import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# instantiate the db

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    with app.app_context():
        extensions(app)

        # register blueprints
        from src.api.routes.urls import bootstrap_routes
        bootstrap_routes(app, route_prefix='/api/v1')

    # shell context for flask-cli
    app.shell_context_processor({'app': app, 'db': db})
    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    # from profile.database import db, migrate
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    return None
