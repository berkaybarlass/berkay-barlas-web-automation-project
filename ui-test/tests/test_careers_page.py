import pytest

from data.expected_content import EXPECTED_JOB_DEPARTMENT, EXPECTED_JOB_LOCATION
from flows.site_flow import SiteFlow
from pages.careers_page import CareersPage


class TestCareersPage:

    @pytest.fixture
    def careers_page_qa_filtered(self, driver):
        careers_page = CareersPage(driver)
        site_flow = SiteFlow(careers_page)
        careers_page.open_page()
        site_flow.handle_cookie_banner("accept_all")
        careers_page.click_see_all_teams()
        careers_page.wait_for_positions_to_load()
        careers_page.click_open_qa_positions()
        return careers_page

    def test_qa_filter_is_active_and_jobs_are_listed(self, careers_page_qa_filtered):
        assert careers_page_qa_filtered.is_quality_assurance_filter_selected(), \
            "Quality Assurance filter is not selected after clicking QA positions."
        assert careers_page_qa_filtered.are_job_postings_present(), \
            "No job postings were found for Quality Assurance filter."

    def test_qa_jobs_match_position_and_location(self, careers_page_qa_filtered):
        careers_page_qa_filtered.select_location()
        job_cards = careers_page_qa_filtered.get_job_cards_data()

        for job in job_cards:
            assert EXPECTED_JOB_DEPARTMENT in job["title"], \
                f"Unexpected job title: '{job['title']}'"
            assert EXPECTED_JOB_LOCATION in job["location"], \
                f"Unexpected job location: '{job['location']}'"

    def test_view_role_button_redirects_to_lever(self, careers_page_qa_filtered):
        careers_page_qa_filtered.select_location()
        careers_page_qa_filtered.click_apply_button()
        assert careers_page_qa_filtered.is_view_role_redirected_to_expected_lever_url()
