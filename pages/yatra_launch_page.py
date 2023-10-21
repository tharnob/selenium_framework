import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class LaunchPage:
    def __init__(self, driver):
        self.driver = driver


    def departFrom(self, departLocation):

        depart_from = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys(departLocation)
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(2)

    def going_to(self, goingtoLocation):

        going_to = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        time.sleep(2)
        going_to.send_keys(goingtoLocation)
        time.sleep(2)
        search_result = self.driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]//li")
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


    def selectDate(self, departuredate):
        origin = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        origin.click()
        time.sleep(4)
        # driver.find_element(By.XPATH, "//td[@id='07/12/2023']").click()
        # time.sleep(4)

        all_dates = self.driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")

        print("It worked!")

        for date in all_dates:
            print(date.get_attribute("data-date"))
            if date.get_attribute("data-date") == departuredate:
                date.click()
                time.sleep(5)
                break

    def clickSearch(self):

        self.driver.find_element(By.XPATH,
                                 "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").click()
        time.sleep(10)