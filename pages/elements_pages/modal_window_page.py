from core.base_page import BasePage

LOCATOR_MODAL_WINDOW = "//div[@role = 'dialog']"

class ModalWindow(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def is_modal_window_display(self, window_name):
        return self.is_element_display(LOCATOR_MODAL_WINDOW + 
                                       f"//div[contains(@class, 'toolbar__title')][contains(text(), '{window_name}')]")
    
    def click_button_in_modal_window(self, button_name):
        if self.is_element_display(LOCATOR_MODAL_WINDOW + f"//span[contains(text(), '{button_name}')]"):
            self.click(LOCATOR_MODAL_WINDOW + f"//span[contains(text(), '{button_name}')]")
            self.wait_for_sceleton_not_dislpay()