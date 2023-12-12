from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
global driver, wait

class LoginPageLocators:
    USERNAME_INPUT = (By.ID, "Txt_User")
    PASSWORD_FIELD = (By.NAME, "Txt_Pass")
    LOGIN_BUTTON = (By.ID, "Login")
    select_institute_locator = (By.XPATH, "//*[@id='CenterSelectionAuditorListGrid_DXDataRow0']/td[1]")
    save_institute_locator = (By.XPATH, "//*[@id='SelectInstitute_Save']/div")
    center_search_locator = (By.XPATH, "//div[@id='SelectCenter_Search']")
    center_save_locator = (By.XPATH, "//div[@id='SelectCenter_Save']//div[@class='dx-button-content']")

def initialize_context(context):
    chrome_options = Options()
    chrome_service = Service(ChromeDriverManager().install())

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
    context.driver = driver

    # Navigate to the website
    driver.get("https://connectonetest.bkinfo.in/Start/Login/Frm_Auditor_Login/")
    driver.implicitly_wait(20)
    driver.maximize_window()

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 10)
    context.wait = wait