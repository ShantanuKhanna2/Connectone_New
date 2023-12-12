import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(params=["chrome","firefox"],scope="function")
def get_browser(request):

    if request.param == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    if request.param == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver.get("http://facebook.com")
    driver.maximize_window()
    yield driver
    driver.quit()