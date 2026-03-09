import os
from datetime import datetime

import pytest

from config.config import SCREENSHOT_DIR
from utils.driver_factory import DriverFactory
from utils.logger import get_logger


logger = get_logger(__name__)


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser: chrome or firefox"
    )
    parser.addoption(
        "--headless",
        action="store",
        default="false",
        help="Headless mode: true or false"
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless").lower() == "true"

    driver = DriverFactory.create_driver(browser=browser, headless=headless)
    driver.implicitly_wait(0)

    request.node.driver = driver

    yield driver

    logger.info("Closing browser")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)

        if driver:
            os.makedirs(SCREENSHOT_DIR, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"{item.name}_{timestamp}.png"
            screenshot_path = os.path.join(SCREENSHOT_DIR, screenshot_name)

            driver.save_screenshot(screenshot_path)
            logger.error(f"Test failed. Screenshot saved: {screenshot_path}")