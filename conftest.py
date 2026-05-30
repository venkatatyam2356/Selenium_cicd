import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Fixture: Driver setup
@pytest.fixture(scope="class")
def init_driver(request):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")

    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)

    request.cls.driver = driver
    yield
    driver.quit()

# Hook: Screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = getattr(item.instance, 'driver', None)
        if driver:
            # Create screenshot folder if it doesn't exist
            os.makedirs("screenshots", exist_ok=True)

            file_name = f"screenshots/{item.name}.png"
            driver.save_screenshot(file_name)
            print(f"\n Screenshot saved to: {file_name}")
