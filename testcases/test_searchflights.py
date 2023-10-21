import time
import pytest
from pages.yatra_launch_page import LaunchPage
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter:


    def test_search_flights(self):

        # Launching browser and opening the travel website


        # Provide going from location
        lp = LaunchPage(self.driver)
        lp.departFrom("New Delhi")

        # Provide going to location
        lp.going_to("New York")

# Not a recommended way to select a calendar date


        # Select the departure date
        lp.selectDate("24/10/2023")

# Choose a date from external file (Recommended Way)

        # Click on flight search button
        lp.clickSearch()

        # Select the filter 1 stop
        self.driver.find_element(By.XPATH, "//p[normalize-space()='1']").click()
        time.sleep(10)



# Launching browser and opening the travel website
# Provide going from location
# Provide going to location
# Select the departure date
# Click on flight search button
# Select the filter 1 stop
# Varify that the filtered results show flights having only 1 stop
# Again Push 1




# autoSuggest = TestSearchAndVerifyFilter()
# autoSuggest.test_search_flights()