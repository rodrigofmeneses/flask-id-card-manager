from .views import employees


def init_app(app):
    app.register_blueprint(employees)