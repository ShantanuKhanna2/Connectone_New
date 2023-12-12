from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time, calendar, random, datetime
from selenium.webdriver import Keys
from datetime import date, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

Chrome_options = Options()
chrome_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=Chrome_options, service= chrome_service)
driver.implicitly_wait(20)
driver.get("https://connectonetest.bkinfo.in/Start/Login/Frm_Auditor_Login/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

#Login username and Password
username =wait.until(EC.element_to_be_clickable((By.ID,"Txt_User")))
ActionChains(driver).move_to_element(username).send_keys("bkshantanu").perform()

password = wait.until(EC.element_to_be_clickable((By.NAME,"Txt_Pass")))
password.send_keys("babatest")

login_click = wait.until(EC.element_to_be_clickable((By.ID,"Login")))
ActionChains(driver).click(login_click).perform()

def click_element(wait, locator):
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()

# Select Institute and Center
select_institute_locator = (By.XPATH,"//*[@id='CenterSelectionAuditorListGrid_DXDataRow0']/td[1]")
save_institute_locator = (By.XPATH, "//*[@id='SelectInstitute_Save']/div")
center_search_locator = (By.XPATH, "//div[@id='SelectCenter_Search']")
center_save_locator = (By.XPATH, "//div[@id='SelectCenter_Save']//div[@class='dx-button-content']")

click_element(wait, select_institute_locator)
click_element(wait, save_institute_locator)
time.sleep(4)
click_element(wait, center_search_locator)
time.sleep(4)
click_element(wait, center_save_locator)

# For dropdown - Accounts -> Voucher_Entries Entries -> Cash Deposit Or Withdawn/Withdrawn
driver.find_element(By.ID,"Accounts_Main").click()
time.sleep(2)

drop_down = wait.until(EC.element_to_be_clickable((By.ID,"Accounts_Vouchers")))
ActionChains(driver).move_to_element(drop_down).perform()
drop_down_1 = wait.until(EC.element_to_be_clickable((By.ID,"Accounts_Voucher_BankToBank")))
ActionChains(driver).click(drop_down_1).perform()
time.sleep(2)

#select MODE name
mode_dropdown_locator = (By.ID, "Cmd_Mode_B2B")
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

#select bank transfer detail
#transfer detail - bank from
from_bankname_dropdown_locator = (By.ID, "GLookUp_BankList1_B2B")

#select bank detail
# Check if the error message element is present for bank
save_button = driver.find_element(By.XPATH, "//*[@id='EditVouB2B']/div")
save_button.click()
from_bankname_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located(from_bankname_dropdown_locator))
ActionChains(driver).move_to_element(from_bankname_dropdown).perform()
error_message_bank = driver.find_element(By.XPATH, "//div[contains(text(),'Bank Name Not Selected...!')]")
try:
    error_message_bank = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Bank Name Not Selected...!')]")))

    if error_message_bank.is_displayed():
        print("Error message appeared:", error_message_bank.text)
    else:
        print("No error message appeared.")
except StaleElementReferenceException:
    print("Element reference is stale. Retrying or handling the situation accordingly.")

from_bankname_options_data = {
     "Bank of Baroda": (By.XPATH,"//*[@id='B2B_GLookUp_BankList1_datagrid']/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[1]"),
     "State Bank of India": (By.XPATH,"(//td[@role='gridcell'][normalize-space()='STATE BANK OF INDIA'])[2]"),
}

from_bankname_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located(from_bankname_dropdown_locator))
from_bankname_dropdown.click()

from_bankname_random_option = random.choice(list(from_bankname_options_data.keys()))
from_bankname_option_locator = from_bankname_options_data[from_bankname_random_option]
from_bankname_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located(from_bankname_option_locator))
from_bankname_option.click()
print("Selected Bank: ", from_bankname_random_option)

#transfer detail - bank to
to_bankname_dropdown_locator = (By.ID, "GLookUp_BankList2_B2B")

#select bank detail
# Check if the error message element is present for bank
save_button = driver.find_element(By.XPATH, "//*[@id='EditVouB2B']/div")
save_button.click()
to_bankname_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located(to_bankname_dropdown_locator))
ActionChains(driver).move_to_element(to_bankname_dropdown).perform()
error_message_bank = driver.find_element(By.XPATH, "//div[contains(text(),'Bank Name Not Selected...!')]")
try:
    error_message_bank = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Bank Name Not Selected...!')]")))

    if error_message_bank.is_displayed():
        print("Error message appeared:", error_message_bank.text)
    else:
        print("No error message appeared.")
except StaleElementReferenceException:
    print("Element reference is stale. Retrying or handling the situation accordingly.")

to_bankname_options_data = {
     "Bank of Baroda": (By.XPATH,"(//td[@role='gridcell'][normalize-space()='BANK OF BARODA'])[2]"),
     "State Bank of India": (By.XPATH,"(//td[@role='gridcell'][normalize-space()='STATE BANK OF INDIA'])[2]"),
}
to_bankname_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located(to_bankname_dropdown_locator))
to_bankname_dropdown.click()

to_bankname_random_option = random.choice(list(to_bankname_options_data.keys()))
to_bankname_option_locator = to_bankname_options_data[to_bankname_random_option]
to_bankname_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located(to_bankname_option_locator))
to_bankname_option.click()
print("Selected Bank: ", to_bankname_random_option)

