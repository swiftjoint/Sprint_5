from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestNavigationLocators, TestAutorisation


class TestNavigationToPersonalAndConstructor:
    def test_navigate_to_personal_area(self, driver, login):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestAutorisation.AUTHORIZED_USER))
        driver.find_element(*TestAutorisation.PERSONAL_CABINET_BUTTON).click()
        profile_element = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestNavigationLocators.PROFILE_LINK_LOCATOR)
        )
        assert profile_element.is_displayed()

    def test_navigate_to_constructor(self, driver, login):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestAutorisation.AUTHORIZED_USER))
        driver.find_element(*TestAutorisation.PERSONAL_CABINET_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestNavigationLocators.PROFILE_LINK_LOCATOR)
        )
        driver.find_element(*TestNavigationLocators.CONSTRUCTOR_BUTTON).click()
        burger_element = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestNavigationLocators.BURGER_ASSEMBLY_HEADER))
        assert burger_element.is_displayed()

    def test_navigate_to_homepage_via_logo(self, driver, login):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestAutorisation.AUTHORIZED_USER))
        driver.find_element(*TestAutorisation.PERSONAL_CABINET_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestNavigationLocators.PROFILE_LINK_LOCATOR))
        driver.find_element(*TestNavigationLocators.STELLAR_BURGERS_LOGO_LOCATOR).click()
        burger_element = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestNavigationLocators.BURGER_ASSEMBLY_HEADER))
        assert burger_element.is_displayed()
