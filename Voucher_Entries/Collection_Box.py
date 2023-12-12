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
drop_down_1 = wait.until(EC.element_to_be_clickable((By.ID, "Accounts_Voucher_CollectionBox")))
ActionChains(driver).click(drop_down_1).perform()
time.sleep(4)

# Check if the error message element is present for Voucher Date
save_button = driver.find_element(By.XPATH, "//*[@id='CBoxVoucherEdit']/div")
save_button.click()
error_message = driver.find_element(By.XPATH, "//div[contains(text(),'Voucher Date Required')]")
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
voucher_date = driver.find_element(By.ID, "Txt_V_Date_CBox")
Last_year_date = ActionChains(driver).move_to_element(voucher_date).click().send_keys(random_date.strftime("%d-%m-%Y")).perform()
print("Selected last year date is:", Last_year_date)

# Check if the error message element is present for last year date
save_button = driver.find_element(By.XPATH, "//*[@id='CBoxVoucherEdit']/div")
save_button.click()
error_message_date = driver.find_element(By.XPATH, "//div[contains(text(),'Date Not As Per Financial Year...!')]")
if error_message_date.is_displayed():
    print("Error message appeared:", error_message_date.text)
else:
    print("No error message appeared for last year date")

ActionChains(driver).move_to_element(voucher_date).click().send_keys(Keys.CONTROL + "a").send_keys(Keys.DELETE).perform()

# Find the start date element
voucher_date = driver.find_element(By.ID, "Txt_V_Date_CBox")
ActionChains(driver).move_to_element(voucher_date).click().send_keys(current_date).perform()
print("Select current year date is:", current_date)
time.sleep(1)

#Check if the error message element is present for 1st person name
save_button = driver.find_element(By.XPATH, "//*[@id='CBoxVoucherEdit']/div")
save_button.click()
person_name_1 = driver.find_element(By.ID, "GLookUp_PartyList1_CBox")
ActionChains(driver).move_to_element(person_name_1).click().perform()
try:
   error_message_name1 = driver.find_element(By.XPATH, "//div[contains(text(),'Select First Person Name..')]")
   if error_message_name1.is_displayed():
    print("Error message appeared:", error_message_name1.text)
except NoSuchElementException:
    print("No error message appeared for 1st name")

# to be done after bug is resolved for first and second person name
# mode_dropdown_locator = (By.ID, "Cmd_Mode_B2B")
# mode_dropdown = wait.until(EC.presence_of_element_located(mode_dropdown_locator))
# mode_dropdown.click()
# time.sleep(2)
#
# mode_options_data = {
#      "CHEQUE": (By.XPATH,"//div[contains(text(),'CHEQUE')]"),
#      "DD": (By.XPATH,"//div[contains(text(),'DD')]"),
#     "CBS": (By.XPATH, "//div[contains(text(),'CBS')]"),
#     "RTGS": (By.XPATH, "//div[contains(text(),'RTGS')]"),
#     "NEFT": (By.XPATH, "//div[contains(text(),'NEFT')]"),
# }
#
# mode_random_option = random.choice(list(mode_options_data.keys()))
# mode_option_locator = mode_options_data[mode_random_option]
# mode_option = wait.until(EC.presence_of_element_located(mode_option_locator))
# mode_option.click()

#Check if the error message element is present for 2nd person name
save_button = driver.find_element(By.XPATH, "//*[@id='CBoxVoucherEdit']/div")
save_button.click()
person_name_2 = driver.find_element(By.ID, "GLookUp_PartyList2_CBox")
ActionChains(driver).move_to_element(person_name_2).click().perform()
try:
   error_message_name2 = driver.find_element(By.XPATH, "//div[contains(text(),'Select Second Person Name..')]")
   if error_message_name2.is_displayed():
    print("Error message appeared:", error_message_name2.text)
except NoSuchElementException:
    print("No error message appeared for Second name")

#Check if the error message element is present for Purpose
purpose_dropdown_locator = (By.ID, "PurposeList__CollBox")
save_button = driver.find_element(By.XPATH, "//*[@id='CBoxVoucherEdit']/div")
save_button.click()
purpose_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located(purpose_dropdown_locator))
ActionChains(driver).move_to_element(purpose_dropdown).perform()
error_message_purpose = driver.find_element(By.XPATH, "//div[contains(text(),'Purpose Cannot Be Blank..!!')]")
if error_message_purpose.is_displayed():
    print("Error message appeared:", error_message_purpose.text)
else:
    print("No error message appeared for Purpose.")

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

