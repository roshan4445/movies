
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    def do_click(self, by_locator):
        wait=WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        wait=WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        wait=WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located(by_locator))

    
    def is_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False
