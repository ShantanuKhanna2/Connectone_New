import datetime
import calendar
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date, timedelta

Chrome_options = Options()
chrome_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=Chrome_options, service=chrome_service)
driver.implicitly_wait(20)
driver.get("https://connectonetest.bkinfo.in/Start/Login/Frm_Auditor_Login/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# Login username and Password
username = wait.until(EC.element_to_be_clickable((By.ID, "Txt_User")))
ActionChains(driver).move_to_element(username).send_keys("bkshantanu").perform()

password = wait.until(EC.element_to_be_clickable((By.NAME, "Txt_Pass")))
password.send_keys("babatest")

login_click = wait.until(EC.element_to_be_clickable((By.ID, "Login")))
ActionChains(driver).click(login_click).perform()

def click_element(wait, locator):
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()

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

# For dropdown, action chain is used if index, visible_text,etc are not working.
driver.find_element(By.ID, "Accounts_Main").click()
time.sleep(2)

drop_down = wait.until(EC.element_to_be_clickable((By.ID, "Accounts_Vouchers")))
ActionChains(driver).move_to_element(drop_down).perform()
drop_down_1 = wait.until(EC.element_to_be_clickable((By.ID, "Accounts_Voucher_Receipt")))
ActionChains(driver).click(drop_down_1).perform()
time.sleep(4)

# Check if the error message element is present for Item Name
save_form_locator = (By.XPATH, "//*[@id='BUT_SAVE_Receipt']/div")
save_form = WebDriverWait(driver, 10).until(EC.presence_of_element_located(save_form_locator))
driver.execute_script("arguments[0].click();", save_form)
time.sleep(1)
driver.find_element(By.XPATH,"//div[@aria-label='OK']//div[@class='dx-button-content']").click()
time.sleep(1)

#select Item name
itemname_dropdown_locator = (By.ID, "Rpt_GLookUp_ItemList")
itemname_dropdown = wait.until(EC.presence_of_element_located(itemname_dropdown_locator))
itemname_dropdown.click()

itemname_options_data = {

    "Advance Received and Payable" : (By.XPATH,"//td[@class='dx-cell-focus-disabled'][normalize-space()='Advance Received and Payable']"),
    "Any Other Income": (By.XPATH,"//td[normalize-space()='Any Other Income']"),
    "Building Insurance Claim Received": (By.XPATH,"//td[normalize-space()='Building Insurance Claim Received']"),
    "Discount Received": (By.XPATH,"//td[normalize-space()='Discount Received']"),
    "Due Amount Received": (By.XPATH,"//td[normalize-space()='Due Amount Received']"),
    "Electricity Deposit For Programme Refund.":(By.XPATH,"//td[normalize-space()='Electricity Deposit For Programme Refund.']")
}

max_retries = 3
retry_count = 0

while retry_count < max_retries:
    try:
        itemname_random_option = random.choice(list(itemname_options_data.keys()))
        itemname_option_locator = itemname_options_data[itemname_random_option]
        print("Selected item name:", itemname_random_option)
        itemname_option = wait.until(EC.presence_of_element_located(itemname_option_locator))
        itemname_option.click()
        break
    except TimeoutException:
        print(f"Timeout exception on attempt {retry_count + 1}")
        retry_count += 1

# Check if the error message element is present for Voucher Date
save_button = driver.find_element(By.XPATH, "//*[@id='BUT_SAVE_Receipt']/div")
save_button.click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[@aria-label='OK']//div[@class='dx-button-content']").click()
time.sleep(1)

# Select Voucher_Entries Date
current_date = datetime.datetime.now().strftime("%d-%m-%Y") # Get the current date
# Your existing code
current_year = date.today().year
random_year = random.randint(current_year - 10, current_year - 1)
random_month = random.randint(1, 12)

# Get the maximum number of days for the selected month
max_days = calendar.monthrange(random_year, random_month)[1]

# Generate a random day within the valid range for the selected month
random_day = random.randint(1, max_days)
random_date = date(random_year, random_month, random_day)
voucher_date = driver.find_element(By.ID, "Rpt_Txt_V_Date")
Last_year_date = ActionChains(driver).move_to_element(voucher_date).click().send_keys(random_date.strftime("%d-%m-%Y")).perform()
print("Selected last year date is:", Last_year_date)

# Check if the error message element is present for last year date
save_button = driver.find_element(By.XPATH, "//*[@id='BUT_SAVE_Receipt']/div")
save_button.click()
error_message_date = driver.find_element(By.XPATH, "//div[contains(text(),'Date Not As Per Financial Year...!')]")
try:
    if error_message_date.is_displayed():
     print("Error message appeared:", error_message_date.text)
except NoSuchElementException:
     print("No error message appeared.")

ActionChains(driver).move_to_element(voucher_date).click().send_keys(Keys.CONTROL + "a").send_keys(Keys.DELETE).perform()
# Find the start date element
voucher_date = driver.find_element(By.ID, "Rpt_Txt_V_Date")
ActionChains(driver).move_to_element(voucher_date).click().send_keys(current_date).perform()
print("Select current year date is:", current_date)
time.sleep(1)

# Check if the error message element is present for Party Detail
save_button = driver.find_element(By.XPATH, "//*[@id='BUT_SAVE_Receipt']/div")
save_button.click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[@aria-label='OK']//div[@class='dx-button-content']").click()
time.sleep(1)

partydetail_dropdown_locator = (By.ID, "Rpt_GLookUp_PartyList1")
partydetail_dropdown = wait.until(EC.presence_of_element_located(partydetail_dropdown_locator))
partydetail_dropdown.click()

partydetail_options_data = {

    "Shantanu" : (By.XPATH,"//*[@id='Frm_Voucher_Win_Gen_Rec_Receipt_LookUp_GetPartyList_datagrid']/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td"),
}

loginmode_random_option = random.choice(list(partydetail_options_data.keys()))
partydetail_option_locator = partydetail_options_data[loginmode_random_option]
partydetail_option = wait.until(EC.presence_of_element_located(partydetail_option_locator))
partydetail_option.click()

# Check if the error message element is present for Amount
save_form_locator = (By.XPATH, "//*[@id='BUT_SAVE_Receipt']/div")
save_form = WebDriverWait(driver, 10).until(EC.presence_of_element_located(save_form_locator))
driver.execute_script("arguments[0].click();", save_form)
time.sleep(1)
driver.find_element(By.XPATH,"//div[@aria-label='OK']//div[@class='dx-button-content']").click()
time.sleep(1)
amount = driver.find_element(By.ID, "Rpt_Txt_Amount")
ActionChains(driver).move_to_element(amount).click().send_keys("34").perform()

# Check if the error message element is present for Purpose
save_form_locator = (By.XPATH, "//*[@id='BUT_SAVE_Receipt']/div")
save_form = WebDriverWait(driver, 10).until(EC.presence_of_element_located(save_form_locator))
driver.execute_script("arguments[0].click();", save_form)
time.sleep(1)
driver.find_element(By.XPATH,"//div[@aria-label='OK']//div[@class='dx-button-content']").click()
time.sleep(1)

purpose_dropdown_locator = (By.ID, "Rpt_GLookUp_PurList")
purpose_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located(purpose_dropdown_locator))
ActionChains(driver).move_to_element(purpose_dropdown).perform()

