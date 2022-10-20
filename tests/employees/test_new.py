def test_employee_new_has_form_to_add_employees(client):
    response = client.get('/employees/new')
    assert b'New Employee' in response.data
    assert b'ID' in response.data
    assert b'Name' in response.data
    assert b'Save' in response.data

