from .views import checkout


def init_app(app):
    app.register_blueprint(checkout)