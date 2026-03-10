from selenium.webdriver.common.by import By

class HomePageLocators:
    HEADER = (By.CSS_SELECTOR, ".header-wrapper")
    FOOTER = (By.CSS_SELECTOR, ".footer-wrapper")
    MAIN = (By.TAG_NAME, "main")
    ALL_SECTIONS = (By.TAG_NAME, "section")
