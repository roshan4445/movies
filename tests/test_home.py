from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from selenium import webdriver
import pytest 
import time
class TestHome:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://qamoviesapp.ccbp.tech/")
        self.login = LoginPage(self.driver)
        self.login.login("rahul","rahul@2021")
        time.sleep(5)
    def test_paly_button(self):
        home_obj=HomePage(self.driver)
        assert home_obj.is_visible(home_obj.playbutton)
        self.driver.quit()
    def test_section_heading(self):
        home_obj=HomePage(self.driver)
        sections=home_obj.section_heading(self.driver)
        print(sections)
        assert sections[0].text=="Trending Now"
        assert sections[1].text=="Originals"
        self.driver.quit()
        


