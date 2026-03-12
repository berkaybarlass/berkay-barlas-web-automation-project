from config.config import EXPECTED_HOME_TITLE_KEYWORD, EXPECTED_HOME_URL
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):

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