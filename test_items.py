import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_checking_the_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert button is not None, "Кнопка не найдена на странице"
