import datetime
import calendar
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
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
chrome_service = Service(executable_path= ChromeDriverManager().install())
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

# For dropdown, action chain is used if index, visible_text,etc are not working.
driver.find_element(By.ID,"Accounts_Main").click()
time.sleep(2)

drop_down = wait.until(EC.element_to_be_clickable((By.ID,"Accounts_Vouchers")))
ActionChains(driver).move_to_element(drop_down).perform()
drop_down_1 = wait.until(EC.element_to_be_clickable((By.ID,"Accounts_Voucher_CashBank")))
ActionChains(driver).click(drop_down_1).perform()
time.sleep(4)

#select Item name
itemname_dropdown_locator = (By.ID, "GLookUp_ItemList_CDW")
itemname_dropdown = wait.until(EC.presence_of_element_located(itemname_dropdown_locator))
itemname_dropdown.click()

itemname_options_data = {
     "Cash Deposited in Bank": (By.XPATH,"//*[@id='Frm_Voucher_Win_Cash_GLookUp_ItemId_datagrid']/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[1]"),
     "Cash Withdrawn from Bank": (By.XPATH,"//*[@id='Frm_Voucher_Win_Cash_GLookUp_ItemId_datagrid']/div/div[6]/div/div/div[1]/div/table/tbody/tr[2]/td[1]"),
}

#loginmode_random_option = random.choice(list(loginmode_options_data.keys()))
itemname_option_locator = itemname_options_data["Cash Deposited in Bank"]
itemname_option = wait.until(EC.presence_of_element_located(itemname_option_locator))
itemname_option.click()

#check mandatory option for Cash Deposited
save_form_locator = (By.XPATH, "//*[@id='EditVouWinCash']/div")
save_form = WebDriverWait(driver, 10).until(EC.presence_of_element_located(save_form_locator))
driver.execute_script("arguments[0].click();", save_form)
time.sleep(3)
driver.find_element(By.XPATH,"//div[@aria-label='OK']//div[@class='dx-button-content']").click()
time.sleep(3)

# Select Voucher_Entries Date
current_date = datetime.datetime.now().strftime("%d-%m-%Y") # Get the current date

#Currency Denomination Details
randomvalue_2000 = random.randint(1,20)
randomvalue_500 = random.randint(1,20)
randomvalue_200 = random.randint(1,20)
randomvalue_100 = random.randint(1,20)
randomvalue_50 = random.randint(1,20)
randomvalue_20 = random.randint(1,20)
randomvalue_10 = random.randint(1,20)
randomvalue_5 = random.randint(1,20)
randomvalue_2 = random.randint(1,20)
randomvalue_1 = random.randint(1,20)

input_element_2000 = driver.find_element(By.ID, "Txt_2000_CDW")
ActionChains(driver).move_to_element(input_element_2000).click().send_keys(randomvalue_2000).perform()

input_element_500 = driver.find_element(By.ID, "Txt_500_CDW")
ActionChains(driver).move_to_element(input_element_500).click().send_keys(randomvalue_500).perform()

input_element_200 = driver.find_element(By.ID, "Txt_200_CDW")
ActionChains(driver).move_to_element(input_element_200).click().send_keys(randomvalue_200).perform()

input_element_100 = driver.find_element(By.ID, "Txt_100_CDW")
ActionChains(driver).move_to_element(input_element_100).click().send_keys(randomvalue_100).perform()

input_element_50 = driver.find_element(By.ID, "Txt_50_CDW")
ActionChains(driver).move_to_element(input_element_50).click().send_keys(randomvalue_50).perform()

input_element_20 = driver.find_element(By.ID, "Txt_20_CDW")
ActionChains(driver).move_to_element(input_element_20).click().send_keys(randomvalue_20).perform()

input_element_10 = driver.find_element(By.ID, "Txt_10_CDW")
ActionChains(driver).move_to_element(input_element_10).click().send_keys(randomvalue_10).perform()

input_element_5 = driver.find_element(By.ID, "Txt_5_CDW")
ActionChains(driver).move_to_element(input_element_5).click().send_keys(randomvalue_5).perform()

input_element_2 = driver.find_element(By.ID, "Txt_2_CDW")
ActionChains(driver).move_to_element(input_element_2).click().send_keys(randomvalue_2).perform()

input_element_1 = driver.find_element(By.ID, "Txt_1_CDW")
ActionChains(driver).move_to_element(input_element_1).click().send_keys(randomvalue_1).perform()

total_amount_locator = driver.find_element(By.ID,"Txt_Amount_CDW")
click_element(wait,total_amount_locator)

value_2000 = driver.execute_script('return $("#Txt_2000_CDW").dxNumberBox("instance").option("value")')
actual_result_2000 = 2000*value_2000

value_500 = driver.execute_script('return $("#Txt_500_CDW").dxNumberBox("instance").option("value")')
actual_result_500 = 500*value_500

value_200 = driver.execute_script('return $("#Txt_200_CDW").dxNumberBox("instance").option("value")')
actual_result_200 = 500*value_200

