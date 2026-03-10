from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from utils.logger import get_logger


class SiteFlow:

    COOKIE_ACTIONS = {
        "accept_all": (By.ID, "wt-cli-accept-all-btn"),
        "only_necessary": (By.ID, "wt-cli-accept-btn"),
        "decline_all": (By.ID, "wt-cli-reject-btn"),
    }

    def __init__(self, page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def handle_cookie_banner(self, action: str = "only_necessary"):

        if action not in self.COOKIE_ACTIONS:
            raise ValueError(
                f"Unsupported cookie action: {action}. "
                f"Allowed values: {list(self.COOKIE_ACTIONS.keys())}"
            )

        locator = self.COOKIE_ACTIONS[action]

        self.logger.info(f"Checking cookie banner with action: {action}")

        try:
            if self.page.is_visible(locator):
                self.logger.info("Cookie banner detected.")
                self.page.click(locator)
                self.logger.info(f"Cookie action executed: {action}")
            else:
                self.logger.info("Cookie banner not visible.")
        except TimeoutException:
            self.logger.info("Cookie banner did not appear.")