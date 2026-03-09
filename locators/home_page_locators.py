from selenium.webdriver.common.by import By


class HomePageLocators:
    COOKIE_ACCEPT_ALL_BUTTON = (By.ID, "wt-cli-accept-all-btn")
    COOKIE_ONLY_NECESSARY_BUTTON = (By.ID, "wt-cli-accept-btn")
    COOKIE_DECLINE_ALL_BUTTON = (By.ID, "wt-cli-reject-btn")
    HEADER = (By.CSS_SELECTOR, ".header-wrapper")
    FOOTER = (By.CSS_SELECTOR, ".footer-wrapper")
    MAIN = (By.TAG_NAME, "main")
    ALL_SECTIONS = (By.TAG_NAME, "section")
