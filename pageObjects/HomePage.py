import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.search_input_xpath = "//*[@id='search']"
        self.search_lsted_item_xpath = "//*[@id='qs-option-0']/span[1]"
        self.search_loop_icon_xpath = "//*[@id='search_mini_form']/div[2]/button"

    def type_into_search_field(self, searchKey):
        search = self.driver.find_element(By.XPATH, self.search_input_xpath)
        search.clear()
        search.send_keys(searchKey)

    def select_listed_item(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.search_lsted_item_xpath).click()

    def perform_enter_action_in_search_field(self):
        search = self.driver.find_element(By.XPATH, self.search_input_xpath)
        search.send_keys(Keys.ENTER)

    def click_on_loop_search_icon(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.search_loop_icon_xpath).click()

    def assert_url(self, keyUrl):
        # Get the current page URL
        current_url = self.driver.current_url

        # Print actual vs expected URL
        print(f"Current URL: {current_url} - Expected to contain: {keyUrl}")
