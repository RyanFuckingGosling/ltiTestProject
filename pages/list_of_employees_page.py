from core.base_page import BasePage

class ListOfEmployees(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_edit_button_for_employee(self, name):
        if self.is_element_display(f"//td[contains(text(), '{name}')]/..//span[contains(text(), 'Редактировать')]"):
            self.click(f"//td[contains(text(), '{name}')]/..//span[contains(text(), 'Редактировать')]")

    def click_save_button_for_broker(self):
        if self.is_element_display("//span[contains(text(), 'Сохранить')]"):
            self.click("//span[contains(text(), 'Сохранить')]")
        self.wait_for_sceleton_not_dislpay()