from selenium import webdriver
import pytest

driver = webdriver.Chrome(executable_path="C:\\Users\Shantanu\PycharmProjects\Connectone\Driver\chromedriver.exe")
driver.get("https://services.connectone.app/form/2587")

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runreport_makereport(item, call):
    outcome = yield
    rep =outcome.get.result()


