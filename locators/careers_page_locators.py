from selenium.webdriver.common.by import By

class CareersPageLocators:
    SEE_ALL_TEAMS_BUTTON = (By.XPATH, "//a[contains(.,'See all teams')]")
    QUALITY_ASSURANCE_POSITIONS_CARD = (By.CSS_SELECTOR, ".elementor-repeater-item-56ca501 .insiderone-icon-cards-grid-item-btn")
    SELECTED_TEAM_FILTER_LABEL = (By.CSS_SELECTOR, "div.filter-button.has-selected-filter")
    JOB_POSTINGS = (By.CSS_SELECTOR, "div.posting")