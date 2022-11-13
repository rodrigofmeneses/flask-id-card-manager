from .companies_controller import companies


def init_app(app):
    app.register_blueprint(companies)
