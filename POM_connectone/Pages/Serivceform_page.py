import datetime
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

Chrome_options = Options()
chrome_service = Service(executable_path="C:\\Users\Shantanu\PycharmProjects\Connectone\Driver\chromedriver.exe")
driver = webdriver.Chrome(options=Chrome_options, service= chrome_service)
driver.implicitly_wait(20)
driver.get("https://connectonetest.bkinfo.in/Start/Login/Frm_Auditor_Login/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# For element not intractable
username =wait.until(EC.element_to_be_clickable((By.ID,"Txt_User")))
ActionChains(driver).move_to_element(username).send_keys("bkshantanu").perform()

password = wait.until(EC.element_to_be_clickable((By.NAME,"Txt_Pass")))
password.send_keys("babatest")

login_click = wait.until(EC.element_to_be_clickable((By.ID,"Login")))
ActionChains(driver).click(login_click).perform()

def click_element(wait, locator):
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()

# Click elements with explicit waits
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
driver.find_element(By.ID,"Facility_Main").click()
drop_down = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='Facility_GodlyServices']")))
ActionChains(driver).click(drop_down).perform()
drop_down_1 = wait.until(EC.element_to_be_clickable((By.ID,"Facility_ChartInfo")))
ActionChains(driver).click(drop_down_1).perform()

create_form = (By.XPATH,"//*[@id='ChartInfoCreateForm']/div/span")
click_element(wait,create_form)
time.sleep(10)

form_number_counter = 2  # Start with the desired initial form number
first_name = wait.until(EC.presence_of_element_located((By.ID, "FormName_createForm")))
form_number = f"Form no.{form_number_counter}"  # Generate the form number based on the counter
ActionChains(driver).move_to_element(first_name).click().send_keys(form_number).perform() # Click the element and input the form number

current_date = datetime.datetime.now().strftime("%d-%m-%Y") # Get the current date

# Find the start date element
start_date = driver.find_element(By.ID, "StartDate_createForm")
ActionChains(driver).move_to_element(start_date).click().send_keys(current_date).perform() # Click the element and input the current date

# Find the end date element
current_date = datetime.datetime.now()
end_date = current_date + datetime.timedelta(days=2) # end date as 2 days after the current date
formatted_end_date = end_date.strftime("%d-%m-%Y")
end_date_element = driver.find_element(By.ID, "EndDate_createForm")

# Click the element and input the calculated end date
ActionChains(driver).move_to_element(end_date_element).click().send_keys(formatted_end_date).perform()

# Selecting Login Mode
loginmode_dropdown_locator = (By.XPATH, "//*[@id='FormLoginRequired_createForm']/div[1]/div/div[2]/div[2]/div/div")

loginmode_options_data = {
     "EMAIL": (By.XPATH,"(//div[contains(text(),'EMAIL')])[1]"),
     "MOBILE OR EMAIL": (By.XPATH,"//div[contains(text(),'MOBILE OR EMAIL')]"),
     "NONE": (By.XPATH, "//div[contains(text(),'NONE')]"),
}

loginmode_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located(loginmode_dropdown_locator))
loginmode_dropdown.click()

loginmode_random_option = random.choice(list(loginmode_options_data.keys()))
loginmode_option_locator = loginmode_options_data[loginmode_random_option]
loginmode_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located(loginmode_option_locator))
loginmode_option.click()

#Selecting Form purpose
purpose_locator = (By.XPATH, "//*[@id='Purpose_createForm']/div[1]/div/div[2]/div[2]/div/div")

purpose_options_data = {
     "CHART": (By.XPATH,"//div[contains(text(),'CHART')]"),
     "REGISTRATION": (By.XPATH,"//div[contains(text(),'REGISTRATION')]"),
     "FORM": (By.XPATH, "(//div[contains(text(),'FORM')])[1]"),
     "FEEDBACK": (By.XPATH,"//div[contains(text(),'FEEDBACK')]"),
     "TRAVEL DETAIL": (By.XPATH,"//div[contains(text(),'TRAVEL DETAIL')]"),
     "ACCOMODATION": (By.XPATH, "//div[contains(text(),'ACCOMMODATION')]"),
}

