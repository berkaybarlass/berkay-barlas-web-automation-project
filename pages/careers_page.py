from selenium.webdriver.support.wait import WebDriverWait

from data.urls import CAREERS_URL
from locators.careers_page_locators import CareersPageLocators
from pages.base_page import BasePage


class CareersPage(BasePage):

    def open_page(self):
        self.open(CAREERS_URL)

    def click_see_all_teams(self):
        self.click(CareersPageLocators.SEE_ALL_TEAMS_BUTTON)

    def click_open_qa_positions(self):
        self.click(CareersPageLocators.QUALITY_ASSURANCE_POSITIONS_CARD)

    def wait_for_positions_to_load(self):
        self.logger.info("Waiting for QA positions count to be greater than 0")

        WebDriverWait(self.driver, 10).until(
            lambda driver: int(
                driver.find_element(*CareersPageLocators.QUALITY_ASSURANCE_POSITIONS_CARD)
                .text.split()[0]
            ) > 0
        )

    def is_quality_assurance_filter_selected(self):
        element = self.wait_for_visibility(
            CareersPageLocators.SELECTED_TEAM_FILTER_LABEL
        )
        return "Quality Assurance" in element.text

    def are_job_postings_present(self):
        jobs = self.find_all(CareersPageLocators.JOB_POSTINGS)

        self.logger.info(f"Found {len(jobs)} job postings")

        return len(jobs) > 0

    def select_location(self):
        self.click(CareersPageLocators.LOCATION_FILTER)
        self.click(CareersPageLocators.LOCATION_ISTANBUL)

    def validate_job_cards(self):
        jobs = self.find_all(CareersPageLocators.JOB_POSTINGS)
        self.logger.info(f"Found {len(jobs)} job postings")

        for job in jobs:
            title = job.find_element(*CareersPageLocators.JOB_TITLE).text
            location = job.find_element(*CareersPageLocators.JOB_LOCATION).text

            assert "Quality Assurance" in title
            assert "ISTANBUL, TURKIYE" in location