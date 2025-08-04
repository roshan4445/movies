from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class AccountPage(BasePage):
    logout_btn=(By.CLASS_NAME,"logout-button")
    avatars_nav=(By.CLASS_NAME,"avatar-img")
    def __init__(self,driver):
        super().__init__(driver)
    def logout(self):
        self.do_click(self.avatars_nav)
        self.do_click(self.logout_btn)