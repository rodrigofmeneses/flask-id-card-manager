from app.ext.database import db
from app.models import Employee, Company


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    company_data = [
        Company(name='UFC'),
        Company(name='UECE'),
    ]
    
    employeer_data = [
        Employee(
            id='1', 
            name='Rodrigo', 
            war_name='Rodrigo Meneses', 
            role='Analista',
            identification='2000510231209',
            admission='26/12/2021',
            company_id=1, 
            to_print=True
        ),
        Employee(
            id='2', 
            name='Marta',
            war_name='Marta Saraiva', 
            role='Processamento de dados',
            identification='2000545321094',
            admission='26/11/2021',
            company_id=1, 
            to_print=True
        ),
        Employee(
            id='3', 
            name='Liz',
            war_name='Maria Liz', 
            role='Contabilista',
            identification='7845645321094',
            admission='26/11/2010',
            company_id=2, 
            to_print=False
        )
    ]
    db.session.bulk_save_objects(company_data)
    db.session.bulk_save_objects(employeer_data)
    db.session.commit()
    return Employee.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))