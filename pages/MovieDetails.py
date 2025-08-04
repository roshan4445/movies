from selenium.webdriver.common.by import By

class MovieDetailsPage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.find_element(By.CLASS_NAME, "movie-title").text

    def get_overview(self):
        return self.driver.find_element(By.CLASS_NAME, "movie-overview").text

    def get_runtime(self):
        return self.driver.find_element(By.CLASS_NAME, "movie-runtime").text

    def get_rating(self):
        return self.driver.find_element(By.CLASS_NAME, "movie-vote-average").text

    def get_genre(self):
        return self.driver.find_element(By.CLASS_NAME, "movie-genre").text

    def get_back_button(self):
        return self.driver.find_element(By.CLASS_NAME, "back-button")  # Optional
