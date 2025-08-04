from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class Navbar(BasePage):
    homes=(By.CSS_SELECTOR,".nav-link.active-nav-link[href='/']")
    popular=(By.CSS_SELECTOR,".nav-link[href='/popular']")
    search_bar=(By.ID,"search")
    serach_btn=(By.CLASS_NAME,"search-button")
    serach_btn_empty=(By.CLASS_NAME,"search-empty-button")
    movie=(By.CLASS_NAME,"search-movies-container")
    avatars=(By.CLASS_NAME,"avatar-img")
    def __init__(self,driver):
        super().__init__(driver)
    def home(self):
        self.do_click(self.homes)
    def popular_btn(self):
        self.do_click(self.popular)
    def search(self,movie_name):
        self.do_click(self.serach_btn_empty)
        self.do_send_keys(self.search_bar,movie_name)
        self.do_click(self.serach_btn)
    def movies_container(self):
        return self.is_visible(self.movie)
    def avatar(self):
        self.do_click(self.avatars)