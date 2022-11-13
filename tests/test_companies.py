from flask import url_for


class TestCompanyCreate:
    def test_add_company(self, browser, companies):
        browser.visit(url_for("companies.index"))
        browser.links.find_by_text("Add Company").click()
        browser.fill("name", "UFC")
        browser.find_by_value("Save").click()
        browser.visit(url_for("companies.index"))
        assert browser.is_text_present("UFC")


class TestCompanyRead:
    def test_companies_page_with_no_companies(self, browser):
        browser.visit(url_for("companies.index"))
        assert browser.is_text_present("No registered companies")

    def test_companies_page_with_many_companies(self, browser, companies):
        browser.visit(url_for("companies.index"))
        assert browser.is_text_present("UFC")
        assert browser.is_text_present("UECE")

    def test_company_detail_page(self, browser, companies):
        browser.visit(url_for("companies.detail", id=1))
        assert browser.is_text_present("UFC")


class TestCompanyUpdate:
    def test_edit_company_page(self, browser, companies):
        browser.visit(url_for("companies.index"))
        assert browser.is_text_present("UFC")

        browser.links.find_by_text("Edit").click()
        assert browser.url == url_for("companies.edit", id=1)

        browser.fill("name", "UNIFOR")
        browser.find_by_value("Save").click()
        assert browser.url == url_for("companies.index")
        assert browser.is_text_present("UNIFOR")


class TestCompanyDelete:
    def test_delete_company(self, browser, companies):
        browser.visit(url_for("companies.index"))
        assert browser.is_text_present("UFC")

        browser.links.find_by_text("Delete").click()
        assert browser.is_text_present("Rodrigo") == False
