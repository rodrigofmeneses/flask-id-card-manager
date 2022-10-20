def test_employees_slash_id_has_details_of_employee(client, new_employees):
    response = client.get('/employees/123456')
    assert b'Rodrigo' in response.data
    assert b'123456' in response.data
