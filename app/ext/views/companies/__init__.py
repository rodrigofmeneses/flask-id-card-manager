from .views import companies


def init_app(app):
    app.register_blueprint(companies)