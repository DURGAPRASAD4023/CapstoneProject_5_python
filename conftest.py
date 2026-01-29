import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def setup():

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.set_page_load_timeout(90)   # ⬅ increase more
    driver.set_script_timeout(90)

    yield driver
    driver.quit()
