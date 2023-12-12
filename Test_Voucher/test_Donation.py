from datetime import datetime, date
import calendar
import pytest
import random
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common import StaleElementReferenceException, NoSuchElementException, TimeoutException
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

def retry_click(element_locator):
    retry_attempts = 3
    for _ in range(retry_attempts):
        try:
            element = wait.until(EC.presence_of_element_located(element_locator))
            element.click()
            return
        except StaleElementReferenceException:
            print("StaleElementReferenceException occurred. Retrying...")
            time.sleep(2)

@pytest.fixture(scope="class")
def driver():
    # Set up the driver and perform the initial setup
    Chrome_options = Options()
    chrome_service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(options=Chrome_options, service=chrome_service)
    driver.implicitly_wait(20)
    driver.get("https://connectonetest.bkinfo.in/Start/Login/Frm_Auditor_Login/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
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
        drop_down_1 = wait.until(EC.element_to_be_clickable((By.ID, "Accounts_Voucher_Donation")))
        ActionChains(driver).click(drop_down_1).perform()
        time.sleep(2)
#Donation
    def test_select_item_name(self, driver):
        wait = WebDriverWait(driver, 10)
        # Check if the error message element is present for Item Name
        save_button = driver.find_element(By.ID, "SAVE_COM")
        save_button.click()
        try:
            error_message_date = driver.find_element(By.XPATH,
                                                 "//div[contains(text(),'Item Name Not Selected...!')]")
            if error_message_date.is_displayed():
                print("Error message appeared:", error_message_date.text)
        except NoSuchElementException:
            print("No error message appeared.")

        #select Item name
        itemname_dropdown_locator = (By.ID, "GLookUp_ItemList_Donation")
        itemname_dropdown = wait.until(EC.presence_of_element_located(itemname_dropdown_locator))
        itemname_dropdown.click()

        itemname_options_data = {

            "Corpus Donation" : (By.XPATH,"//td[normalize-space()='Corpus Donation']"),
            "Donation": (By.XPATH,"//td[normalize-space()='Donation']"),
        }

        itemname_random_option = random.choice(list(itemname_options_data.keys()))
        itemname_option_locator = itemname_options_data[itemname_random_option]
        print("Selected item name:", itemname_random_option)
        itemname_option = wait.until(EC.presence_of_element_located(itemname_option_locator))
        itemname_option.click()

    def test_select_voucher_date(self, driver):
        # Check if the error message element is present for Voucher Date
        save_button = driver.find_element(By.ID, "SAVE_COM")
        save_button.click()
        try:
            error_message_date = driver.find_element(By.XPATH,
                                                 "//div[contains(text(),'Voucher Date Not Selected...!')]")
            if error_message_date.is_displayed():
                print("Error message appeared:", error_message_date.text)
        except NoSuchElementException:
            print("No error message appeared.")

        # Select Voucher_Entries Date
        voucher_date = driver.find_element(By.ID, "Txt_V_Date_Donation")
        Last_year_date = ActionChains(driver).move_to_element(voucher_date).click().send_keys(random_date.strftime("%d-%m-%Y")).perform()
        print("Selected last year date is:", Last_year_date)

        # Check if the error message element is present for last year date
        save_button = driver.find_element(By.ID, "SAVE_COM")
        save_button.click()
        error_message_date = driver.find_element(By.XPATH, "//div[contains(text(),'Date Not As Per Financial Year...!')]")
        try:
            if error_message_date.is_displayed():
             print("Error message appeared:", error_message_date.text)
        except NoSuchElementException:
             print("No error message appeared.")

        ActionChains(driver).move_to_element(voucher_date).click().send_keys(Keys.CONTROL + "a").send_keys(Keys.DELETE).perform()
        # Find the start date element
        voucher_date = driver.find_element(By.ID, "Txt_V_Date_Donation")
        ActionChains(driver).move_to_element(voucher_date).click().send_keys(current_date).perform()
        print("Select current year date is:", current_date)
        time.sleep(1)

    def test_select_donor_name(self, driver):
        save_button = driver.find_element(By.ID, "SAVE_COM")
        save_button.click()
        donor_dropdown_locator = (By.ID, "GLookUp_PartyList_Donation")
        try:
            error_message_date = driver.find_element(By.XPATH,
                                                 "//div[contains(text(),'Donor Not Selected...!')]")
            if error_message_date.is_displayed():
                print("Error message appeared:", error_message_date.text)
        except NoSuchElementException:
            print("No error message appeared.")
        donor_dropdown = wait.until(EC.presence_of_element_located(donor_dropdown_locator))
        donor_dropdown.click()
        driver.find_element(By.XPATH,"(//input[@aria-label='Search in data grid'])[4]").send_keys("user")
        donor_options_data = {
             "User-02abefb5": (By.XPATH,"//td[normalize-space()='User-02abefb5']"),
             "User-02ba244a": (By.XPATH,"//td[normalize-space()='User-02ba244a']"),
            "User-037befaf": (By.XPATH, "//td[normalize-space()='User-037befaf']"),
        }

        donor_random_option = random.choice(list(donor_options_data.keys()))
        donor_option_locator = donor_options_data[donor_random_option]
        print("Selected donor name:", donor_random_option)
        retry_click(donor_option_locator)

    def test_select_mode_name(self, driver):
        mode_dropdown_locator = (By.ID, "Cmd_Mode_Donation")
        mode_dropdown = wait.until(EC.presence_of_element_located(mode_dropdown_locator))
        mode_dropdown.click()

        mode_options_data = {
             "CHEQUE": (By.XPATH,"//div[contains(text(),'CHEQUE')]"),
             "DD": (By.XPATH,"//div[contains(text(),'DD')]"),
            "CBS": (By.XPATH, "//div[contains(text(),'CBS')]"),
            "RTGS": (By.XPATH, "//div[contains(text(),'RTGS')]"),
            "NEFT": (By.XPATH, "//div[contains(text(),'NEFT')]"),
        }

        mode_random_option = random.choice(list(mode_options_data.keys()))
        mode_option_locator = mode_options_data[mode_random_option]
        print("Selected mode name:", mode_random_option)
        mode_option = wait.until(EC.presence_of_element_located(mode_option_locator))
        mode_option.click()
        print("Selected mode name:", mode_random_option)
        cheque_number_locator = (By.ID, "Txt_Ref_No_Donation")
        cheque_number = wait.until(EC.element_to_be_clickable(cheque_number_locator))

        if mode_random_option in ['CHEQUE','DD']:
            ActionChains(driver).move_to_element(cheque_number).click().send_keys(str(random.randint(100000,999999))).perform()
        else:
            ActionChains(driver).move_to_element(cheque_number).click().send_keys("123").perform()

        bank_dropdown_locator = (By.ID, "GLookUp_BankList_Donation")
        bank_dropdown = wait.until(EC.presence_of_element_located(bank_dropdown_locator))
        bank_dropdown.click()
        bank_options_data = {
            "BANK OF BARODA": (By.XPATH, "(//td[@role='gridcell'][normalize-space()='BANK OF BARODA'])[2]"),
            "STATE BANK OF INIDA": (By.XPATH, "//td[normalize-space()='STATE BANK OF INDIA']"),
        }
        bank_random_option = random.choice(list(bank_options_data.keys()))
        bank_option_locator = bank_options_data[bank_random_option]
        print("Selected bank name:", bank_random_option)
        bank_option = wait.until(EC.element_to_be_clickable(bank_option_locator))
        bank_option.click()
        
    def test_amount(self, driver):
        save_button = driver.find_element(By.ID, "SAVE_COM")
        save_button.click()
        amount = driver.find_element(By.ID, "Txt_Amount_Donation")
        ActionChains(driver).move_to_element(amount).perform()

        try:
            error_message_date = driver.find_element(By.XPATH,
                                                 "//div[contains(text(),'Amount cannot be Zero/Negative...!')]")
            if error_message_date.is_displayed():
                print("Error message appeared:", error_message_date.text)
        except NoSuchElementException:
            print("No error message appeared.")

        ActionChains(driver).move_to_element(amount).click().send_keys("34").perform()

    def test_select_purpose(self, driver):
        save_button = driver.find_element(By.ID, "SAVE_COM")
        save_button.click()
        purpose_dropdown_locator = driver.find_element(By.ID, "GLookUp_PurList_Donation")
        ActionChains(driver).move_to_element(purpose_dropdown_locator).perform()
        try:
            error_message_date = driver.find_element(By.XPATH,
                                                 "//div[contains(text(),'Purpose not Selected...!')]")
            if error_message_date.is_displayed():
                print("Error message appeared:", error_message_date.text)
        except NoSuchElementException:
            print("No error message appeared.")

        purpose_options_data = {
             "Anniversary": (By.XPATH,"//div[contains(text(),'Anniversary')]"),
             "Alvida Tannav": (By.XPATH, "//div[contains(text(),'Alvida Tannav')]"),
             "Aviation Shipping Tourism Programme": (By.XPATH, "//div[contains(text(),'Aviation Shipping Tourism Programme')]"),
             "Awakening with B.K": (By.XPATH, "//div[contains(text(),'Awakening with B.K')]"),
             "Azadi ka Amrit Mahotsav": (By.XPATH, "//div[contains(text(),'Azadi ka Amrit Mahotsav')]"),
             "Bhawan Inauguration": (By.XPATH, "//div[contains(text(),'Bhawan Inauguration')]"),
             "Biogas Plant": (By.XPATH, "//div[contains(text(),'Biogas Plant')]"),
        }

        purpose_dropdown_locator.click()
        purpose_random_option = random.choice(list(purpose_options_data.keys()))
        purpose_option_locator = purpose_options_data[purpose_random_option]
        print("Selected purpose name:", purpose_random_option)
        purpose_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located(purpose_option_locator))
        purpose_option.click()
        time.sleep(2)

    def test_save_form(self, driver):
        save_button = driver.find_element(By.ID, "SAVE_COM")
        ActionChains(driver).move_to_element(save_button).click().perform()
        print("Form saved sucessfully")