value_100 = driver.execute_script('return $("#Txt_100_CDW").dxNumberBox("instance").option("value")')
actual_result_100 = 100*value_100

value_50 = driver.execute_script('return $("#Txt_50_CDW").dxNumberBox("instance").option("value")')
actual_result_50 = 50*value_50

value_20 = driver.execute_script('return $("#Txt_20_CDW").dxNumberBox("instance").option("value")')
actual_result_20 = 20*value_20

value_10 = driver.execute_script('return $("#Txt_10_CDW").dxNumberBox("instance").option("value")')
actual_result_10 = 10*value_10

value_5 = driver.execute_script('return $("#Txt_5_CDW").dxNumberBox("instance").option("value")')
actual_result_5 = 5*value_5

value_2 = driver.execute_script('return $("#Txt_2_CDW").dxNumberBox("instance").option("value")')
actual_result_2 = 2*value_2

value_1 = driver.execute_script('return $("#Txt_1_CDW").dxNumberBox("instance").option("value")')
actual_result_1 = 1*value_1

expected_result_2000 = driver.execute_script('return $("#BE_2000_CDW").dxNumberBox("instance").option("value")')
expected_result_500 = driver.execute_script('return $("#BE_500_CDW").dxNumberBox("instance").option("value")')
expected_result_200 = driver.execute_script('return $("#BE_200_CDW").dxNumberBox("instance").option("value")')
expected_result_100 = driver.execute_script('return $("#BE_100_CDW").dxNumberBox("instance").option("value")')
expected_result_50 = driver.execute_script('return $("#BE_50_CDW").dxNumberBox("instance").option("value")')
expected_result_20 = driver.execute_script('return $("#BE_20_CDW").dxNumberBox("instance").option("value")')
expected_result_10 = driver.execute_script('return $("#BE_10_CDW").dxNumberBox("instance").option("value")')
expected_result_5 = driver.execute_script('return $("#BE_5_CDW").dxNumberBox("instance").option("value")')
expected_result_2 = driver.execute_script('return $("#BE_2_CDW").dxNumberBox("instance").option("value")')
expected_result_1 = driver.execute_script('return $("#BE_1_CDW").dxNumberBox("instance").option("value")')

# Compare the actual and expected results
if actual_result_2000 == expected_result_2000:
    print("Values matched: Actual_2000 =", actual_result_2000, "Expected_2000 =", expected_result_2000, "random_value_selected_2000 =", randomvalue_2000)
else:
    print("Values did not match: Actual_2000 =", actual_result_2000, "Expected_2000 =", expected_result_2000, "random_value_selected_2000 =", randomvalue_2000)

if actual_result_500 == expected_result_500:
    print("Values matched: Actual_500 =", actual_result_500, "Expected_500 =", expected_result_500, "random_value_selected_500 =", randomvalue_500)
else:
    print("Values did not match: Actual_500 =", actual_result_500, "Expected_500 =", expected_result_500, "random_value_selected_500 =", randomvalue_500)

if actual_result_200 == expected_result_200:
    print("Values matched: Actual_200 =", actual_result_200, "Expected_200 =", expected_result_200, "random_value_selected_200 =", randomvalue_200)
else:
    print("Values did not match: Actual_200 =", actual_result_200, "Expected_200 =", expected_result_200,"random_value_selected_200 =", randomvalue_200)
    
if actual_result_100 == expected_result_100:
    print("Values matched: Actual_100 =", actual_result_100, "Expected_100 =", expected_result_100, "random_value_selected_100 =", randomvalue_100)
else:
    print("Values did not match: Actual_100 =", actual_result_100, "Expected_100 =", expected_result_100, "random_value_selected_100 =", randomvalue_100)

if actual_result_50 == expected_result_50:
    print("Values matched: Actual_50 =", actual_result_50, "Expected_50 =", expected_result_50, "random_value_selected_50 =", randomvalue_50)
else:
    print("Values did not match: Actual_50 =", actual_result_50, "Expected_50 =", expected_result_50, "random_value_selected_50 =", randomvalue_50)

if actual_result_20 == expected_result_20:
    print("Values matched: Actual_20 =", actual_result_20, "Expected_20 =", expected_result_20, "random_value_selected_20 =", randomvalue_20)
else:
    print("Values did not match: Actual_20 =", actual_result_20, "Expected_20 =", expected_result_20, "random_value_selected_20 =", randomvalue_20)

if actual_result_10 == expected_result_10:
    print("Values matched: Actual_10 =", actual_result_10, "Expected_10 =", expected_result_10, "random_value_selected_10 =", randomvalue_10)
else:
    print("Values did not match: Actual_10 =", actual_result_10, "Expected_10 =", expected_result_10, "random_value_selected_10 =", randomvalue_10)

if actual_result_5 == expected_result_5:
    print("Values matched: Actual_5 =", actual_result_5, "Expected_5 =", expected_result_5, "random_value_selected_5 =", randomvalue_5)
else:
    print("Values did not match: Actual_5 =", actual_result_5, "Expected_5 =", expected_result_5, "random_value_selected_5 =", randomvalue_5)

