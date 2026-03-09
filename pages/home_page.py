from config.config import BASE_URL, EXPECTED_HOME_TITLE_KEYWORD, EXPECTED_HOME_URL
from selenium.common.exceptions import TimeoutException
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):

    def go_to_home_page(self):
        self.open(BASE_URL)
        self.wait_for_document_ready()

    def handle_cookie_banner(self, action="accept_all"):
        cookie_actions = {
            "accept_all": HomePageLocators.COOKIE_ACCEPT_ALL_BUTTON,
            "only_necessary": HomePageLocators.COOKIE_ONLY_NECESSARY_BUTTON,
            "decline_all": HomePageLocators.COOKIE_DECLINE_ALL_BUTTON,
        }

        if action not in cookie_actions:
            raise ValueError(
                f"Unsupported cookie action: {action}. "
                f"Use one of: {list(cookie_actions.keys())}"
            )

        locator = cookie_actions[action]

        try:
            if self.is_visible(locator):
                self.logger.info(f"Cookie banner action selected: {action}")
                self.click(locator)
            else:
                self.logger.info("Cookie banner is not visible.")
        except TimeoutException:
            self.logger.info("Cookie banner did not appear.")

    def wait_for_lazy_loaded_sections(self, minimum_section_count=1):
        self.logger.info(
            f"Waiting for at least {minimum_section_count} sections to be loaded."
        )
        self.wait.until(
            lambda driver: len(driver.find_elements(*HomePageLocators.ALL_SECTIONS)) >= minimum_section_count
        )

    def is_home_page_url_correct(self):
        current_url = self.get_current_url().rstrip("/")
        expected_url = EXPECTED_HOME_URL.rstrip("/")
        return current_url == expected_url

    def is_home_page_title_correct(self):
        title = self.get_page_title()
        return EXPECTED_HOME_TITLE_KEYWORD.lower() in title.lower()

    def are_main_blocks_loaded(self):
        header_visible = self.is_visible(HomePageLocators.HEADER)
        main_visible = self.is_visible(HomePageLocators.MAIN)
        footer_visible = self.is_visible(HomePageLocators.FOOTER)
        sections = self.find_all(HomePageLocators.ALL_SECTIONS)

        self.logger.info(
            f"Main blocks status | header={header_visible}, "
            f"main={main_visible}, footer={footer_visible}, "
            f"sections_count={len(sections)}"
        )

        return (
            header_visible and
            main_visible and
            footer_visible and
            len(sections) > 0
        )

    def load_home_page_and_prepare(self, cookie_action="only_necessary", minimum_section_count=1):
        self.go_to_home_page()
        self.handle_cookie_banner(cookie_action)
        self.wait_for_lazy_loaded_sections(minimum_section_count)