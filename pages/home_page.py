from config.config import EXPECTED_HOME_TITLE_KEYWORD, EXPECTED_HOME_URL
from selenium.common.exceptions import TimeoutException
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from data.urls import BASE_URL


class HomePage(BasePage):

    def go_to_home_page(self):
        self.open(BASE_URL)
        self.wait_for_document_ready()

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

    def load_home_page_and_prepare(self, minimum_section_count=1):
        self.go_to_home_page()
        self.wait_for_lazy_loaded_sections(minimum_section_count)