if actual_result_2 == expected_result_2:
    print("Values matched: Actual_2 =", actual_result_2, "Expected_2 =", expected_result_2, "random_value_selected_2 =", randomvalue_2)
else:
    print("Values did not match: Actual_2 =", actual_result_2, "Expected_2 =", expected_result_2, "random_value_selected_2 =", randomvalue_2)

if actual_result_1 == expected_result_1:
    print("Values matched: Actual_1 =", actual_result_1, "Expected_1 =", expected_result_1, "random_value_selected_1 =", randomvalue_1)
else:
    print("Values did not match: Actual_1 =", actual_result_1, "Expected_1 =", expected_result_1, "random_value_selected_1 =", randomvalue_1)

# same add values for 20,10,5,1 and then check total result.
expected_total_result = driver.execute_script('return $("#Txt_Amount_CDW").dxNumberBox("instance").option("value")')

number_boxes = [
    "BE_2000_CDW", "BE_500_CDW","BE_200_CDW", "BE_100_CDW", "BE_50_CDW",
    "BE_20_CDW", "BE_10_CDW", "BE_5_CDW", "BE_2_CDW", "BE_1_CDW"
]

expected_results = []

for box_id in number_boxes:
    js_code = f'return $("#{box_id}").dxNumberBox("instance").option("value");'
    expected_result = driver.execute_script(js_code)
    expected_results.append(expected_result)

# Calculate the sum of the expected results
actual_total_result = sum(expected_results)

print("Total Sum:", actual_total_result)

if actual_total_result == expected_total_result:
    print("Values matched: actual_total_result =", actual_total_result, "expected_total_result =", expected_total_result)
else:
    print("Values did not match: actual_total_result =", actual_total_result, "expected_total_result =", expected_total_result)

# Check if the error message element is present
save_button = driver.find_element(By.XPATH, "//*[@id='EditVouWinCash']/div")
save_button.click()
error_message = driver.find_element(By.XPATH, "//div[contains(text(),'Voucher_Entries Date Incorrect / Blank. . . !')]")
if error_message.is_displayed():
    print("Error message appeared:", error_message.text)
else:
    print("No error message appeared.")

#Check for previous date

# Your existing code
current_year = date.today().year
random_year = random.randint(current_year - 10, current_year - 1)
random_month = random.randint(1, 12)

# Get the maximum number of days for the selected month
max_days = calendar.monthrange(random_year, random_month)[1]

# Generate a random day within the valid range for the selected month
random_day = random.randint(1, max_days)

random_date = date(random_year, random_month, random_day)

voucher_date = driver.find_element(By.ID, "Txt_V_Date_CDW")
ActionChains(driver).move_to_element(voucher_date).click().send_keys(random_date.strftime("%d-%m-%Y")).perform()

# Check if the error message element is present
save_button = driver.find_element(By.XPATH, "//*[@id='EditVouWinCash']/div")
save_button.click()
error_message_date = driver.find_element(By.XPATH, "//div[contains(text(),'Date Not As Per Financial Year...!')]")
if error_message_date.is_displayed():
    print("Error message appeared:", error_message_date.text)
else:
    print("No error message appeared.")

ActionChains(driver).move_to_element(voucher_date).click().send_keys(Keys.CONTROL + "a").send_keys(Keys.DELETE).perform()
# Find the start date element
voucher_date = driver.find_element(By.ID, "Txt_V_Date_CDW")
current_year_date = ActionChains(driver).move_to_element(voucher_date).click().send_keys(current_date).perform()
print("Select current year date is:", current_year_date)
time.sleep(1)

bankname_dropdown_locator = (By.XPATH, "//div[@id='GLookUp_BankList_CDW']//div[@class='dx-dropdowneditor-icon']")
#select bank detail
# Check if the error message element is present for bank
save_button = driver.find_element(By.XPATH, "//*[@id='EditVouWinCash']/div")
save_button.click()
bankname_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located(bankname_dropdown_locator))
ActionChains(driver).move_to_element(bankname_dropdown).perform()
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

bankname_options_data = {
     "Bank of Baroda": (By.XPATH,"//*[@id='Frm_Voucher_Win_Cash_GLookUp_BankList_datagrid']/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[1]"),
     "State Bank of India": (By.XPATH,"//*[@id='Frm_Voucher_Win_Cash_GLookUp_BankList_datagrid']/div/div[6]/div/div/div[1]/div/table/tbody/tr[2]/td[1]"),
}

bankname_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located(bankname_dropdown_locator))
bankname_dropdown.click()

bankname_random_option = random.choice(list(bankname_options_data.keys()))
bankname_option_locator = bankname_options_data[bankname_random_option]
bankname_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located(bankname_option_locator))
bankname_option.click()

#purpose
purpose_dropdown_locator = (By.XPATH, "//*[@id='PurposeID_CDW']/div[1]/div/div[2]/div/div/div")
save_button = driver.find_element(By.XPATH, "//*[@id='EditVouWinCash']/div")
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

# click on the save button
save_button = driver.find_element(By.XPATH, "//*[@id='EditVouWinCash']/div")
save_button.click()
print("Form saved sucessfully")
