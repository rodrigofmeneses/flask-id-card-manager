from app.models import Employee
from pytest import fixture


@fixture(scope='module')
def new_employee():
    employee = Employee(name='Rodrigo', id='376176')
    return employee

def test_new_employee(new_employee):
    '''
    GIVEN a Employee model
    WHEN a new Employee is created
    THEN check the id and name fields are defined correctly
    '''
    assert new_employee.name == 'Rodrigo'
    assert new_employee.id == '376176'

def test_serializer_employee(new_employee):
    '''
    GIVEN a Employee model
    WHEN a new Employee is created
    THEN check serializer method
    '''
    assert new_employee.serializer() == {'name':'Rodrigo','id':'376176'}