purpose_options_data = {
     "Anniversary": (By.XPATH,"//div[contains(text(),'Anniversary')]"),
     "Alvida Tannav": (By.XPATH, "//div[contains(text(),'Alvida Tannav')]"),
     "Aviation Shipping Tourism Programme": (By.XPATH, "//div[contains(text(),'Aviation Shipping Tourism Programme')]"),
     "Awakening with B.K": (By.XPATH, "//div[contains(text(),'Awakening with B.K')]"),
     "Azadi ka Amrit Mahotsav": (By.XPATH, "//div[contains(text(),'Azadi ka Amrit Mahotsav')]"),
     "Bhawan Inauguration": (By.XPATH, "//div[contains(text(),'Bhawan Inauguration')]"),
     "Biogas Plant": (By.XPATH, "//div[contains(text(),'Biogas Plant')]"),
}

purpose_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located(purpose_dropdown_locator))
purpose_dropdown.click()

purpose_random_option = random.choice(list(purpose_options_data.keys()))
purpose_option_locator = purpose_options_data[purpose_random_option]
purpose_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located(purpose_option_locator))
purpose_option.click()
time.sleep(3)

#select MODE name
mode_dropdown_locator = (By.ID, "Rpt_Cmd_Mode")
mode_dropdown = wait.until(EC.presence_of_element_located(mode_dropdown_locator))
mode_dropdown.click()
time.sleep(2)

mode_options_data = {
     "CHEQUE": (By.XPATH,"//div[contains(text(),'CHEQUE')]"),
     "DD": (By.XPATH,"//div[contains(text(),'DD')]"),
    "CBS": (By.XPATH, "//div[contains(text(),'CBS')]"),
    "RTGS": (By.XPATH, "//div[contains(text(),'RTGS')]"),
    "NEFT": (By.XPATH, "//div[contains(text(),'NEFT')]"),
}

mode_random_option = random.choice(list(mode_options_data.keys()))
mode_option_locator = mode_options_data[mode_random_option]
mode_option = wait.until(EC.presence_of_element_located(mode_option_locator))
mode_option.click()

# click on the save button
save_button = driver.find_element(By.XPATH, "//*[@id='BUT_SAVE_Receipt']/div")
save_button.click()
print("Form saved sucessfully")
