import config
from pages.home_page import HomePage


class TestHomePage:

    def test_home_page_must_have_logo_hacker_rank(self, browser):
        """
        Checking the presence of the HackerRank logo on the home page
        """

        driver, wait = browser
        page = HomePage(driver, wait)
        page.open_home_page()

        assert page.wait_appear_logo(), f"Missing hackerRank logo on home page"

    def test_home_page_must_have_two_buttons_sign_up(self, browser):
        """
        Checking the display of two sign up buttons on the home page
        """
        driver, wait = browser
        page = HomePage(driver, wait)
        page.open_home_page()

        sign_up_buttons = page.wait_appear_sign_up_buttons()
        assert len(sign_up_buttons) == 2, f"Missing on or two buttons sign up on home page"

    def test_open_get_started_page_by_click_any_of_sign_up_buttons(self, browser):
        """
        Checking the opening of the page /get-started after clicking on one of the sign up buttons on the home page
        """
        driver, wait = browser
        page = HomePage(driver, wait)
        page.open_home_page()

        page.click_any_of_two_sign_up_buttons()
        page.wait_appear_title()

        assert page.get_current_url() == config.url.GET_STARTED, f"Opening page url doesn't match with /get-started/"

    def test_open_registration_page_for_free_account(self, browser):
        """
        Checking the opening of the auth/signup page after selecting free account on the /get-started page
        """
        driver, wait = browser
        page = HomePage(driver, wait)
        page.open_get_started_page()

        page.click_practice_button()
        page.click_create_account_button()
        page.wait_appear_logo_on_sign_up_page()

        assert page.get_current_url() == config.url.SIGN_UP, f"Opening page url doesn't match with /auth/signup"

