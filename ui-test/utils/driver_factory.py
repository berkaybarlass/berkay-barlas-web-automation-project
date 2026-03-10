from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from utils.logger import get_logger


logger = get_logger(__name__)


class DriverFactory:
    @staticmethod
    def create_driver(browser: str = "chrome", headless: bool = False):
        browser = browser.lower()

        logger.info(f"Creating driver for browser: {browser} | headless={headless}")

        if browser == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-popup-blocking")
            driver = webdriver.Chrome(options=options)

        elif browser == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("-headless")
            driver = webdriver.Firefox(options=options)
            driver.maximize_window()

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        logger.info("Driver created successfully.")
        return driver