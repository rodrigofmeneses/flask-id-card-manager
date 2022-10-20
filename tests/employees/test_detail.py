def test_when_acess_employees_slash_id_then_details_of_employee_is_visible(client, employees):
    response = client.get('/employees/123456')
    assert b'Rodrigo' in response.data
    assert b'123456' in response.data
