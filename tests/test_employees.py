from flask import url_for
from pytest import mark


class TestEmployeeCreate:
    def test_add_employee(self, browser, employees, companies):
        browser.visit(url_for('employees.index'))
        browser.links.find_by_text('Add Employee').click()
        browser.fill('id', '333333')
        browser.fill('name', 'Meneses')
        browser.fill('war_name', 'Meneses')
        browser.fill('role', 'Auxiliar')
        browser.fill('identification', '123456789')
        browser.fill('admission', '12/08/2021')
        browser.select('company', '1')
        browser.find_by_value('Save').click()
        assert browser.is_text_present('Meneses')
        assert browser.is_text_present('333333')
        assert browser.is_text_present('UFC')
    
    @mark.current
    def test_add_employee_with_same_id(self, browser, employees):
        browser.visit(url_for('employees.index'))
        browser.links.find_by_text('Add Employee').click()
        browser.fill('id', '123456')
        browser.fill('name', 'Paulo')
        browser.fill('war_name', 'Meneses')
        browser.fill('role', 'Auxiliar')
        browser.fill('identification', '123456789')
        browser.fill('admission', '12/08/2021')
        browser.select('company', '1')
        browser.find_by_value('Save').click()
        assert browser.url == url_for('employees.create')
        assert browser.is_text_present('Employee has exist')


class TestEmployeeRead:
    def test_employees_page_with_no_employees(self, browser):
        browser.visit(url_for('employees.index'))
        assert browser.is_text_present('No registered employees')

    def test_employees_page_with_many_employees(self, browser, employees):
        browser.visit(url_for('employees.index'))
        assert browser.is_text_present("Rodrigo")
        assert browser.is_text_present("Marta")

    def test_employee_detail_page(self, browser, employees):
        browser.visit(url_for('employees.detail', id=123456))
        assert browser.is_text_present("Rodrigo")
        assert browser.is_text_present("123456")


class TestEmployeeUpdate:
    def test_edit_employee_page(self, browser, employees):
        browser.visit(url_for('employees.index'))

        assert browser.is_text_present('Rodrigo')
        assert browser.is_text_present('123456') 

        browser.links.find_by_text('Edit').click()
        assert browser.url == url_for('employees.edit', id=123456)
        browser.fill('name', 'Meneses')
        browser.fill('war_name', 'Meneses')
        browser.fill('role', 'Auxiliar')
        browser.fill('identification', '123456789')
        browser.fill('admission', '12/08/2021')
        browser.select('company', '1')
        browser.find_by_value('Save').click()

        assert browser.url == url_for('employees.index')
        assert browser.is_text_present('Meneses')

class TestEmployeeDelete:
    def test_delete_employee(self, browser, employees):
        browser.visit(url_for('employees.index'))

        assert browser.is_text_present('Rodrigo')
        assert browser.is_text_present('123456') 

        browser.links.find_by_text('Delete').click()
        assert browser.is_text_present('Rodrigo') == False
        assert browser.is_text_present('123456') == False

