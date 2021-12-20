import pytest
from selenium import webdriver
import time

def test_add_button(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    add_button = browser.find_element_by_css_selector("#add_to_basket_form .btn")
    assert add_button != None, 'Add button not found'