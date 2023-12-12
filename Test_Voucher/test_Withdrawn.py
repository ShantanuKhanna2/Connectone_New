from datetime import datetime, date
import calendar
import pytest
import random
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def click_element(wait, locator):
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()


# Select Voucher_Entries Date
current_date = datetime.now().strftime("%d-%m-%Y")  # Get the current date
# Your existing code
current_year = date.today().year
random_year = random.randint(current_year - 10, current_year - 1)
random_month = random.randint(1, 12)
# Get the maximum number of days for the selected month
max_days = calendar.monthrange(random_year, random_month)[1]
# Generate a random day within the valid range for the selected month
random_day = random.randint(1, max_days)
random_date = date(random_year, random_month, random_day)


@pytest.fixture(scope="class")
def driver():
    # Set up the driver and perform the initial setup
    Chrome_options = Options()
    chrome_service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(options=Chrome_options, service=chrome_service)
    driver.implicitly_wait(10)
    driver.get("https://connectonetest.bkinfo.in/Start/Login/Frm_Auditor_Login/")
    driver.maximize_window()
    yield driver
    # Teardown: Close the driver after the test
    driver.quit()

class TestServiceForm:
    def test_login(self, driver):
        # Login
        global wait
        wait = WebDriverWait(driver, 10)
        username = wait.until(EC.element_to_be_clickable((By.ID, "Txt_User")))
        ActionChains(driver).move_to_element(username).send_keys("bkshantanu").perform()
        password = wait.until(EC.element_to_be_clickable((By.NAME, "Txt_Pass")))
        password.send_keys("babatest")
        login_click = wait.until(EC.element_to_be_clickable((By.ID, "Login")))
        ActionChains(driver).click(login_click).perform()

    def test_select_institute_and_center(self, driver):
        # Select Institute and Center

        select_institute_locator = (By.XPATH, "//*[@id='CenterSelectionAuditorListGrid_DXDataRow0']/td[1]")
        save_institute_locator = (By.XPATH, "//*[@id='SelectInstitute_Save']/div")
        center_search_locator = (By.XPATH, "//div[@id='SelectCenter_Search']")
        center_save_locator = (By.XPATH, "//div[@id='SelectCenter_Save']//div[@class='dx-button-content']")

        click_element(wait, select_institute_locator)
        click_element(wait, save_institute_locator)
        time.sleep(4)
        click_element(wait, center_search_locator)
        time.sleep(4)
        click_element(wait, center_save_locator)

    def test_select_voucher_type(self, driver):
        # Select Voucher Type
        wait = WebDriverWait(driver, 10)

        driver.find_element(By.ID, "Accounts_Main").click()
        time.sleep(2)

        drop_down = wait.until(EC.element_to_be_clickable((By.ID, "Accounts_Vouchers")))
        ActionChains(driver).move_to_element(drop_down).perform()
        drop_down_1 = wait.until(EC.element_to_be_clickable((By.ID, "Accounts_Voucher_CashBank")))
        ActionChains(driver).click(drop_down_1).perform()
        time.sleep(2)

    def test_select_Item_name(self, driver):
        # Select MODE name
        wait = WebDriverWait(driver, 10)
        itemname_dropdown_locator = (By.ID, "GLookUp_ItemList_CDW")
        itemname_dropdown = wait.until(EC.presence_of_element_located(itemname_dropdown_locator))
        itemname_dropdown.click()
        time.sleep(2)

        itemname_options_data = {
            "Cash Deposited in Bank": (By.XPATH,
                                       "//*[@id='Frm_Voucher_Win_Cash_GLookUp_ItemId_datagrid']/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[1]"),
            "Cash Withdrawn from Bank": (By.XPATH,
                                         "//*[@id='Frm_Voucher_Win_Cash_GLookUp_ItemId_datagrid']/div/div[6]/div/div/div[1]/div/table/tbody/tr[2]/td[1]"),
        }

        # loginmode_random_option = random.choice(list(loginmode_options_data.keys()))
        itemname_option_locator = itemname_options_data["Cash Withdrawn from Bank"]
        itemname_option = wait.until(EC.presence_of_element_located(itemname_option_locator))
        itemname_option.click()

    def test_cash_deposit_amount(self, driver):
        save_form_locator = (By.XPATH, "//*[@id='EditVouWinCash']/div")
        save_form = WebDriverWait(driver, 10).until(EC.presence_of_element_located(save_form_locator))
        driver.execute_script("arguments[0].click();", save_form)
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@aria-label='OK']//div[@class='dx-button-content']").click()
        time.sleep(1)

        amount = driver.find_element(By.ID, "Txt_Amount_CDW")
        ActionChains(driver).move_to_element(amount).click().send_keys("34").perform()

    def test_select_voucher_dates(self, driver):
        save_button = driver.find_element(By.XPATH, "//*[@id='EditVouWinCash']/div")
        save_button.click()
        try:
            error_message_voucher = driver.find_element(By.XPATH,
                                            "//div[contains(text(),'Voucher Date Incorrect / Blank. . . !')]")
            if error_message_voucher.is_displayed():
                print("Error message appeared:", error_message_voucher.text)
        except NoSuchElementException:
            print("No error message appeared.")
        voucher_date = driver.find_element(By.ID, "Txt_V_Date_CDW")
        last_year_date = ActionChains(driver).move_to_element(voucher_date).click().send_keys(random_date.strftime("%d-%m-%Y")).perform()
        print("Select last year date is:", last_year_date)

        # Check if the error message element is present for current year date
        save_button = driver.find_element(By.XPATH, "//*[@id='EditVouWinCash']/div")
        save_button.click()
        try:
            error_message_date = driver.find_element(By.XPATH, "//div[contains(text(),'Date Not As Per Financial Year...!')]")
            if error_message_date.is_displayed():
               print("Error message appeared:", error_message_date.text)
        except NoSuchElementException:
            print("No error message appeared.")

        ActionChains(driver).move_to_element(voucher_date).click().send_keys(Keys.CONTROL + "a").send_keys(Keys.DELETE).perform()
        # Find the start date element
        voucher_date = driver.find_element(By.ID, "Txt_V_Date_CDW")
        current_year_date = ActionChains(driver).move_to_element(voucher_date).click().send_keys(current_date).perform()
        print("Select current year date is:", current_year_date)
        time.sleep(1)

    def test_select_bank_details(self, driver):
        wait = WebDriverWait(driver, 10)
        bankname_dropdown_locator = (By.XPATH, "//div[@id='GLookUp_BankList_CDW']//div[@class='dx-dropdowneditor-icon']")

        # select bank detail
        # Check if the error message element is present for bank
        save_button = driver.find_element(By.XPATH, "//*[@id='EditVouWinCash']/div")
        save_button.click()
        bankname_dropdown = wait.until(EC.presence_of_element_located(bankname_dropdown_locator))
        ActionChains(driver).move_to_element(bankname_dropdown).perform()
        try:
            error_message_bank = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Bank Name Not Selected...!')]")))

            if error_message_bank.is_displayed():
                print("Error message appeared:", error_message_bank.text)
            else:
                print("No error message appeared.")
        except StaleElementReferenceException:
            print("Element reference is stale. Retrying or handling the situation accordingly.")

        bankname_options_data = {
            "Bank of Baroda": (By.XPATH,
                               "//*[@id='Frm_Voucher_Win_Cash_GLookUp_BankList_datagrid']/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[1]"),
            "State Bank of India": (By.XPATH,
                                    "//*[@id='Frm_Voucher_Win_Cash_GLookUp_BankList_datagrid']/div/div[6]/div/div/div[1]/div/table/tbody/tr[2]/td[1]"),
        }

        bankname_dropdown = wait.until(EC.presence_of_element_located(bankname_dropdown_locator))
        bankname_dropdown.click()

        bankname_random_option = random.choice(list(bankname_options_data.keys()))
        bankname_option_locator = bankname_options_data[bankname_random_option]
        bankname_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located(bankname_option_locator))
        bankname_option.click()

    def test_select_purpose(self, driver):
        wait = WebDriverWait(driver, 10)
        purpose_dropdown_locator = (By.XPATH, "//*[@id='PurposeID_CDW']/div[1]/div/div[2]/div/div/div")
        save_button = driver.find_element(By.XPATH, "//*[@id='EditVouWinCash']/div")
        save_button.click()
        purpose_dropdown = wait.until(EC.presence_of_element_located(purpose_dropdown_locator))
        ActionChains(driver).move_to_element(purpose_dropdown).perform()
        error_message_purpose = driver.find_element(By.XPATH, "//div[contains(text(),'Purpose Cannot Be Blank..!!')]")
        if error_message_purpose.is_displayed():
            print("Error message appeared:", error_message_purpose.text)
        else:
            print("No error message appeared.")

        purpose_options_data = {
            "Anniversary": (By.XPATH, "//div[contains(text(),'Anniversary')]"),
            "Alvida Tannav": (By.XPATH, "//div[contains(text(),'Alvida Tannav')]"),
            "Aviation Shipping Tourism Programme": (
            By.XPATH, "//div[contains(text(),'Aviation Shipping Tourism Programme')]"),
            "Awakening with B.K": (By.XPATH, "//div[contains(text(),'Awakening with B.K')]"),
            "Azadi ka Amrit Mahotsav": (By.XPATH, "//div[contains(text(),'Azadi ka Amrit Mahotsav')]"),
            "Bhawan Inauguration": (By.XPATH, "//div[contains(text(),'Bhawan Inauguration')]"),
            "Biogas Plant": (By.XPATH, "//div[contains(text(),'Biogas Plant')]"),
        }

        purpose_dropdown = wait.until(EC.presence_of_element_located(purpose_dropdown_locator))
        purpose_dropdown.click()

        purpose_random_option = random.choice(list(purpose_options_data.keys()))
        purpose_option_locator = purpose_options_data[purpose_random_option]
        purpose_option = wait.until(EC.element_to_be_clickable(purpose_option_locator))
        purpose_option.click()
        print("Selected purpose:", purpose_random_option)
        time.sleep(2)

    def test_save_form(self, driver):
        save_button = driver.find_element(By.XPATH, "//*[@id='EditVouWinCash']/div")
        save_button.click()
        print("Form saved sucessfully")