from dynaconf import FlaskDynaconf
from flask import Flask


def create_app(**config):
    app = Flask(__name__)
    FlaskDynaconf(app) 
    app.config.load_extensions(
        "EXTENSIONS"
    )
    app.config.update(config)
    return app