from app.ext.database import db
from app.models import Employee, Company
from faker import Faker
from random import choice


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    fake = Faker()

    company_data = [
        Company(name="UFC"),
        Company(name="UECE"),
    ]

    employeer_data = [
        Employee(
            id=i,
            name=fake.name(),
            # war_name='Rodrigo Meneses',
            # role='Analista',
            # identification='2000510231209',
            # admission='26/12/2021',
            company_id=choice([1, 2]),
            to_print=choice([True, False]),
        )
        for i in range(25)
    ]
    db.session.bulk_save_objects(company_data)
    db.session.bulk_save_objects(employeer_data)
    db.session.commit()
    return Employee.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))