#purpose
purpose_dropdown_locator = (By.ID, "PurposeID_B2B")

save_button = driver.find_element(By.XPATH, "//*[@id='EditVouB2B']/div")
save_button.click()
purpose_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located(purpose_dropdown_locator))
ActionChains(driver).move_to_element(purpose_dropdown).perform()
error_message_purpose = driver.find_element(By.XPATH, "//div[contains(text(),'Purpose Cannot Be Blank..!!')]")
if error_message_purpose.is_displayed():
    print("Error message appeared:", error_message_purpose.text)
else:
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

purpose_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located(purpose_dropdown_locator))
purpose_dropdown.click()

purpose_random_option = random.choice(list(purpose_options_data.keys()))
purpose_option_locator = purpose_options_data[purpose_random_option]
purpose_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located(purpose_option_locator))
purpose_option.click()
print("Selected purpose:", purpose_random_option)
time.sleep(3)

# Check if the error message element is present for Voucher Date
save_button = driver.find_element(By.XPATH, "//*[@id='EditVouB2B']/div")
save_button.click()
error_message = driver.find_element(By.XPATH, "//div[contains(text(),'Voucher Date Not Selected...!')]")
if error_message.is_displayed():
    print("Error message appeared:", error_message.text)
else:
    print("No error message appeared.")
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

voucher_date = driver.find_element(By.ID, "Txt_V_Date_B2B")
Last_year_date = ActionChains(driver).move_to_element(voucher_date).click().send_keys(random_date.strftime("%d-%m-%Y")).perform()
print("Selected last year date is:", Last_year_date)

# Check if the error message element is present for last year date
save_button = driver.find_element(By.XPATH, "//*[@id='EditVouB2B']/div")
save_button.click()
error_message_date = driver.find_element(By.XPATH, "//div[contains(text(),'Date Not As Per Financial Year...!')]")
if error_message_date.is_displayed():
    print("Error message appeared:", error_message_date.text)
else:
    print("No error message appeared.")

ActionChains(driver).move_to_element(voucher_date).click().send_keys(Keys.CONTROL + "a").send_keys(Keys.DELETE).perform()
# Find the start date element
voucher_date = driver.find_element(By.ID, "Txt_V_Date_B2B")
ActionChains(driver).move_to_element(voucher_date).click().send_keys(current_date).perform()
print("Select current year date is:", current_date)
time.sleep(1)

#MODE_Reference_Detail:

#Check if the error message element is present for refernce number
save_button = driver.find_element(By.XPATH, "//*[@id='EditVouB2B']/div")
save_button.click()
ref_number = driver.find_element(By.ID, "Txt_Ref_No_B2B")
ActionChains(driver).move_to_element(ref_number).perform()
error_message = driver.find_element(By.XPATH, "//div[contains(text(),'Ref No Not Selected...!')]")
if error_message.is_displayed():
    print("Error message appeared:", error_message.text)
else:
    print("No error message appeared.")
ActionChains(driver).move_to_element(ref_number).click().send_keys("12345").perform()

#Check if the error message element is present for refernce date
save_button = driver.find_element(By.XPATH, "//*[@id='EditVouB2B']/div")
save_button.click()
ref_date = driver.find_element(By.ID, "Txt_Ref_Date_B2B")
error_message = driver.find_element(By.XPATH, "//div[contains(text(),'Cheque Date Not Selected...!')]")
if error_message.is_displayed():
    print("Error message appeared:", error_message.text)
else:
    print("No error message appeared.")

ActionChains(driver).move_to_element(ref_date).click().send_keys(random_date.strftime("%d-%m-%Y")).perform()
print("Selected last year date is:", random_date.strftime("%d-%m-%Y"))

# Check if the error message element is present
save_button = driver.find_element(By.XPATH, "//*[@id='EditVouB2B']/div")
save_button.click()
try:
   error_message_date = driver.find_element(By.XPATH, "//div[contains(text(),'Date Not As Per Financial Year...!')]")
   if error_message_date.is_displayed():
    print("Error message appeared:", error_message_date.text)
except NoSuchElementException:
    print("No error message appeared.")

ActionChains(driver).move_to_element(ref_date).click().send_keys(Keys.CONTROL + "a").send_keys(Keys.DELETE).perform()
# Find the start date element
voucher_date = driver.find_element(By.ID, "Txt_V_Date_B2B")
ActionChains(driver).move_to_element(ref_date).click().send_keys(current_date).perform()
print("Selected current ref year date is:", current_date)

#Check if the error message element is present for amount
save_button = driver.find_element(By.XPATH, "//*[@id='EditVouB2B']/div")
save_button.click()
amount = driver.find_element(By.ID, "Txt_Amount_B2B")
ActionChains(driver).move_to_element(amount).perform()
error_message = driver.find_element(By.XPATH, "//div[contains(text(),'Amount Not Selected...!')]")
if error_message.is_displayed():
    print("Error message appeared:", error_message.text)
else:
    print("No error message appeared.")

ActionChains(driver).move_to_element(amount).click().send_keys("34").perform()

# click on the save button
save_button = driver.find_element(By.XPATH, "//*[@id='EditVouB2B']/div")
save_button.click()
print("Form saved sucessfully")

