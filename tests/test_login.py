from pages.LoginPage import LoginPage
import pytest 
import time
class TestLogin:
    def test_correct_cred(self, driver):
        login_obj = LoginPage(driver)
        login_obj.login("rahul","rahul@2021")
        time.sleep(2)
        print(driver.current_url)
        assert driver.current_url == "https://qamoviesapp.ccbp.tech/"
        driver.save_screenshot("sucessfull_logion.png")
    def test_empty_fields(self,driver):
        login_obj = LoginPage(driver)
        login_obj.login("","")
        time.sleep(2)
        assert login_obj.get_error_message != "*Username or password is invalid"
        driver.save_screenshot("sucessfull_logion.png")
    def test_username_empty(self,driver):
        login_obj = LoginPage(driver)
        login_obj.login("","rahul@2021")
        time.sleep(2)
        assert login_obj.get_error_message != "*Username or password is invalid"
    def test_wrong_credentails(self,driver):
        login_obj = LoginPage(driver)
        login_obj.login("ramya","rahul@2021")
        time.sleep(2)
        assert login_obj.get_error_message != "*username and password didn't match"

    

