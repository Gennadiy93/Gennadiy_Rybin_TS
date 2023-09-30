from pages.base_page import BasePage


class SignUpPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        # Локаторы
        self.SIGN_UP_PAGE_LOGO_LOCATOR = "//img[@alt='HackerRank']"
        self.SIGN_UP_PAGE_FIRST_AND_LAST_NAME_INPUT_LOCATOR = "//input[@placeholder='First & Last name']"
        self.SIGN_UP_PAGE_EMAIL_INPUT_LOCATOR = "//input[@name='email']"
        self.SIGN_UP_PAGE_PASSWORD_INPUT_LOCATOR = "//input[@name='password']"
        self.SIGN_UP_PAGE_CREATE_ACCOUNT_BUTTON_LOCATOR = "//*[text()='Create An Account']"
        self.SIGN_UP_PAGE_CHECK_BOX_LOCATOR = "//*[@class='checkbox-wrap']"
        self.SIGN_UP_PAGE_HEY_NAME_TEXT_LOCATOR = "//h1[@class='onboarding-sidebar-heading']"
        self.SIGN_UP_PAGE_ERROR_INVALID_EMAIL_ADDRESS_LOCATOR = "//form//*[text()='Invalid email address.']"
        self.ON_BOARDING_PAGE_TWO_BUTTONS_BY_FIRST_STEP = "//*[@aria-labelledby='legend-label-intent']//label"
        self.ON_BOARDING_PAGE_TWO_BUTTONS_BY_SECOND_STEP = "//*[@aria-labelledby='legend-label-hackerType']//label"
        self.ON_BOARDING_PAGE_SKIP_BUTTON_LOCATOR = "//button[@data-analytics = 'SkipOnboarding']"
        self.DARK_MODE_MODAL_LOCATOR = "//*[@class='dark-mode-modal']"
        self.CROSS_ICON_ON_DARK_MODE_MODAL_LOCATOR = "//*[@class='dark-mode-modal']//*[@data-balloon='Close']"
        self.PROFILE_MENU = "//*[@data-analytics = 'NavBarProfileDropDown']"
        self.PROFILE_MENU_LOGOUT_BUTTON = "//button[@data-analytics='NavBarProfileDropDownLogout']"
        self.LOG_IN_BUTTON_LOCATOR = "//button[text()='Log In']"
        self.SIGN_UP_BUTTON_LOCATOR = "//button[text()='Sign Up']"

