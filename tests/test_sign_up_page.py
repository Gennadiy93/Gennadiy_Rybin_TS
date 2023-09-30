import random

import allure

import config
from pages.sign_up_page import SignUpPage
from faker import Faker
import string
import secrets


class TestSignUpPage:

    def test_registration_free_user_using_valid_data_before_first_step(self, setup):
        """
        Checking free account registration using valid data before the first step of onboarding
        """
        with allure.step("Driver generation and opening Sign up page"):
            driver, wait = setup
            page = SignUpPage(driver, wait)
            page.open_page(config.url.SIGN_UP)
        with allure.step("Generate valid data for registration"):
            fake = Faker()
            fake_name = fake.name()
            fake_email = fake.email()
            alphabet = string.ascii_letters + string.digits + string.punctuation
            fake_password = ''.join(secrets.choice(alphabet) for _ in range(10))
        with allure.step("Filling in the name in the first and last name input field"):
            page.is_visible(page.SIGN_UP_PAGE_FIRST_AND_LAST_NAME_INPUT_LOCATOR).send_keys(fake_name)
        with allure.step("Filling in the email in the email input field"):
            page.is_visible(page.SIGN_UP_PAGE_EMAIL_INPUT_LOCATOR).send_keys(fake_email)
        with allure.step("Filling in the password in the password input field"):
            page.is_visible(page.SIGN_UP_PAGE_PASSWORD_INPUT_LOCATOR).send_keys(fake_password)
        with allure.step("Click on checkbox agree with policy"):
            page.is_visible(page.SIGN_UP_PAGE_CHECK_BOX_LOCATOR).click()
        with allure.step("Click on Create account button"):
            page.is_visible(page.SIGN_UP_PAGE_CREATE_ACCOUNT_BUTTON_LOCATOR).click()
        with allure.step("Checking a name is presence and get name from webelement"):
            web_element_with_text = page.is_visible(page.SIGN_UP_PAGE_HEY_NAME_TEXT_LOCATOR)
            all_text = page.get_text_from_web_element(web_element_with_text)
        with allure.step("Checking generated name match with text from web element"):
            assert all_text.split()[1] == fake_name.split()[0], f"Displaying text doesn't match with generated name"

    def test_registration_free_user_using_valid_data_with_skip_anketa(self, setup):
        """
        Checking free account registration using valid data with skip of the questionnaire
        """
        with allure.step("Driver generation and opening Sign up page"):
            driver, wait = setup
            page = SignUpPage(driver, wait)
            page.open_page(config.url.SIGN_UP)
        with allure.step("Generate valid data for registration"):
            fake = Faker()
            fake_name = fake.name()
            fake_email = fake.email()
            alphabet = string.ascii_letters + string.digits + string.punctuation
            fake_password = ''.join(secrets.choice(alphabet) for _ in range(10))
        with allure.step("Filling in the name in the first and last name input field"):
            page.is_visible(page.SIGN_UP_PAGE_FIRST_AND_LAST_NAME_INPUT_LOCATOR).send_keys(fake_name)
        with allure.step("Filling in the email in the email input field"):
            page.is_visible(page.SIGN_UP_PAGE_EMAIL_INPUT_LOCATOR).send_keys(fake_email)
        with allure.step("Filling in the password in the password input field"):
            page.is_visible(page.SIGN_UP_PAGE_PASSWORD_INPUT_LOCATOR).send_keys(fake_password)
        with allure.step("Click on checkbox agree with policy"):
            page.is_visible(page.SIGN_UP_PAGE_CHECK_BOX_LOCATOR).click()
        with allure.step("Click on Create account button"):
            page.is_visible(page.SIGN_UP_PAGE_CREATE_ACCOUNT_BUTTON_LOCATOR).click()
        with allure.step("Select any answers of the questionnaire on the first step"):
            buttons_by_first_step = page.are_visible(page.ON_BOARDING_PAGE_TWO_BUTTONS_BY_FIRST_STEP)
            random.choice(buttons_by_first_step).click()
        with allure.step("Select any answers of the questionnaire on the second step"):
            buttons_by_second_step = page.are_visible(page.ON_BOARDING_PAGE_TWO_BUTTONS_BY_SECOND_STEP)
            random.choice(buttons_by_second_step).click()
        with allure.step("Click on Skip button"):
            page.is_visible(page.ON_BOARDING_PAGE_SKIP_BUTTON_LOCATOR).click()
        with allure.step("Closing dark modal pop up"):
            page.is_visible(page.CROSS_ICON_ON_DARK_MODE_MODAL_LOCATOR).click()
        with allure.step("Checking the presence of a user profile"):
            assert page.is_visible(page.PROFILE_MENU), f"Missing profile menu on dashboard page"

    def test_registration_free_user_using_invalid_email(self, setup):
        """
        Checking free account registration using invalid email
        """
        with allure.step("Driver generation and opening Sign up page"):
            driver, wait = setup
            page = SignUpPage(driver, wait)
            page.open_page(config.url.SIGN_UP)
        with allure.step("Generate valid name and password and invalid email for registration"):
            fake = Faker()
            fake_name = fake.name()
            invalid_email = "test"
            alphabet = string.ascii_letters + string.digits + string.punctuation
            fake_password = ''.join(secrets.choice(alphabet) for _ in range(10))
        with allure.step("Filling in the name in the first and last name input field"):
            page.is_visible(page.SIGN_UP_PAGE_FIRST_AND_LAST_NAME_INPUT_LOCATOR).send_keys(fake_name)
        with allure.step("Filling in the invalid email in the email input field"):
            page.is_visible(page.SIGN_UP_PAGE_EMAIL_INPUT_LOCATOR).send_keys(invalid_email)
        with allure.step("Filling in the password in the password input field"):
            page.is_visible(page.SIGN_UP_PAGE_PASSWORD_INPUT_LOCATOR).send_keys(fake_password)
        with allure.step("Checking the presence of a text error"):
            assert page.is_visible(page.SIGN_UP_PAGE_ERROR_INVALID_EMAIL_ADDRESS_LOCATOR), f"Missing or incorrect error text message"

    def test_registration_free_user_using_valid_data_and_sign_out(self, setup):
        """
        Checking for free account registration and then sign out
        """
        with allure.step("Driver generation and opening Sign up page"):
            driver, wait = setup
            page = SignUpPage(driver, wait)
            page.open_page(config.url.SIGN_UP)
        with allure.step("Generate valid data for registration"):
            fake = Faker()
            fake_name = fake.name()
            fake_email = fake.email()
            alphabet = string.ascii_letters + string.digits + string.punctuation
            fake_password = ''.join(secrets.choice(alphabet) for _ in range(10))
        with allure.step("Filling in the name in the first and last name input field"):
            page.is_visible(page.SIGN_UP_PAGE_FIRST_AND_LAST_NAME_INPUT_LOCATOR).send_keys(fake_name)
        with allure.step("Filling in the email in the email input field"):
            page.is_visible(page.SIGN_UP_PAGE_EMAIL_INPUT_LOCATOR).send_keys(fake_email)
        with allure.step("Filling in the password in the password input field"):
            page.is_visible(page.SIGN_UP_PAGE_PASSWORD_INPUT_LOCATOR).send_keys(fake_password)
        with allure.step("Click on checkbox agree with policy"):
            page.is_visible(page.SIGN_UP_PAGE_CHECK_BOX_LOCATOR).click()
        with allure.step("Click on Create account button"):
            page.is_visible(page.SIGN_UP_PAGE_CREATE_ACCOUNT_BUTTON_LOCATOR).click()
        with allure.step("Select any answers of the questionnaire on the first step"):
            buttons_by_first_step = page.are_visible(page.ON_BOARDING_PAGE_TWO_BUTTONS_BY_FIRST_STEP)
            random.choice(buttons_by_first_step).click()
        with allure.step("Select any answers of the questionnaire on the second step"):
            buttons_by_second_step = page.are_visible(page.ON_BOARDING_PAGE_TWO_BUTTONS_BY_SECOND_STEP)
            random.choice(buttons_by_second_step).click()
        with allure.step("Click on Skip button"):
            page.is_visible(page.ON_BOARDING_PAGE_SKIP_BUTTON_LOCATOR).click()
        with allure.step("Closing dark modal pop up"):
            page.is_visible(page.CROSS_ICON_ON_DARK_MODE_MODAL_LOCATOR).click()
        with allure.step("Click on User profile button"):
            page.is_visible(page.PROFILE_MENU).click()
        with allure.step("Click on Logout button"):
            page.is_visible(page.PROFILE_MENU_LOGOUT_BUTTON).click()
        with allure.step("Checking the absence of a user profile"):
            page.is_not_visible(page.PROFILE_MENU)
        with allure.step("Checking the presence Log in button and Sign up buttons"):
            assert page.is_visible(page.LOG_IN_BUTTON_LOCATOR) and page.is_visible(page.SIGN_UP_BUTTON_LOCATOR), f"Missing Log in or Sign up buttons after Sign out"








