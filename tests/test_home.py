from flask import url_for


def test_when_acess_home_page_then_page_must_be_online(browser):
    '''
    GIVEN a Flask application configured for testing
    WHEN the "/" page is requested (GET)
    THEN check that the response is valid
    '''
    browser.visit(url_for('home.index'))
    assert browser.is_text_present('ID Card Manager')

def test_when_acess_home_page_then_page_must_be_a_list_of_new_employees(browser, employees):
    browser.visit(url_for('home.index'))
    assert browser.is_text_present('Rodrigo')
    assert browser.is_text_present('Marta')

def test_when_acess_home_page_with_no_employees_registered_must_see_a_message(browser):
    browser.visit(url_for('home.index'))
    assert browser.is_text_present('ID Card Manager')
    assert browser.is_text_present('No registered employees')
