from selenium.webdriver.common.by import By

class CareersPageLocators:
    SEE_ALL_TEAMS_BUTTON = (By.XPATH, "//a[contains(.,'See all teams')]")
    QUALITY_ASSURANCE_POSITIONS_CARD = (By.CSS_SELECTOR, ".elementor-repeater-item-56ca501 .insiderone-icon-cards-grid-item-btn")
    SELECTED_TEAM_FILTER_LABEL = (By.CSS_SELECTOR, "div.filter-button.has-selected-filter")
    JOB_POSTINGS = (By.CSS_SELECTOR, ".posting-title")
    LOCATION_FILTER = (By.CSS_SELECTOR, "[aria-label='Filter by Location: All'] > .filter-button")
    LOCATION_ISTANBUL = (By.XPATH, "//a[.='Istanbul, Turkiye']")
    JOB_TITLE = (By.XPATH, "//div[@class='posting']/a[@href='https://jobs.lever.co/insiderone/774658ce-0d6e-4b07-a69b-4629fa11d6f3']")
    JOB_LOCATION = (By.CSS_SELECTOR, ".sort-by-location")