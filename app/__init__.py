from flask import Flask
from app.controllers import init_app as controlers_init
from app.ext.commands import init_app as commands_init
from app.ext.database import init_app as database_init
from app.ext.wtforms import init_app as wtforms_init


def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()
    controlers_init(app)
    commands_init(app)
    database_init(app)
    wtforms_init(app)
    return app
