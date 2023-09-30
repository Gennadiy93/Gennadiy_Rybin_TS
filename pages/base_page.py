from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open_page(self, url: str) -> None:
        driver = self.driver
        return driver.get(url)

    def get_page_title(self) -> str:
        driver = self.driver
        return driver.title

    def is_visible(self, locator: str) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))

    def is_not_visible(self, locator: str) -> WebElement:
        return self.wait.until(EC.invisibility_of_element_located((By.XPATH, locator)))

    def are_visible(self, locator: str) -> List[WebElement]:
        return self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, locator)))

    @staticmethod
    def get_text_from_web_element(element: WebElement) -> str:
        return str(element.text).strip()