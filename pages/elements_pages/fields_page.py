from core.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

LOCATOR_FIELD = "//label[contains(text(), '{:s}')]/following-sibling::input"

class FieldsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def clear_field_with_name(self, field_name):
        self.click(LOCATOR_FIELD.format(field_name))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element(f"//button[contains(@aria-label, 'Clear {field_name}')]")).perform()
        if self.is_element_display(f"//button[contains(@aria-label, 'Clear {field_name}')]"):
            self.click(f"//button[contains(@aria-label, 'Clear {field_name}')]")

    def is_field_display(self, field_name):
        if self.is_element_display(LOCATOR_FIELD.format(field_name)):
            return True
        return False
    
    def get_text_from_field(self, field_name):
        return self.find_element(LOCATOR_FIELD.format(field_name)).text

    def send_keys_to_field(self, field_name, text):
        if self.is_field_display(field_name):
            self.find_element(LOCATOR_FIELD.format(field_name)).clear()
            self.find_element(LOCATOR_FIELD.format(field_name)).send_keys(text)