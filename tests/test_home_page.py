from data.urls import BASE_URL
from flows.site_flow import SiteFlow
from pages.home_page import HomePage


class TestHomePage:

    def test_home_page_is_opened_and_main_blocks_are_loaded(self, driver):
        home_page = HomePage(driver)
        site_flow = SiteFlow(home_page)

        home_page.open(BASE_URL)
        site_flow.handle_cookie_banner("only_necessary")

        assert home_page.is_home_page_url_correct(), \
            f"Expected exact URL to be home page, but got: {home_page.get_current_url()}"

        assert home_page.is_home_page_title_correct(), \
            f"Expected page title to contain expected keyword, but got: {home_page.get_page_title()}"

        assert home_page.are_main_blocks_loaded(), \
            "One or more main blocks are not loaded on the home page."