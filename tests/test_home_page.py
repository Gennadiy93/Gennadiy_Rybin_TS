import random

import allure
import pytest

import config
from pages.home_page import HomePage


class TestHomePage:

    def test_home_page_must_have_logo_hacker_rank(self, setup):
        """
        Checking the presence of the HackerRank logo on the home page
        """
        with allure.step("Driver generation and opening home page"):
            driver, wait = setup
            page = HomePage(driver, wait)
            page.open_page(config.url.DOMAIN)

        with allure.step("Checking the presence of the HackerRank logo on the home page"):
            assert page.is_visible(page.HOME_PAGE_LOGO_LOCATOR), f"Missing hackerRank logo on home page"

    def test_home_page_must_have_two_buttons_sign_up(self, setup):
        """
        Checking the display of two sign up buttons on the home page
        """
        with allure.step("Driver generation and opening home page"):
            driver, wait, = setup
            page = HomePage(driver, wait)
            page.open_page(config.url.DOMAIN)

        with allure.step("Checking the display two sign up buttons on the home page"):
            sign_up_buttons = page.are_visible(page.HOME_PAGE_SIGN_UP_BUTTONS_LOCATOR)
            assert len(sign_up_buttons) == 2, f"Missing on or two buttons sign up on home page"

    def test_open_get_started_page_by_click_any_of_sign_up_buttons(self, setup):
        """
        Checking the opening of the page /get-started after clicking on one of the sign up buttons on the home page
        """
        with allure.step("Driver generation and opening home page"):
            driver, wait = setup
            page = HomePage(driver, wait)
            page.open_page(config.url.DOMAIN)
        with allure.step("Displaying sign up buttons and click one of them"):
            sign_up_buttons = page.are_visible(page.HOME_PAGE_SIGN_UP_BUTTONS_LOCATOR)
            random.choice(sign_up_buttons).click()
        with allure.step("Checking title on opening page"):
            page.is_visible(page.GET_STARTED_PAGE_TITLE_LOCATOR)
        with allure.step("Checking the opening of the page /get-started after clicking on one of the sign up buttons on the home page"):
            assert driver.current_url == config.url.GET_STARTED, f"Opening page url doesn't match with /get-started/"

    def test_open_registration_page_for_free_account(self, setup):
        """
        Checking the opening of the auth/signup page after selecting free account on the /get-started page
        """
        with allure.step("Driver generation and opening get started page"):
            driver, wait = setup
            page = HomePage(driver, wait)
            page.open_page(config.url.GET_STARTED)
        with allure.step("Select free user for registrations"):
            page.is_visible(page.GET_STARTED_PAGE_PRACTICE_BUTTON_LOCATOR).click()
        with allure.step("Click Create Account button"):
            page.is_visible(page.GET_STARTED_PAGE_CREATE_ACCOUNT_BUTTON_LOCATOR).click()
        with allure.step("Checking the logo is presence"):
            page.is_visible(page.SIGN_UP_PAGE_LOGO_LOCATOR)
        with allure.step("Checking the opening of the auth/signup page after selecting free account on the /get-started page"):
            assert driver.current_url == config.url.SIGN_UP, f"Opening page url doesn't match with /auth/signup"