purpose_dropdowns = WebDriverWait(driver, 10).until(EC.presence_of_element_located(purpose_locator))
purpose_dropdowns.click()
purpose_randommode_option = random.choice(list(purpose_options_data.keys()))
purpose_option_locator = purpose_options_data[purpose_randommode_option]
purpose_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located(purpose_option_locator))
purpose_option.click()

#Selecting project
project_locator = (By.XPATH, "//*[@id='ProjectID_createForm']/div[1]/div/div[2]/div/div/div")

project_options_data = {
     "7 Billion Acts of Goodness": (By.XPATH,"//div[contains(text(),'7 Billion Acts of Goodness')]"),
     "Blood Donation Camp": (By.XPATH,"//div[contains(text(),'Blood Donation Camp')]"),
     "CAD Project (Heart Problems Project)": (By.XPATH, "//div[contains(text(),'CAD Project (Heart Problems Project)')]"),
     "Clean India Mission": (By.XPATH,"//div[contains(text(),'Clean India Mission')]"),
     "Clean the Mind Green the Earth": (By.XPATH,"//div[contains(text(),'Clean the Mind Green the Earth')]"),
}


project_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located(project_locator))
project_dropdown.click()

project_randommode_option = random.choice(list(project_options_data.keys()))
project_option_locator = project_options_data[project_randommode_option]
project_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located(project_option_locator))
project_option.click()

suffix = wait.until(EC.presence_of_element_located((By.ID,"RegNoPrefix_createForm")))
ActionChains(driver).move_to_element(suffix).click().send_keys("H").perform()

start_msg = driver.find_element(By.XPATH,"//*[@id='StartDateMsg_createForm']/div[2]/div[1]/p")
ActionChains(driver).move_to_element(start_msg).click().send_keys("Hello everyone").perform()

end_msg = driver.find_element(By.XPATH,"//*[@id='EndDateMsg_createForm']/div[2]/div[1]/p")
ActionChains(driver).move_to_element(end_msg).click().send_keys("Thank you").perform()

# add questions
add_question_1 = driver.find_element(By.XPATH,"//*[@id='devextreme228']/div")
ActionChains(driver).move_to_element(add_question_1).click(add_question_1).perform()

question_1 = wait.until(EC.element_to_be_clickable((By.ID,"Section_0__Question")))
ActionChains(driver).move_to_element(question_1).click().send_keys("Tell me about yourself").perform()

#Selecting Answer Mode
answer_mode_locator = (By.ID, "Section_0__Mode")

answer_mode_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located(answer_mode_locator))
answer_mode_dropdown.click()

answer_mode_option_locator = (By.XPATH, "//div[contains(text(),'Short Answer')]")
answer_mode_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located(answer_mode_option_locator))
answer_mode_option.click()

#question tag drop down
question_tag_locator = (By.XPATH, "//*[@id='Section[0].Tag']/div[1]/div/div[2]/div/div/div")

question_tag_options_data = {
     "Accommodation Preference": (By.XPATH,"//div[contains(text(),'Accommodation Preference')]"),
     "Accommodation Remarks": (By.XPATH,"//div[contains(text(),'Accommodation Remarks')]"),
     "Age": (By.XPATH, "//div[@class='dx-item-content dx-list-item-content'][normalize-space()='Age']"),
     "Arrival Date": (By.XPATH,"//div[contains(text(),'Arrival Date')]"),
     "Arrival Time": (By.XPATH,"//div[contains(text(),'Arrival Time')]"),
     "Assignee": (By.XPATH,"//div[contains(text(),'Assignee')]"),
     "Departure Date": (By.XPATH,"//div[contains(text(),'Departure Date')]"),
     "Departure Time": (By.XPATH,"//div[contains(text(),'Departure Time')]"),
     "Chart Date": (By.XPATH,"//div[contains(text(),'Chart Date')]"),
     "Communication Mode": (By.XPATH, "//div[contains(text(),'Communication Mode')]"),
     "Event Purpose": (By.XPATH, "//div[contains(text(),'Event Purpose')]"),
     "Gender": (By.XPATH, "//div[contains(text(),'Gender')]"),
     "Journey Food": (By.XPATH, "//div[contains(text(),'Journey Food')]"),
     "Name": (By.XPATH, "//div[@class='dx-item-content dx-list-item-content'][normalize-space()='Name']"),
     "Need Transport": (By.XPATH, "//div[contains(text(),'Need Transport')]"),
     "Payment Mode": (By.XPATH, "//div[contains(text(),'Payment Mode')]"),
     "Points to be Totalled": (By.XPATH, "//div[contains(text(),'Points to be Totalled')]"),
     "Total Registration Count": (By.XPATH, "//div[contains(text(),'Total Registration Count')]"),
     "Wing": (By.XPATH, "//div[contains(text(),'Wing')]"),
}

