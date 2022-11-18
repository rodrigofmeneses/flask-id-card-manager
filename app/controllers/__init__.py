from app.controllers.checkout_controller import checkout
from app.controllers.companies_controller import companies
from app.controllers.employees_controller import employees
from app.controllers.home_controller import home


def init_app(app):
    app.register_blueprint(checkout)
    app.register_blueprint(companies)
    app.register_blueprint(employees)
    app.register_blueprint(home)