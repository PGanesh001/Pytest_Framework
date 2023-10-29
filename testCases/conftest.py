import pytest
from selenium import webdriver
from utilites import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configuration("basic info","browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    else:
        print("browser required")
    driver.maximize_window()
    base_url = ReadConfigurations.read_configuration("basic info", "baseURL")
    driver.get(base_url)
    request.cls.driver = driver
    yield
    driver.quit()
