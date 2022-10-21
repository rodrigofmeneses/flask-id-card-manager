from pytest import fixture
from app.models import Employee


@fixture(scope='module')
def employee():
    employee = Employee(name='Rodrigo', id=376176)
    return employee

def test_new_employee(employee):
    assert employee.name == 'Rodrigo'
    assert employee.id == 376176

def test_serializer_employee(employee):
    assert employee.serializer() == {'name':'Rodrigo','id':376176}