from app.ext.database import db
from app.models import Employee


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    data = [
        Employee(id='123456', name='Rodrigo'),
        Employee(id='654321', name='Marta')
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Employee.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))