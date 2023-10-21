from selenium.webdriver.common.by import By
import time


class Second_page:
    def __init__(self, driver):
        self.driver = driver

    def filter_page(self):
        self.driver.find_element(By.XPATH, "//p[normalize-space()='1']").click()
        time.sleep(10)