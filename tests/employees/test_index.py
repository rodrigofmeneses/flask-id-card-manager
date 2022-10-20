def test_employees_page_when_GET_then_response_correctly(client):
    response = client.get('/employees')
    assert response.status_code == 200
    assert b'Employees' in response.data

def test_employees_page_has_a_list_with_all_employees(client, new_employees):
    response = client.get('/employees')
    assert b'Rodrigo' in response.data
    assert b'Marta' in response.data