question_tag_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located(question_tag_locator))
question_tag_dropdown.click()

tag_option_locator = question_tag_options_data["Arrival Date"]
# question_tag_randommode_option = random.choice(list(question_tag_options_data.keys()))
#tag_option_locator = question_tag_options_data[question_tag_randommode_option]
question_tag_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located(tag_option_locator))
question_tag_option.click()

add_question_2 = driver.find_element(By.XPATH,"//*[@id='devextreme228']/div")
ActionChains(driver).move_to_element(add_question_2).click(add_question_2).perform()

question_2 = wait.until(EC.element_to_be_clickable((By.ID,"Section_1__Question")))
ActionChains(driver).move_to_element(question_2).click().send_keys("Do you know Rajyoga Meditation").perform()

#Selecting Answer Mode
answer_mode_locator_2 = (By.ID, "Section_1__Mode")

answer_mode_dropdown_2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(answer_mode_locator_2))
answer_mode_dropdown_2.click()

answer_mode_option_locator_2 = (By.XPATH, "(//div[contains(text(),'Paragraph')])[2]")
answer_mode_option_2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(answer_mode_option_locator_2))
answer_mode_option_2.click()

save_form_locator = (By.XPATH, "//div[@title='Save Form']//div")
save_form = WebDriverWait(driver, 10).until(EC.presence_of_element_located(save_form_locator))

# Scroll to the button (if needed)
driver.execute_script("arguments[0].scrollIntoView();", save_form)

# Click the button using JavaScript
driver.execute_script("arguments[0].click();", save_form)
time.sleep(2)

unique_formname_locator = (By.XPATH,"//div//div[@data-bind='dxControlsDescendantBindings: true']//div//div//div//div//div//div[@aria-label='OK']//div")
unique_formname = WebDriverWait(driver, 10).until(EC.presence_of_element_located(unique_formname_locator))
unique_formname.click()
time.sleep(2)

form_number_counter = 2

def input_and_save_form_number(form_number):
    first_name = wait.until(EC.presence_of_element_located((By.ID, "FormName_createForm")))
    driver.find_element(By.XPATH, "//*[@id='FormName_createForm']/div/div[2]/span/span").click()
    time.sleep(2)
    ActionChains(driver).move_to_element(first_name).click().send_keys(form_number).perform()
    save_form_locator = (By.XPATH, "//div[@title='Save Form']//div")
    save_form = WebDriverWait(driver, 10).until(EC.presence_of_element_located(save_form_locator))
    driver.execute_script("arguments[0].scrollIntoView();", save_form)
    driver.execute_script("arguments[0].click();", save_form)

while True:
    form_number = f"Form no.{form_number_counter}"

    try:
        input_and_save_form_number(form_number)
        id_unique_locator = (By.XPATH, "//*[@id='Application_Body']/div[5]/div/div/div[3]/div/div[2]/div/div/div/div")
        driver.find_element(*id_unique_locator).click()
        print(f"Form number {form_number} is not unique, trying the next one.")
        form_number_counter += 1
    except NoSuchElementException:
        print(f"Form number {form_number} is unique.")
        break

time.sleep(15)

