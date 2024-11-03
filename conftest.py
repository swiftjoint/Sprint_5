import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from locators import TestAutorisation


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*TestAutorisation.LOGIN_BUTTON).click()
    driver.find_element(*TestAutorisation.EMAIL_INPUT_XPATH).send_keys("zhigulin_12@gmail.com")
    driver.find_element(*TestAutorisation.PASSWORD_INPUT_XPATH).send_keys("Qwe123")
    driver.find_element(*TestAutorisation.LOGIN_BUTTON_VIEW).click()
    yield driver


@pytest.fixture()
def login_lk(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*TestAutorisation.PERSONAL_CABINET_BUTTON).click()
    driver.find_element(*TestAutorisation.EMAIL_INPUT_XPATH).send_keys("zhigulin_12@gmail.com")
    driver.find_element(*TestAutorisation.PASSWORD_INPUT_XPATH).send_keys("Qwe123")
    driver.find_element(*TestAutorisation.LOGIN_BUTTON_VIEW).click()
    yield driver


@pytest.fixture()
def log_in_via_reg_btn(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*TestAutorisation.LOGIN_BUTTON).click()
    driver.find_element(*TestAutorisation.REGISTER_BUTTON).click()
    driver.find_element(*TestAutorisation.REGISTRATION_FORM_LOGIN_BUTTON).click()
    driver.find_element(*TestAutorisation.EMAIL_INPUT_XPATH).send_keys("zhigulin_12@gmail.com")
    driver.find_element(*TestAutorisation.PASSWORD_INPUT_XPATH).send_keys("Qwe123")
    driver.find_element(*TestAutorisation.LOGIN_BUTTON_VIEW).click()
    yield driver


@pytest.fixture()
def log_in_via_reset_btn(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*TestAutorisation.LOGIN_BUTTON).click()
    driver.find_element(*TestAutorisation.RESET_PASSWORD_BUTTON).click()
    driver.find_element(*TestAutorisation.REGISTRATION_FORM_LOGIN_BUTTON).click()
    driver.find_element(*TestAutorisation.EMAIL_INPUT_XPATH).send_keys("zhigulin_12@gmail.com")
    driver.find_element(*TestAutorisation.PASSWORD_INPUT_XPATH).send_keys("Qwe123")
    driver.find_element(*TestAutorisation.LOGIN_BUTTON_VIEW).click()
    yield driver
