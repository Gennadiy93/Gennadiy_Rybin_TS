import random
import allure
import config

from pages.base_page import BasePage
from typing import List
from selenium.webdriver.remote.webelement import WebElement


class HomePage(BasePage):
    # Локаторы
    _HOME_PAGE_LOGO_LOCATOR = "//img[@alt='HackerRank Logo']"
    _HOME_PAGE_SIGN_UP_BUTTONS_LOCATOR = "//a[text()='Sign up']"
    _GET_STARTED_PAGE_TITLE_LOCATOR = "//h1[text()='How do you want to use HackerRank?']"
    _GET_STARTED_PAGE_PRACTICE_BUTTON_LOCATOR = "//a[@data-action='practice']"
    _GET_STARTED_PAGE_CREATE_ACCOUNT_BUTTON_LOCATOR = "//a[text()='Create account']"
    _SIGN_UP_PAGE_LOGO_LOCATOR = "//img[@alt='HackerRank']"

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    @allure.step("Opening home page")
    def open_home_page(self) -> None:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.driver.get(config.url.DOMAIN)

    @allure.step("Opening Get Started page")
    def open_get_started_page(self) -> None:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.driver.get(config.url.GET_STARTED)

    @allure.step("Checking the presence of the HackerRank logo on the home page")
    def wait_appear_logo(self) -> WebElement:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.is_visible(self._HOME_PAGE_LOGO_LOCATOR)

    @allure.step("Checking the display two sign up buttons on the home page")
    def wait_appear_sign_up_buttons(self) -> List[WebElement]:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.are_visible(self._HOME_PAGE_SIGN_UP_BUTTONS_LOCATOR)

    @allure.step("Checking title on opening get started page")
    def wait_appear_title(self) -> WebElement:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.is_visible(self._GET_STARTED_PAGE_TITLE_LOCATOR)

    @allure.step("Checking the logo is presence on sign up page")
    def wait_appear_logo_on_sign_up_page(self) -> WebElement:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.is_visible(self._SIGN_UP_PAGE_LOGO_LOCATOR)

    @allure.step("Click one of two buttons sign up")
    def click_any_of_two_sign_up_buttons(self) -> None:
        sign_up_buttons = self.are_visible(self._HOME_PAGE_SIGN_UP_BUTTONS_LOCATOR)
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return random.choice(sign_up_buttons).click()

    @allure.step("Select free user for registrations")
    def click_practice_button(self) -> None:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.is_visible(self._GET_STARTED_PAGE_PRACTICE_BUTTON_LOCATOR).click()

    @allure.step("Select Create Account")
    def click_create_account_button(self) -> None:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.is_visible(self._GET_STARTED_PAGE_CREATE_ACCOUNT_BUTTON_LOCATOR).click()

    @allure.step("Get current url")
    def get_current_url(self) -> None:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.driver.current_url
