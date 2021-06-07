from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.contactUs_link_xpath = "//*[@id='contact-link']/a"

    def navigateToContactUs(self):
        self.driver.find_element(By.XPATH, self.contactUs_link_xpath).click()
