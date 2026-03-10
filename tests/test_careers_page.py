import pytest

from data.expected_content import EXPECTED_JOB_DEPARTMENT, EXPECTED_JOB_LOCATION
from flows.site_flow import SiteFlow
from pages.careers_page import CareersPage


class TestCareersPage:

    @pytest.fixture
    def qa_filtered_careers_page(self, driver):
        careers_page = CareersPage(driver)
        site_flow = SiteFlow(careers_page)
        careers_page.open_page()
        site_flow.handle_cookie_banner("accept_all")
        careers_page.click_see_all_teams()
        careers_page.wait_for_positions_to_load()
        careers_page.click_open_qa_positions()
        assert careers_page.is_quality_assurance_filter_selected(), \
            "Quality Assurance filter is not selected after clicking QA positions."
        assert careers_page.are_job_postings_present(), \
            "No job postings were found for Quality Assurance filter."
        return careers_page

    def test_qa_jobs_match_position_and_location(self, qa_filtered_careers_page):
        #qa_filtered_careers_page.select_location()
        #qa_filtered_careers_page.validate_job_cards()

        qa_filtered_careers_page.select_location()
        job_cards = qa_filtered_careers_page.get_job_cards_data()

        for job in job_cards:
            assert EXPECTED_JOB_DEPARTMENT in job["title"], \
                f"Unexpected job title: '{job['title']}'"
            assert EXPECTED_JOB_LOCATION in job["location"], \
                f"Unexpected job location: '{job['location']}'"

    def test_qa_jobs_filter_and_view_role_redirect(self, qa_filtered_careers_page):
        qa_filtered_careers_page.select_location()
        qa_filtered_careers_page.validate_job_cards()
        qa_filtered_careers_page.click_apply_button()
        assert qa_filtered_careers_page.is_view_role_redirected_to_expected_lever_url()