def test_new_employee(employee):
    assert employee.name == 'Rodrigo'
    assert employee.id == 376176

def test_serializer_employee(employee):
    assert employee.serializer() == {'name':'Rodrigo','id':376176}