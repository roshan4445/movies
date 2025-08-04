
from pages.LoginPage import LoginPage
from selenium import webdriver
from pages.Navbar import Navbar
import pytest 
import time
class TestNavbar:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://qamoviesapp.ccbp.tech/")
        self.login = LoginPage(self.driver)
        self.login.login("rahul","rahul@2021")
        time.sleep(5)
    def test_home(self):
        nav_obj=Navbar(self.driver)
        nav_obj.home()
        
        assert self.driver.current_url=="https://qamoviesapp.ccbp.tech/"
        self.driver.quit()
    def test_popular(self):
        nav_obj=Navbar(self.driver)
        nav_obj.popular_btn()

        assert self.driver.current_url=="https://qamoviesapp.ccbp.tech/popular"
        self.driver.quit()
    def test_search_bar(self):
        nav_obj=Navbar(self.driver)
        nav_obj.search("venom")
        assert nav_obj.movies_container()==True
    def test_avatar(self):
        nav_obj=Navbar(self.driver)
        nav_obj.avatar()
        assert self.driver.current_url=="https://qamoviesapp.ccbp.tech/account"


