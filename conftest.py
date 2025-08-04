import pytest
from selenium import webdriver
import time
@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://qamoviesapp.ccbp.tech/")
    yield driver
    time.sleep(5)
    driver.quit()