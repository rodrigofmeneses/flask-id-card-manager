import os
from app import create_app
from app.ext.database import db
from app.models import Employee, Company
from pytest import fixture
from splinter import Browser
from dotenv import load_dotenv

load_dotenv('.env.test')


@fixture(scope="class")
def browser():
    app = create_app()
    app.config.update(
        TESTING = True,
        DEBUG = os.getenv('FLASK_DEBUG'),
        SQLALCHEMY_DATABASE_URI = os.getenv('FLASK_SQLALCHEMY_DATABASE_URI'),
        SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
    )
    context = app.test_request_context()
    context.push()
    with app.test_client():
        db.create_all()
        yield Browser("flask", app=app)
        db.drop_all()
        db.session.remove()


@fixture()
def employees(companies):
    employees = [
        Employee(name="Rodrigo", id=123456, company_id=1, to_print=True),
        Employee(name="Marta", id=654321, company_id=2, to_print=False),
    ]
    db.session.bulk_save_objects(employees)
    db.session.commit()
    yield employees
    for employee in Employee.query.all():
        db.session.delete(employee)
    db.session.commit()


@fixture()
def companies():
    companies = [Company(name="UFC"), Company(name="UECE")]
    db.session.bulk_save_objects(companies)
    db.session.commit()
    yield companies
    for company in Company.query.all():
        db.session.delete(company)
    db.session.commit()
