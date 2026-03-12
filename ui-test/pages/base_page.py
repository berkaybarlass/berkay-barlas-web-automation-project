import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import DEFAULT_TIMEOUT, ENABLE_HIGHLIGHT, HIGHLIGHT_DURATION, HIGHLIGHT_STYLE
from utils.logger import get_logger


class BasePage:
    def __init__(self, driver, timeout=DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = get_logger(self.__class__.__name__)

    def open(self, url):
        self.logger.info(f"Navigating to: {url}")
        self.driver.get(url)
        self.wait_for_document_ready()
        self.logger.info(f"Page ready: {url}")

    def wait_for_visibility(self, locator):
        self.logger.info(f"Waiting for visibility of locator: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        self.logger.info(f"Waiting for element to be clickable: {locator}")
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_presence(self, locator):
        self.logger.info(f"Waiting for presence of locator: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_all_presence(self, locator):
        self.logger.info(f"Waiting for all elements presence: {locator}")
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def find(self, locator):
        self.logger.info(f"Finding element: {locator}")
        return self.wait_for_presence(locator)

    def find_all(self, locator):
        self.logger.info(f"Finding all elements: {locator}")
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            self.logger.warning(f"No elements found for locator: {locator}")
            return []

    def is_visible(self, locator):
        try:
            self.wait_for_visibility(locator)
            self.logger.info(f"Element is visible: {locator}")
            return True
        except TimeoutException:
            self.logger.warning(f"Element is not visible: {locator}")
            return False

    def get_current_url(self):
        current_url = self.driver.current_url
        self.logger.info(f"Current URL: {current_url}")
        return current_url

    def get_page_title(self):
        title = self.driver.title
        self.logger.info(f"Page title: {title}")
        return title

    def wait_for_document_ready(self):
        self.logger.info("Waiting for document.readyState to be complete")
        self.wait.until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    def highlight_element(self, element):
        if not ENABLE_HIGHLIGHT:
            return

        self.logger.info("Highlighting element before action")

        original_style = element.get_attribute("style") or ""

        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            f"{original_style}; {HIGHLIGHT_STYLE}"
        )

        time.sleep(HIGHLIGHT_DURATION)

        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            original_style
        )

    def click(self, locator):
        self.logger.info(f"Click action requested for locator: {locator}")
        element = self.wait_for_clickable(locator)
        self.highlight_element(element)
        element.click()
        self.logger.info(f"Clicked on locator: {locator}")

    def click_element(self, element, description="element"):
        self.logger.info(f"Click action requested for: {description}")
        self.highlight_element(element)
        element.click()
        self.logger.info(f"Clicked on: {description}")