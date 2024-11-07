import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from locators import TestAutorisation
from data import UrlPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    driver.get(UrlPage.PAGE_URL)
    driver.find_element(*TestAutorisation.LOGIN_BUTTON).click()
    driver.find_element(*TestAutorisation.EMAIL_INPUT_XPATH).send_keys("zhigulin_12@gmail.com")
    driver.find_element(*TestAutorisation.PASSWORD_INPUT_XPATH).send_keys("Qwe123")
    driver.find_element(*TestAutorisation.LOGIN_BUTTON_VIEW).click()
