from flask import url_for


class TestCreate:
    def test_when_user_register_new_employee_then_main_page_must_show_new_employee(self, browser):
        browser.visit(url_for('home.index'))
        browser.links.find_by_text('Add Employee').click()
        browser.fill('name', 'Rodrigo')
        browser.fill('id', '123456')
        browser.find_by_value('Save').click()
        assert browser.url == url_for('home.index')
        assert browser.is_text_present('Rodrigo')
        assert browser.is_text_present('123456')


class TestRead:
    def test_when_acess_employees_page_with_no_employees_registered_must_see_a_message(self, browser):
        browser.visit(url_for('employees.index'))
        assert browser.is_text_present('No registered employees')

    def test_when_acess_employees_page_must_see_a_list_of_employees(self, browser, employees):
        browser.visit(url_for('employees.index'))
        assert browser.is_text_present("Rodrigo")
        assert browser.is_text_present("Marta")
    
    def test_when_acess_employees_slash_id_then_details_of_employee_is_visible(self, browser, employees):
        browser.visit(url_for('employees.detail', id=123456))
        assert browser.is_text_present("Rodrigo")
        assert browser.is_text_present("123456")


# class TestUpdate:
#     ...

# class TestDelete:
#     ...