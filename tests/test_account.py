from pages.account import AccountPage
from pages.LoginPage import LoginPage
from selenium import webdriver
import pytest 
import time
class TestAccount:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://qamoviesapp.ccbp.tech/")
        self.login = LoginPage(self.driver)
        self.login.login("rahul","rahul@2021")
        time.sleep(5)
    def test_logout(self):
        account_obj=AccountPage(self.driver)
        account_obj.logout()
        assert self.driver.current_url=="https://qamoviesapp.ccbp.tech/login"
        self.driver.quit()
        