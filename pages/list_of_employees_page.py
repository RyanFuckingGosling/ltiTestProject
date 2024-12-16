from core.base_page import BasePage

class ListOfEmployees(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_edit_button_for_employee(self, name):
        if self.is_element_display(f"//td[contains(text(), '{name}')]/..//span[contains(text(), 'Редактировать')]"):
            self.click(f"//td[contains(text(), '{name}')]/..//span[contains(text(), 'Редактировать')]")
        self.wait_for_sceleton_not_dislpay()

    def click_save_button_for_broker(self):
        if self.is_element_display("//span[contains(text(), 'Сохранить')]"):
            self.click("//span[contains(text(), 'Сохранить')]")
        self.wait_for_sceleton_not_dislpay()

    def click_button_with_text_in_field(self, field_name, button_name):
        if self.is_element_display(f"//div[contains(text(), '{field_name}')]/../following-sibling::div//span[contains(text(), '{button_name}')]"):
            self.click(f"//div[contains(text(), '{field_name}')]/../following-sibling::div//span[contains(text(), '{button_name}')]")
        self.wait_for_sceleton_not_dislpay()

    def is_document_display_in_field(self, field_name, document_name):
        return self.is_element_display(f"//div[contains(text(), '{field_name}')]/.." +
                                       f"/following-sibling::div//a[contains(text(), '{document_name}')]")
