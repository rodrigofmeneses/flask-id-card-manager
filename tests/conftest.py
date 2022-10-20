from app import create_app
from app.ext.database import db
from app.models import Employee
from pytest import fixture
from dotenv import load_dotenv


load_dotenv('.env.test')

@fixture(scope='module')
def client():
    app = create_app(FORCE_ENV_FOR_DYNACONF="testing")
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()
        db.session.remove()

@fixture()
def new_employees():
    employees = [
        Employee(name='Rodrigo', id='123456'), Employee(name='Marta', id='654321')
    ]
    db.session.bulk_save_objects(employees)
    db.session.commit()
    yield employees
    for employee in Employee.query.all():
        db.session.delete(employee)
    db.session.commit()