from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class LoginPage(BasePage):
    username_locator=(By.ID,"usernameInput")
    password_locator=(By.ID,"passwordInput")
    button=(By.CLASS_NAME,"login-button")
    error_msg_locator=(By.CLASS_NAME,"error-message")
    def __init__(self,driver):
        super().__init__(driver)
    def login(self,username,password):
        self.do_send_keys(self.username_locator,username)
        self.do_send_keys(self.password_locator,password)
        self.do_click(self.button)
    def get_error_message(self):
        return self.get_element_text(self.error_msg_locator)
