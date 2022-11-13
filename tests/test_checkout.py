from flask import url_for


def test_checkout_page_online(browser):
    browser.visit(url_for("home.index"))
    browser.links.find_by_text("Checkout").click()
    assert browser.url == url_for("checkout.index")
    assert browser.is_text_present("Checkout")


def test_checkout_page_with_employees(browser, employees):
    browser.visit(url_for("checkout.index"))
    assert browser.is_text_present("Rodrigo")
    assert not browser.is_text_present("Marta")