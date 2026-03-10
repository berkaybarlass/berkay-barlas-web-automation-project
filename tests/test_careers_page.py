from flows.site_flow import SiteFlow
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

        def test_qa_jobs_match_expected_position_department_and_location(self, driver):
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
            careers_page.select_location()
            careers_page.validate_job_cards()

        def test_qa_jobs_filter_results_and_view_role_redirect(self, driver):
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
            careers_page.select_location()
            careers_page.validate_job_cards()
            careers_page.click_apply_button()
            careers_page.is_view_role_redirected_to_expected_lever_url()