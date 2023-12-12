from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
Chrome_options = Options()
driver = webdriver.Chrome(options=Chrome_options, executable_path="/Driver/chromedriver.exe")
wait = WebDriverWait(driver, 10)
from selenium.webdriver.common.by import By

class Test_LoginPage():

    def __int__(self, driver):
        self.driver = driver
        self.username_textbox_id = "Txt_User"
        self.password_textbox_id = "Txt_Pass"
        self.login_button_id     = "Login"

    def enter_username(self, username):
        wait.until(EC.element_to_be_clickable((By.ID,"self.username_textbox_id"))).clear()
        wait.until(EC.element_to_be_clickable((By.ID, "self.username_textbox_id"))).send_keys(username)


        #ActionChains(driver).move_to_element(username_1).send_keys(username).perform()
        #username_1.send_keys(username)

    def enter_password(self, password):
        password_1 = wait.until(EC.element_to_be_clickable((By.NAME,"self.password_textbox_id")))
        password_1.send_keys(password)

    def click_login(self):
        login_click = wait.until(EC.element_to_be_clickable((By.ID,"login_button_id")))
        ActionChains(driver).click(login_click).perform()

