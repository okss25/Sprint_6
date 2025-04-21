import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

@pytest.fixture()
def driver():

    service = FirefoxService()
    driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()