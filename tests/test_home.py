from flask import url_for


def test_home_page_online(browser):
    browser.visit(url_for('home.index'))
    assert browser.is_text_present('ID Card Manager')

def test_home_page_with_employees(browser, employees):
    browser.visit(url_for('home.index'))
    assert browser.is_text_present('Rodrigo')
    assert browser.is_text_present('Marta')

def test_home_page_with_no_employees(browser):
    browser.visit(url_for('home.index'))
    assert browser.is_text_present('ID Card Manager')
    assert browser.is_text_present('No registered employees')
