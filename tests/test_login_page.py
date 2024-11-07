from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import UrlPage
from helpers import generate_random_name, generate_random_email, generate_random_password
from locators import TestAutorisation


class TestRegistrationAndLogin:

    def test_successful_registration_with_valid_name_email_and_password(self, driver):
        driver.get(UrlPage.PAGE_URL)
        driver.find_element(*TestAutorisation.LOGIN_BUTTON).click()
        driver.find_element(*TestAutorisation.REGISTER_BUTTON).click()
        random_name = generate_random_name()
        random_email = generate_random_email()
        random_password = generate_random_password()
        driver.find_element(*TestAutorisation.NAME_INPUT_XPATH).send_keys(random_name)
        driver.find_element(*TestAutorisation.EMAIL_INPUT_XPATH).send_keys(random_email)
        driver.find_element(*TestAutorisation.PASSWORD_INPUT_XPATH).send_keys(random_password)
        driver.find_element(*TestAutorisation.REGISTRATION_BUTTON_LOGIN).click()
        login_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestAutorisation.LOGIN_BUTTON_VIEW))
        assert login_button.is_displayed()

    def test_registration_with_invalid_password(self, driver):
        driver.get(UrlPage.PAGE_URL)
        driver.find_element(*TestAutorisation.LOGIN_BUTTON).click()
        driver.find_element(*TestAutorisation.REGISTER_BUTTON).click()
        random_name = generate_random_name()
        random_email = generate_random_email()
        driver.find_element(*TestAutorisation.NAME_INPUT_XPATH).send_keys(random_name)
        driver.find_element(*TestAutorisation.EMAIL_INPUT_XPATH).send_keys(random_email)
        driver.find_element(*TestAutorisation.PASSWORD_INPUT_XPATH).send_keys("qwe")
        driver.find_element(*TestAutorisation.REGISTRATION_BUTTON_LOGIN).click()
        password_error = driver.find_element(*TestAutorisation.PASSWORD_ERROR)
        assert password_error.is_displayed()

    def test_successful_login_button_click(self, driver, login):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located
            (TestAutorisation.AUTHORIZED_USER))
        element = driver.find_element(*TestAutorisation.AUTHORIZED_USER)
        assert element.is_displayed()

    def test_button_login_from_personal_cabinet(self, driver):
        driver.get(UrlPage.PAGE_URL)
        driver.find_element(*TestAutorisation.PERSONAL_CABINET_BUTTON).click()
        driver.find_element(*TestAutorisation.EMAIL_INPUT_XPATH).send_keys("zhigulin_12@gmail.com")
        driver.find_element(*TestAutorisation.PASSWORD_INPUT_XPATH).send_keys("Qwe123")
        driver.find_element(*TestAutorisation.LOGIN_BUTTON_VIEW).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located
            (TestAutorisation.AUTHORIZED_USER))
        element = driver.find_element(*TestAutorisation.AUTHORIZED_USER)
        assert element.is_displayed()

    def test_login_via_registration_form_button(self, driver):
        driver.get(UrlPage.PAGE_URL)
        driver.find_element(*TestAutorisation.LOGIN_BUTTON).click()
        driver.find_element(*TestAutorisation.REGISTER_BUTTON).click()
        driver.find_element(*TestAutorisation.REGISTRATION_FORM_LOGIN_BUTTON).click()
        driver.find_element(*TestAutorisation.EMAIL_INPUT_XPATH).send_keys("zhigulin_12@gmail.com")
        driver.find_element(*TestAutorisation.PASSWORD_INPUT_XPATH).send_keys("Qwe123")
        driver.find_element(*TestAutorisation.LOGIN_BUTTON_VIEW).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located
            (TestAutorisation.AUTHORIZED_USER))
        element = driver.find_element(*TestAutorisation.AUTHORIZED_USER)
        assert element.is_displayed()

    def test_login_via_reset_password_form_button(self, driver):
        driver.get(UrlPage.PAGE_URL)
        driver.find_element(*TestAutorisation.LOGIN_BUTTON).click()
        driver.find_element(*TestAutorisation.RESET_PASSWORD_BUTTON).click()
        driver.find_element(*TestAutorisation.REGISTRATION_FORM_LOGIN_BUTTON).click()
        driver.find_element(*TestAutorisation.EMAIL_INPUT_XPATH).send_keys("zhigulin_12@gmail.com")
        driver.find_element(*TestAutorisation.PASSWORD_INPUT_XPATH).send_keys("Qwe123")
        driver.find_element(*TestAutorisation.LOGIN_BUTTON_VIEW).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located
            (TestAutorisation.AUTHORIZED_USER))
        element = driver.find_element(*TestAutorisation.AUTHORIZED_USER)
        assert element.is_displayed()
