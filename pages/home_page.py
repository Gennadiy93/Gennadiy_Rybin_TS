from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        # Локаторы
        self.HOME_PAGE_LOGO_LOCATOR = "//img[@alt='HackerRank Logo']"
        self.HOME_PAGE_SIGN_UP_BUTTONS_LOCATOR = "//a[text()='Sign up']"
        self.GET_STARTED_PAGE_TITLE_LOCATOR = "//h1[text()='How do you want to use HackerRank?']"
        self.GET_STARTED_PAGE_PRACTICE_BUTTON_LOCATOR = "//a[@data-action='practice']"
        self.GET_STARTED_PAGE_CREATE_ACCOUNT_BUTTON_LOCATOR = "//a[text()='Create account']"
        self.SIGN_UP_PAGE_LOGO_LOCATOR = "//img[@alt='HackerRank']"
