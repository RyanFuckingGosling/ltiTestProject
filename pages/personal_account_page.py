from core.base_page import BasePage

class PersonalAccount(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def is_display_create_button_in_field(self, field_name):
        return self.is_element_display(f"//div[contains(text(), '{field_name}')]/../button//span[contains(text(), 'Сформировать')]")
    
    def is_display_broker_allert_with_text(self, text):
        return self.is_element_display(f"//div[@role='alert']//div[contains(text(), '{text}')]")

    def is_display_value_in_field(self, field_name):
        return self.is_element_display(f"//div[contains(text(), '{field_name}')]/../div[contains(@class, 'value-column col')]")
    