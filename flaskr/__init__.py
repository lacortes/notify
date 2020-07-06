import os

from flask import Flask
from flask_restful import Api

from config import Config
from .git_handler import HelloWorld

api = Api()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=Config.SECRET_KEY
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    configure_api(app)

    return app


def configure_api(app):
    api.app = app
    api.add_resource(HelloWorld, '/api')

