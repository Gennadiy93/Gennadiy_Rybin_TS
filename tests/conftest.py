import pytest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def setup(get_webdriver):
    driver = get_webdriver
    wait = WebDriverWait(driver, 10)
    yield driver, wait
    driver.quit()


@pytest.fixture
def get_chrome_options():
    """
    use options.add_argument("--headless")  to hide the browser

    """
    options = Options()
    options.add_argument('chrome')
    options.add_argument('window-size=1300,1080')
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=options)
    return driver


@pytest.fixture
def browser():
    bro = "Firefox"
    if bro == "Chrome":
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['browserVersion'] = "117.0"
        capabilities['selenoid:options'] = {
            "enableVNC": False
        }
        options = webdriver.ChromeOptions()
        options.add_argument('window-size=1920,1080')
        options.set_capability("browserVersion", "117.0")
        options.set_capability("selenoid:options", {
            "enableVNC": True
        })
        driver = webdriver.Remote(
            command_executor=f"http://192.168.0.210:4444/wd/hub",
            options=options
        )

        wait = WebDriverWait(driver, 10)
        yield driver, wait
        driver.quit()
    elif bro == "Firefox":
        capabilities = DesiredCapabilities.FIREFOX.copy()
        capabilities['browserVersion'] = "118.0"
        capabilities['selenoid:options'] = {
            "enableVNC": False,
            "enableVideo": False
        }

        options = webdriver.FirefoxOptions()
        options.add_argument('window-size=19200,1080')
        options.set_capability("browserVersion", "117.0")
        options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": False
        })
        driver = webdriver.Remote(
            command_executor=f"http://192.168.0.210:4444/wd/hub",
            options=options
        )

        wait = WebDriverWait(driver, 10)
        yield driver, wait
        driver.quit()
