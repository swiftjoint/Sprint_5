from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestAutorisation, TestNavigationLocators


class TestUserLogout:
    def test_logout_successful(self, driver, login):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestAutorisation.AUTHORIZED_USER))
        driver.find_element(*TestAutorisation.PERSONAL_CABINET_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestNavigationLocators.LOGOUT_BUTTON)).click()
        button_element = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestAutorisation.LOGIN_BUTTON_VIEW))
        assert button_element.is_displayed()
