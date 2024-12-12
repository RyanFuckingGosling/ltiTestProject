from core.base_page import BasePage

LOCATOR_Dropdown = "//label[contains(text(), '{:s}')]/../div/input"
LOCATOR_DropdownValue = LOCATOR_Dropdown + "/ancestor::div[contains(@class, 'v-input')]//div[@class='v-list-item__title']"

class DropdownPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_dropdown(self, dropdown_name):
        if self.is_element_display(LOCATOR_Dropdown.format(dropdown_name)):
            self.click(LOCATOR_Dropdown.format(dropdown_name))

    def is_display_value_in_dropdown(self, dropdown_name, value):
        return self.is_element_display(LOCATOR_Dropdown.format(dropdown_name) + f"/../div[contains(text(), '{value}')]")

    def is_dropdown_display(self, dropdown_name):
        return self.is_element_display(LOCATOR_Dropdown.format(dropdown_name))
    
    def select_value_in_dropdown(self, dropdown_name, value):
        self.click_dropdown(dropdown_name)
        if self.is_element_display(LOCATOR_DropdownValue.format(dropdown_name, value)):
            self.click(LOCATOR_DropdownValue.format(dropdown_name, value))