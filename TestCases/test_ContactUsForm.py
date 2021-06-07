import unittest

from selenium import webdriver
from PageObjects.ContactUsPage import ContactUsPage
from PageObjects.HomePage import HomePage


class TestHomePage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_validateContactUs(self):
        # Launching website
        driver = self.driver
        driver.get("http://automationpractice.com")
        homepage = HomePage(driver)
        # Validate success Contact us form sent
        homepage.navigateToContactUs()
        contactUs = ContactUsPage(driver)
        contactUs.selectSubjectHeading("Customer service")
        contactUs.enterEmailAddress("test@test.com")
        contactUs.enterOrderReference("12345")
        contactUs.enterMessage("Test message here")
        contactUs.sendForm()
        driver.implicitly_wait(5)
        self.driver.save_screenshot("../Screenshots/" + "test_valid_contactUsFormSubmit.png")
        self.assertEqual("Your message has been successfully sent to our team.", contactUs.getMessageSent(),
                         "Contact us message sent is not displayed")
        # Navigate to ContactUs page
        homepage.navigateToContactUs()
        # Validate Subject Header
        contactUs = ContactUsPage(driver)
        contactUs.enterEmailAddress("test@test.com")
        contactUs.enterOrderReference("12345")
        contactUs.enterMessage("Test")
        contactUs.sendForm()
        driver.implicitly_wait(5)
        self.assertEqual("Please select a subject from the list provided.", contactUs.getError(),
                         "Subject Header is not validated")
        self.driver.save_screenshot("../Screenshots/" + "test_invalid_subjectHeader.png")
        # Validate Email address
        contactUs.selectSubjectHeading("Customer service")
        contactUs.enterEmailAddress("")
        contactUs.sendForm()
        driver.implicitly_wait(5)
        self.assertEqual("Invalid email address.", contactUs.getError(),
                         "Email address is not validated")
        self.driver.save_screenshot("../Screenshots/" + "test_empty_emailAddress.png")
        contactUs.enterEmailAddress("test.test")
        contactUs.sendForm()
        driver.implicitly_wait(5)
        self.assertEqual("Invalid email address.", contactUs.getError(),
                         "Email address is not validated")
        self.driver.save_screenshot("../Screenshots/" + "test_invalid_emailAddress.png")
        # Validate Message text box
        contactUs.enterEmailAddress("test@test.com")
        contactUs.enterMessage("")
        contactUs.sendForm()
        driver.implicitly_wait(5)
        self.assertEqual("The message cannot be blank.", contactUs.getError(),
                         "Message is not validated")
        self.driver.save_screenshot("../Screenshots/" + "test_invalid_message.png")
        # Validate Order reference
        contactUs.enterMessage("Test Message here")
        contactUs.enterOrderReference("")
        contactUs.sendForm()
        driver.implicitly_wait(5)
        self.driver.save_screenshot("../Screenshots/" + "test_invalid_orderReference.png")
        self.assertEqual("The order reference cannot be blank.", contactUs.getError(),
                         "Order Reference is not validated")

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
