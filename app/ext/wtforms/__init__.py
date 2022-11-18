from flask_wtf.csrf import CSRFProtect


def init_app(app):
    CSRFProtect(app)
    return app
