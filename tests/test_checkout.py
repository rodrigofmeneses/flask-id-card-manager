from flask import url_for
from pytest import mark


def test_checkout_page_online(browser):
    browser.visit(url_for('home.index'))
    browser.links.find_by_text('Checkout').click()
    assert browser.url == url_for('checkout.index')
    assert browser.is_text_present('Checkout')

def test_checkout_page_with_employees(browser, employees):
    browser.visit(url_for('checkout.index'))
    assert browser.is_text_present('Rodrigo')
    assert browser.is_text_present('Marta')

def test_checkout_page_with_no_employees(browser):
    browser.visit(url_for('checkout.index'))
    assert browser.is_text_present('No employees to print')

# @mark.current
# def test_select_image_folder(browser):
#     browser.visit(url_for('checkout.index'))
#     assert browser.is_text_present('Image Folder')
#     assert browser.is_text_present('No selected image folder')

# def test_click_select_image_folder_text_change(browser):
#     browser.visit(url_for('checkout.index'))
#     browser.links.find_by_text('Image Folder')
#     assert browser.is_text_present('/some_folder')

