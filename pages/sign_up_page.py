import random
import config
import allure
import string
import secrets

from pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement
from faker import Faker


class SignUpPage(BasePage):
    # Локаторы
    _SIGN_UP_PAGE_LOGO_LOCATOR = "//img[@alt='HackerRank']"
    _SIGN_UP_PAGE_FIRST_AND_LAST_NAME_INPUT_LOCATOR = "//input[@placeholder='First & Last name']"
    _SIGN_UP_PAGE_EMAIL_INPUT_LOCATOR = "//input[@name='email']"
    _SIGN_UP_PAGE_PASSWORD_INPUT_LOCATOR = "//input[@name='password']"
    _SIGN_UP_PAGE_CREATE_ACCOUNT_BUTTON_LOCATOR = "//*[text()='Create An Account']"
    _SIGN_UP_PAGE_CHECK_BOX_LOCATOR = "//*[@class='checkbox-wrap']"
    _SIGN_UP_PAGE_HEY_NAME_TEXT_LOCATOR = "//h1[@class='onboarding-sidebar-heading']"
    _SIGN_UP_PAGE_ERROR_INVALID_EMAIL_ADDRESS_LOCATOR = "//form//*[text()='Invalid email address.']"
    _ON_BOARDING_PAGE_TWO_BUTTONS_BY_FIRST_STEP = "//*[@aria-labelledby='legend-label-intent']//label"
    _ON_BOARDING_PAGE_TWO_BUTTONS_BY_SECOND_STEP = "//*[@aria-labelledby='legend-label-hackerType']//label"
    _ON_BOARDING_PAGE_SKIP_BUTTON_LOCATOR = "//button[@data-analytics = 'SkipOnboarding']"
    _DARK_MODE_MODAL_LOCATOR = "//*[@class='dark-mode-modal']"
    _CROSS_ICON_ON_DARK_MODE_MODAL_LOCATOR = "//*[@class='dark-mode-modal']//*[@data-balloon='Close']"
    _PROFILE_MENU = "//*[@data-analytics = 'NavBarProfileDropDown']"
    _PROFILE_MENU_LOGOUT_BUTTON = "//button[@data-analytics='NavBarProfileDropDownLogout']"
    _LOG_IN_BUTTON_LOCATOR = "//button[text()='Log In']"
    _SIGN_UP_BUTTON_LOCATOR = "//button[text()='Sign Up']"

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.fake = Faker()
        self.FAKE_NAME = self.fake.name()
        self.FAKE_FIRST_NAME = self.FAKE_NAME.split()[0]
        self.FAKE_EMAIL = self.fake.email()
        self.INVALID_EMAIL = "test"
        self.ALPHABET = string.ascii_letters + string.digits + string.punctuation
        self.FAKE_PASSWORD = ''.join(secrets.choice(self.ALPHABET) for _ in range(10))

    @allure.step("Opening Sign Up page")
    def open_sign_up_page(self) -> None:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return self.driver.get(config.url.SIGN_UP)

    @allure.step("Checking user profile")
    def wait_appear_user_profile_button(self) -> WebElement:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.is_visible(self._PROFILE_MENU)

    @allure.step("Checking the absence of a user profile")
    def wait_disappear_user_profile_button(self) -> WebElement:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.is_not_visible(self._PROFILE_MENU)

    @allure.step("Checking the presence Log in button")
    def wait_appear_log_in_button(self) -> WebElement:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.is_visible(self._LOG_IN_BUTTON_LOCATOR)

    @allure.step("Checking the presence Sign Up button")
    def wait_appear_sign_up_button(self) -> WebElement:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.is_visible(self._SIGN_UP_BUTTON_LOCATOR)

    @allure.step("Checking the presence of a text error about invalid email")
    def wait_appear_invalid_email_error(self) -> WebElement:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.is_visible(self._SIGN_UP_PAGE_ERROR_INVALID_EMAIL_ADDRESS_LOCATOR)

    @allure.step("Filling in the name in the first and last name input field")
    def filling_in_the_name_in_the_first_and_last_name_input(self) -> None:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.is_visible(self._SIGN_UP_PAGE_FIRST_AND_LAST_NAME_INPUT_LOCATOR).send_keys(self.FAKE_NAME)

    @allure.step("Filling in the email in the email input field")
    def filling_in_the_valid_email_in_the_email_input(self) -> None:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.is_visible(self._SIGN_UP_PAGE_EMAIL_INPUT_LOCATOR).send_keys(self.FAKE_EMAIL)

    @allure.step("Filling in the invalid email in the email input field")
    def filling_in_the_invalid_email_in_the_email_input(self) -> None:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.is_visible(self._SIGN_UP_PAGE_EMAIL_INPUT_LOCATOR).send_keys(self.INVALID_EMAIL)

    @allure.step("Filling in the password in the password input field")
    def filling_in_the_password_in_the_password_input(self) -> None:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.is_visible(self._SIGN_UP_PAGE_PASSWORD_INPUT_LOCATOR).send_keys(self.FAKE_PASSWORD)

    @allure.step("Click on checkbox agree with policy")
    def click_on_checkbox_agree_with_policy(self) -> None:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.is_visible(self._SIGN_UP_PAGE_CHECK_BOX_LOCATOR).click()

    @allure.step("Click on Create account button")
    def click_on_create_account_button(self) -> None:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.is_visible(self._SIGN_UP_PAGE_CREATE_ACCOUNT_BUTTON_LOCATOR).click()

    @allure.step("Select any answers of the questionnaire on the first step")
    def click_on_any_answers_of_the_questionnaire_on_the_first_step(self) -> None:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        buttons_on_first_step = self.are_visible(self._ON_BOARDING_PAGE_TWO_BUTTONS_BY_FIRST_STEP)
        return random.choice(buttons_on_first_step).click()

    @allure.step("Select any answers of the questionnaire on the second step")
    def click_on_any_answers_of_the_questionnaire_on_the_second_step(self) -> None:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        buttons_on_second_step = self.are_visible(self._ON_BOARDING_PAGE_TWO_BUTTONS_BY_SECOND_STEP)
        return random.choice(buttons_on_second_step).click()

    @allure.step("Click on Skip button")
    def click_on_skip_button(self) -> None:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.is_visible(self._ON_BOARDING_PAGE_SKIP_BUTTON_LOCATOR).click()

    @allure.step("Click on cross icon button for closing dark modal")
    def click_on_cross_icon_button_for_closing_dark_modal(self) -> None:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.is_visible(self._CROSS_ICON_ON_DARK_MODE_MODAL_LOCATOR).click()

    @allure.step("Click on User profile button")
    def click_on_user_profile_button(self) -> None:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.wait_appear_user_profile_button().click()

    @allure.step("Click on User profile Logout button")
    def click_on_user_profile_logout_button(self) -> None:
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.is_visible(self._PROFILE_MENU_LOGOUT_BUTTON).click()

    @allure.step("Get name from webelement")
    def get_name_from_web_element(self) -> str:
        web_element_with_text = self.is_visible(self._SIGN_UP_PAGE_HEY_NAME_TEXT_LOCATOR)
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        return self.get_text_from_web_element(web_element_with_text).split()[1]
