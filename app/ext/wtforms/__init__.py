from flask_wtf.csrf import CSRFProtect


def init_app(app):
    csrf = CSRFProtect(app)
    return app
