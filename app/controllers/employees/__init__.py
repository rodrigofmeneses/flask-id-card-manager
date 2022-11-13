from .employees_controller import employees


def init_app(app):
    app.register_blueprint(employees)
