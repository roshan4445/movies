from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class HomePage(BasePage):
    username_locator=(By.ID,"usernameInput")
    password_locator=(By.ID,"passwordInput")
    playbutton=(By.CLASS_NAME,"home-movie-play-button")
    sections_loctaor="movies-list-heading"
    def __init__(self,driver):
        super().__init__(driver)
    def section_heading(self,driver):
        sections=driver.find_elements(By.CLASS_NAME,self.sections_loctaor)
        return sections

    
    
