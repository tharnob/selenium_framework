import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



class DemoAutoSuggest:
    def demo_auto_suggest(self):

        # Launching browser and opening the travel website
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.maximize_window()


        # Provide going from location
        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys("New Delhi")
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(2)

        # Provide going to location
        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        time.sleep(2)
        going_to.send_keys("New")
        time.sleep(2)
        search_result = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]//li")
        time.sleep(2)
        print(search_result)
        print(len(search_result))
        time.sleep(2)
        for result in search_result:
            print(result.text)
            print(result)
            print("||||||||||||")
            if "New York (JFK)" in result.text:
                result.click()
                time.sleep(4)
                break


# Not a recommended way to select a calendar date


        # Select the departure date
        origin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        origin.click()
        time.sleep(4)
        # driver.find_element(By.XPATH, "//td[@id='07/12/2023']").click()
        # time.sleep(4)

# Choose a date from external file (Recommended Way)

        all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")

        print("It worked!")

        for date in all_dates:
            print(date.get_attribute("data-date"))
            if date.get_attribute("data-date") == "09/11/2023":
                date.click()
                time.sleep(5)
                break



        # Click on flight search button
        driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").click()
        time.sleep(10)


        # Select the filter 1 stop
        driver.find_element(By.XPATH, "//p[normalize-space()='1']").click()
        time.sleep(10)



# Launching browser and opening the travel website
# Provide going from location
# Provide going to location
# Select the departure date
# Click on flight search button
# Select the filter 1 stop
# Varify that the filtered results show flights having only 1 stop





autoSuggest = DemoAutoSuggest()
autoSuggest.demo_auto_suggest()