# Currency Denomination Details
randomvalue_2000 = random.randint(1, 20)
randomvalue_500 = random.randint(1, 20)
randomvalue_200 = random.randint(1, 20)
randomvalue_100 = random.randint(1, 20)
randomvalue_50 = random.randint(1, 20)
randomvalue_20 = random.randint(1, 20)
randomvalue_10 = random.randint(1, 20)
randomvalue_5 = random.randint(1, 20)
randomvalue_2 = random.randint(1, 20)
randomvalue_1 = random.randint(1, 20)

input_element_2000 = driver.find_element(By.ID, "Txt_2000")
ActionChains(driver).move_to_element(input_element_2000).click().send_keys(randomvalue_2000).perform()

input_element_500 = driver.find_element(By.ID, "Txt_500")
ActionChains(driver).move_to_element(input_element_500).click().send_keys(randomvalue_500).perform()

input_element_200 = driver.find_element(By.ID, "Txt_200")
ActionChains(driver).move_to_element(input_element_200).click().send_keys(randomvalue_200).perform()

input_element_100 = driver.find_element(By.ID, "Txt_100")
ActionChains(driver).move_to_element(input_element_100).click().send_keys(randomvalue_100).perform()

input_element_50 = driver.find_element(By.ID, "Txt_50")
ActionChains(driver).move_to_element(input_element_50).click().send_keys(randomvalue_50).perform()

input_element_20 = driver.find_element(By.ID, "Txt_20")
ActionChains(driver).move_to_element(input_element_20).click().send_keys(randomvalue_20).perform()

input_element_10 = driver.find_element(By.ID, "Txt_10")
ActionChains(driver).move_to_element(input_element_10).click().send_keys(randomvalue_10).perform()

input_element_5 = driver.find_element(By.ID, "Txt_5")
ActionChains(driver).move_to_element(input_element_5).click().send_keys(randomvalue_5).perform()

input_element_2 = driver.find_element(By.ID, "Txt_2")
ActionChains(driver).move_to_element(input_element_2).click().send_keys(randomvalue_2).perform()

input_element_1 = driver.find_element(By.ID, "Txt_1")
ActionChains(driver).move_to_element(input_element_1).click().send_keys(randomvalue_1).perform()

total_amount_locator = driver.find_element(By.ID, "Txt_Amount_CBox")
click_element(wait, total_amount_locator)

value_2000 = driver.execute_script('return $("#Txt_2000").dxNumberBox("instance").option("value")')
actual_result_2000 = 2000 * value_2000

value_500 = driver.execute_script('return $("#Txt_500").dxNumberBox("instance").option("value")')
actual_result_500 = 500 * value_500

value_200 = driver.execute_script('return $("#Txt_200").dxNumberBox("instance").option("value")')
actual_result_200 = 500 * value_200

value_100 = driver.execute_script('return $("#Txt_100").dxNumberBox("instance").option("value")')
actual_result_100 = 100 * value_100

value_50 = driver.execute_script('return $("#Txt_50").dxNumberBox("instance").option("value")')
actual_result_50 = 50 * value_50

value_20 = driver.execute_script('return $("#Txt_20").dxNumberBox("instance").option("value")')
actual_result_20 = 20 * value_20

value_10 = driver.execute_script('return $("#Txt_10").dxNumberBox("instance").option("value")')
actual_result_10 = 10 * value_10

value_5 = driver.execute_script('return $("#Txt_5").dxNumberBox("instance").option("value")')
actual_result_5 = 5 * value_5

value_2 = driver.execute_script('return $("#Txt_2").dxNumberBox("instance").option("value")')
actual_result_2 = 2 * value_2

value_1 = driver.execute_script('return $("#Txt_1").dxNumberBox("instance").option("value")')
actual_result_1 = 1 * value_1

expected_result_2000 = driver.execute_script('return $("#BE_2000").dxNumberBox("instance").option("value")')
expected_result_500 = driver.execute_script('return $("#BE_500").dxNumberBox("instance").option("value")')
expected_result_200 = driver.execute_script('return $("#BE_200").dxNumberBox("instance").option("value")')
expected_result_100 = driver.execute_script('return $("#BE_100").dxNumberBox("instance").option("value")')
expected_result_50 = driver.execute_script('return $("#BE_50").dxNumberBox("instance").option("value")')
expected_result_20 = driver.execute_script('return $("#BE_20").dxNumberBox("instance").option("value")')
expected_result_10 = driver.execute_script('return $("#BE_10").dxNumberBox("instance").option("value")')
expected_result_5 = driver.execute_script('return $("#BE_5").dxNumberBox("instance").option("value")')
expected_result_2 = driver.execute_script('return $("#BE_2").dxNumberBox("instance").option("value")')
expected_result_1 = driver.execute_script('return $("#BE_1").dxNumberBox("instance").option("value")')

