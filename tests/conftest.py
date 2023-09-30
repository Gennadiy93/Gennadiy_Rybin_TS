import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def setup(get_webdriver):
    driver = get_webdriver
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds
    yield driver, wait
    driver.quit()


@pytest.fixture
def get_chrome_options():
    """
    use options.add_argument("--headless")  to hide the browser

    """
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('window-size=1300,1080')

    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=options)
    return driver
