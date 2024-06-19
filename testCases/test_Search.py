import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.HomePage import HomePage
from pageObjects.CatalogSearch import CatalogSearch


# For search, the user should be able to find all products containing the keyword in the product title.
# Products not containing the keyword should not display results.
class TestSearch(unittest.TestCase):
    # driver = None
    driver = None

    @classmethod
    def setUpClass(cls):
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.maximize_window()

    # Verify search result using a valid keyword
    def test_validateSearchFromList(self):
        print("Running test_validateSearchFromList")
        # Launching website
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        catalogSearch = CatalogSearch(driver)
        homepage = HomePage(driver)
        # Verify search result using a valid keyword
        homepage.type_into_search_field("Jackets for women")
        homepage.select_listed_item()
        homepage.assert_url("Jackets for women")
        catalogSearch.assert_all_items_contain_keyword("Jacket")

    # Verify search result using a valid keyword using the enter key
    def test_validateSearchFromEnterKey(self):
        print("Running test_validateSearchFromEnterKey")
        # Launching website
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        catalogSearch = CatalogSearch(driver)
        homepage = HomePage(driver)
        # Verify search result using a valid keyword
        homepage.type_into_search_field("Shorts")
        homepage.perform_enter_action_in_search_field()
        homepage.assert_url("Shorts")
        catalogSearch.assert_all_items_contain_keyword("Short")

    # Verify search result using a valid keyword by clicking on the loop icon
    def test_validateSearchFromLoopIcon(self):
        print("Running test_validateSearchFromLoopIcon")
        # Launching website
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        catalogSearch = CatalogSearch(driver)
        homepage = HomePage(driver)
        # Verify search result using a valid keyword
        homepage.type_into_search_field("Yoga")
        homepage.click_on_loop_search_icon()
        homepage.assert_url("Yoga")
        catalogSearch.assert_all_items_contain_keyword("Yoga")

    # Verify search result using an invalid keyword
    def test_validateSearchInvalidKey(self):
        print("Running test_validateSearchInvalidKey")
        # Launching website
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        catalogSearch = CatalogSearch(driver)
        homepage = HomePage(driver)
        # Verify search result using a valid keyword
        homepage.type_into_search_field("Towels")
        homepage.perform_enter_action_in_search_field()
        catalogSearch.assert_invalid_results("Your search returned no results.")

    # Verify search result using an empty field
    def test_validateEmptySearch(self):
        print("Running test_validateEmptySearch")
        # Launching website
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        catalogSearch = CatalogSearch(driver)
        homepage = HomePage(driver)
        # Verify search result using a valid keyword
        homepage.type_into_search_field("")
        homepage.perform_enter_action_in_search_field()
        page_source = driver.page_source
        assert "Please enter a search keyword" in page_source, "Expected text not found on the page"

    @classmethod
    def tearDownClass(cls):
        print("Running tearDownClass")
        cls.driver.close()
        cls.driver.quit()
        super().tearDownClass()


if __name__ == '__main__':
    unittest.main()
