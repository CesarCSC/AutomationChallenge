from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CatalogSearch:

    def __init__(self, driver):
        self.driver = driver
        self.item_list_xpath = "//ol[@class='products list items product-items']//strong/a"
        self.search_result_message_xpath = "//*[@id='maincontent']/div[3]/div[1]/div[2]"

    def assert_all_items_contain_keyword(self, keyItem):
        # Wait for the product list to load, adjust selector as needed
        product_list = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "products"))
        )

        # Find all <li> elements under the product list
        li_elements = product_list.find_elements(By.XPATH, self.item_list_xpath)

        for li in li_elements:
            # Get the text content of the <li> element
            li_text = li.text
            # Print actual vs expected text
            print(f"Actual: {li_text} - Expected to contain: {keyItem}")
            # Assert that keyItem is in the li_text
            assert keyItem in li_text, f"Expected '{keyItem}' in element: {li_text}"

    def assert_invalid_results(self, expected_message):
        search_result = self.driver.find_element(By.XPATH, self.search_result_message_xpath)
        actual_message = search_result.text.strip()
        assert actual_message == expected_message, f"Expected message '{expected_message}', but got '{actual_message}'"
        print(f"Actual: {actual_message} - Expected : {expected_message}")
