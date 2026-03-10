from flows.site_flow import SiteFlow
from pages.base_page import BasePage
from pages.careers_page import CareersPage


class TestCareersPage:

        def test_careers_page(self, driver):
            careers_page = CareersPage(driver)
            site_flow = SiteFlow(careers_page)

            careers_page.open_page()
            site_flow.handle_cookie_banner("only_necessary")
            careers_page.click_see_all_teams()
            careers_page.wait_for_positions_to_load()
            careers_page.click_open_qa_positions()
            careers_page.is_quality_assurance_filter_selected()
            assert careers_page.are_job_postings_present(), \
                "No job postings were found for Quality Assurance filter."
