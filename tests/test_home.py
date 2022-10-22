from flask import url_for

from tests.conftest import browser


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

def test_button_to_employees(browser):
    browser.visit(url_for('home.index'))
    browser.links.find_by_text('Employees').click()
    assert browser.url == url_for('employees.index')

def test_button_to_company(browser):
    browser.visit(url_for('home.index'))
    browser.links.find_by_text('Companies').click()
    assert browser.url == url_for('companies.index')