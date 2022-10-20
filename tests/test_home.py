def test_home_page_when_GET_then_response_correctly(client):
    '''
    GIVEN a Flask application configured for testing
    WHEN the "/" page is requested (GET)
    THEN check that the response is valid
    '''
    response = client.get('/')
    assert response.status_code == 200
    assert b'ID Card Manager' in response.data

def test_home_page_when_POST_then_response_correctly(client):
    '''
    GIVEN a Flask application configured for testing
    WHEN the '/' page is posted to (POST)
    THEN check that a "405" status code is returned
    '''
    response = client.post('/')
    assert response.status_code == 405
    assert b'ID Card Manager' not in response.data

def test_when_acess_home_page_is_visible_a_list_of_employees(client, employees):
    response = client.get('/')
    assert b'Rodrigo' in response.data
    assert b'Marta' in response.data

def test_each_employee_has_edit_and_delete_buttons(client, employees):
    response = client.get('/')
    assert b'123456/edit">Edit' in response.data
    assert b'123456/delete">Delete' in response.data
