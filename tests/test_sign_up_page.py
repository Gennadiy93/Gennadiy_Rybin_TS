from pages.sign_up_page import SignUpPage


class TestSignUpPage:
    def test_registration_free_user_using_valid_data_before_first_step(self, setup):
        """
        Checking free account registration using valid data before the first step of onboarding
        """
        driver, wait = setup
        page = SignUpPage(driver, wait)
        page.open_sign_up_page()

        page.filling_in_the_name_in_the_first_and_last_name_input()
        page.filling_in_the_valid_email_in_the_email_input()
        page.filling_in_the_password_in_the_password_input()
        page.filling_in_the_password_in_the_password_input()
        page.click_on_checkbox_agree_with_policy()
        page.click_on_create_account_button()

        assert page.get_name_from_web_element() == page.FAKE_FIRST_NAME, f"Displaying text doesn't match with generated name"

    def test_registration_free_user_using_valid_data_with_skip_anketa(self, setup):
        """
        Checking free account registration using valid data with skip of the questionnaire
        """
        driver, wait = setup
        page = SignUpPage(driver, wait)
        page.open_sign_up_page()

        page.filling_in_the_name_in_the_first_and_last_name_input()
        page.filling_in_the_valid_email_in_the_email_input()
        page.filling_in_the_password_in_the_password_input()
        page.click_on_checkbox_agree_with_policy()
        page.click_on_create_account_button()

        page.click_on_any_answers_of_the_questionnaire_on_the_first_step()
        page.click_on_any_answers_of_the_questionnaire_on_the_second_step()
        page.click_on_skip_button()
        page.click_on_cross_icon_button_for_closing_dark_modal()

        assert page.wait_appear_user_profile_button, f"Missing profile menu on dashboard page"

    def test_registration_free_user_using_invalid_email(self, setup):
        """
        Checking free account registration using invalid email
        """
        driver, wait = setup
        page = SignUpPage(driver, wait)
        page.open_sign_up_page()

        page.filling_in_the_name_in_the_first_and_last_name_input()
        page.filling_in_the_invalid_email_in_the_email_input()
        page.filling_in_the_password_in_the_password_input()

        assert page.wait_appear_invalid_email_error, f"Missing or incorrect error text message"

    def test_registration_free_user_using_valid_data_and_sign_out(self, setup):
        """
        Checking for free account registration and then sign out
        """
        driver, wait = setup
        page = SignUpPage(driver, wait)
        page.open_sign_up_page()

        page.filling_in_the_name_in_the_first_and_last_name_input()
        page.filling_in_the_valid_email_in_the_email_input()
        page.filling_in_the_password_in_the_password_input()
        page.click_on_checkbox_agree_with_policy()
        page.click_on_create_account_button()

        page.click_on_any_answers_of_the_questionnaire_on_the_first_step()
        page.click_on_any_answers_of_the_questionnaire_on_the_second_step()
        page.click_on_skip_button()
        page.click_on_cross_icon_button_for_closing_dark_modal()

        page.click_on_user_profile_button()
        page.click_on_user_profile_logout_button()
        page.wait_disappear_user_profile_button()

        assert page.wait_appear_log_in_button() and page.wait_appear_sign_up_button(), f"Missing Log in or Sign up buttons after Sign out"
