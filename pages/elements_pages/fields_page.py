from core.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

LOCATOR_FIELD = "//label[contains(text(), '{:s}')]/following-sibling::input"

class FieldsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def is_display_field(self, field_name):
        if self.is_element_display(LOCATOR_FIELD.format(field_name)):
            return True
        return False
    
    def is_display_text_in_field(self, field_name, text):
        if self.is_display_field(field_name):
            pass

    def send_keys_to_field(self, field_name, text):
        if self.is_display_field(field_name):
            self.find_element(LOCATOR_FIELD.format(field_name)).clear()
            self.find_element(LOCATOR_FIELD.format(field_name)).send_keys(text)