# Compare the actual and expected results
if actual_result_2000 == expected_result_2000:
    print("Values matched: Actual_2000 =", actual_result_2000, "Expected_2000 =", expected_result_2000,
          "random_value_selected_2000 =", randomvalue_2000)
else:
    print("Values did not match: Actual_2000 =", actual_result_2000, "Expected_2000 =", expected_result_2000,
          "random_value_selected_2000 =", randomvalue_2000)

if actual_result_500 == expected_result_500:
    print("Values matched: Actual_500 =", actual_result_500, "Expected_500 =", expected_result_500,
          "random_value_selected_500 =", randomvalue_500)
else:
    print("Values did not match: Actual_500 =", actual_result_500, "Expected_500 =", expected_result_500,
          "random_value_selected_500 =", randomvalue_500)

if actual_result_200 == expected_result_200:
    print("Values matched: Actual_200 =", actual_result_200, "Expected_200 =", expected_result_200,
          "random_value_selected_200 =", randomvalue_200)
else:
    print("Values did not match: Actual_200 =", actual_result_200, "Expected_200 =", expected_result_200,
          "random_value_selected_200 =", randomvalue_200)

if actual_result_100 == expected_result_100:
    print("Values matched: Actual_100 =", actual_result_100, "Expected_100 =", expected_result_100,
          "random_value_selected_100 =", randomvalue_100)
else:
    print("Values did not match: Actual_100 =", actual_result_100, "Expected_100 =", expected_result_100,
          "random_value_selected_100 =", randomvalue_100)

if actual_result_50 == expected_result_50:
    print("Values matched: Actual_50 =", actual_result_50, "Expected_50 =", expected_result_50,
          "random_value_selected_50 =", randomvalue_50)
else:
    print("Values did not match: Actual_50 =", actual_result_50, "Expected_50 =", expected_result_50,
          "random_value_selected_50 =", randomvalue_50)

if actual_result_20 == expected_result_20:
    print("Values matched: Actual_20 =", actual_result_20, "Expected_20 =", expected_result_20,
          "random_value_selected_20 =", randomvalue_20)
else:
    print("Values did not match: Actual_20 =", actual_result_20, "Expected_20 =", expected_result_20,
          "random_value_selected_20 =", randomvalue_20)

if actual_result_10 == expected_result_10:
    print("Values matched: Actual_10 =", actual_result_10, "Expected_10 =", expected_result_10,
          "random_value_selected_10 =", randomvalue_10)
else:
    print("Values did not match: Actual_10 =", actual_result_10, "Expected_10 =", expected_result_10,
          "random_value_selected_10 =", randomvalue_10)

if actual_result_5 == expected_result_5:
    print("Values matched: Actual_5 =", actual_result_5, "Expected_5 =", expected_result_5, "random_value_selected_5 =",
          randomvalue_5)
else:
    print("Values did not match: Actual_5 =", actual_result_5, "Expected_5 =", expected_result_5,
          "random_value_selected_5 =", randomvalue_5)

if actual_result_2 == expected_result_2:
    print("Values matched: Actual_2 =", actual_result_2, "Expected_2 =", expected_result_2, "random_value_selected_2 =",
          randomvalue_2)
else:
    print("Values did not match: Actual_2 =", actual_result_2, "Expected_2 =", expected_result_2,
          "random_value_selected_2 =", randomvalue_2)

if actual_result_1 == expected_result_1:
    print("Values matched: Actual_1 =", actual_result_1, "Expected_1 =", expected_result_1, "random_value_selected_1 =",
          randomvalue_1)
else:
    print("Values did not match: Actual_1 =", actual_result_1, "Expected_1 =", expected_result_1,
          "random_value_selected_1 =", randomvalue_1)

# same add values for 20,10,5,1 and then check total result.
expected_total_result = driver.execute_script('return $("#Txt_Amount_CBox").dxNumberBox("instance").option("value")')

number_boxes = [
    "BE_2000", "BE_500", "BE_200", "BE_100", "BE_50",
    "BE_20", "BE_10", "BE_5", "BE_2", "BE_1"
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
    print("Values matched: actual_total_result =", actual_total_result, "expected_total_result =",
          expected_total_result)
else:
    print("Values did not match: actual_total_result =", actual_total_result, "expected_total_result =",
          expected_total_result)

# click on the save button
save_button = driver.find_element(By.XPATH, "//*[@id='CBoxVoucherEdit']/div")
save_button.click()
print("Form saved sucessfully")
