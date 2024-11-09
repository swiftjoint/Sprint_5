from data import UrlPage
from locators import TestConstructorSections


class TestConstructorElements:
    def test_navigate_to_burger_section(self, driver):
        driver.get(UrlPage.PAGE_URL)
        driver.find_element(*TestConstructorSections.BURGER_CONSTRUCTOR_ELEMENT)
        burger_element = driver.find_element(*TestConstructorSections.SELECTED_BURGER_ELEMENT)
        assert burger_element.is_displayed()

    def test_navigate_to_sauces_section(self, driver):
        driver.get(UrlPage.PAGE_URL)
        driver.find_element(*TestConstructorSections.SAUCES_CONSTRUCTOR_ELEMENT).click()
        sauces_element = driver.find_element(*TestConstructorSections.SELECTED_SAUCES_ELEMENT)
        assert sauces_element.is_displayed()

    def test_navigate_to_fillings_section(self, driver):
        driver.get(UrlPage.PAGE_URL)
        driver.find_element(*TestConstructorSections.FILLINGS_CONSTRUCTOR_ELEMENT).click()
        fillings_element = driver.find_element(*TestConstructorSections.SELECTED_FILLINGS_ELEMENT)
        assert fillings_element.is_displayed()
