from flask import url_for


class TestCompanyCreate:
    def test_companies(self, browser, companies):
        browser.visit(url_for('companies.index'))
        assert browser.is_text_present('UFC')

    def test_add_company(self, browser, companies):
        browser.visit(url_for('home.index'))
        browser.links.find_by_text('Add Company').click()
        browser.fill('name', 'UFC')
        browser.find_by_value('Save').click()
        browser.visit(url_for('companies.index'))
        assert browser.is_text_present('UFC')
        