import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ContactUsPage:

    def __init__(self, driver):
        self.driver = driver
        self.contactUs_subjectHeading_ddl_xpath = "//*[@id='id_contact']"
        self.contactUs_emailAddress_input_id = "email"
        self.contactUs_orderReference_input_id = "id_order"
        self.contactUs_attachFile_btn_id = "fileUpload"
        self.contactUs_message_txtBox_id = "message"
        self.contactUs_send_btn_id = "submitMessage"
        self.contactUs_error_label_xpath = "//*[@id='center_column']//li"
        self.contactUs_successful_label_xpath = "//*[@id='center_column']/p"

    def selectSubjectHeading(self, subjectHeading):
        subject = Select(self.driver.find_element(By.XPATH, self.contactUs_subjectHeading_ddl_xpath))
        subject.select_by_visible_text(subjectHeading)

    def enterEmailAddress(self, emailAddress):
        email = self.driver.find_element(By.ID, self.contactUs_emailAddress_input_id)
        email.clear()
        email.send_keys(emailAddress)

    def enterOrderReference(self, orderReference):
        order = self.driver.find_element(By.ID, self.contactUs_orderReference_input_id)
        order.clear()
        order.send_keys(orderReference)

    def enterMessage(self, msg):
        message = self.driver.find_element(By.ID, self.contactUs_message_txtBox_id)
        message.clear()
        message.send_keys(msg)

    def attachFile(self, file):
        attachFile = self.driver.find_element(By.ID, self.contactUs_attachFile_btn_id)
        attachFile.send_keys(self.filename(file))

    def filename(self, file):
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), file)

    def sendForm(self):
        self.driver.find_element(By.ID, self.contactUs_send_btn_id).click()

    def getError(self):
        return self.driver.find_element(By.XPATH, self.contactUs_error_label_xpath).text

    def getMessageSent(self):
        return self.driver.find_element(By.XPATH, self.contactUs_successful_label_xpath).text
