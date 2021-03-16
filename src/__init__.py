import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

# instantiate the db
db = SQLAlchemy()
ma = Marshmallow()


def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    ma.init_app(app)

    # register blueprints
    from src.api.views import audio_blueprint
    app.register_blueprint(audio_blueprint)

    # shell context for flask-cli
    app.shell_context_processor({'app': app, 'db': db})
    return app
