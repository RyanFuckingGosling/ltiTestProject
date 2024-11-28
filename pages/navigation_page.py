from core.base_page import BasePage


LOCATOR_TAB_NAME = "//div[@role='button']//div[contains(text(), '{:s}')]/.."
LOCATOR_SECTION_NAME = LOCATOR_TAB_NAME + "/ancestor::div[contains(@class, 'v-list-group--active')]//div[contains(text(), '{:s}')]"


class NavigationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_tab(self, tab_name):
        if self.is_tab_display(tab_name):
            self.find_element(LOCATOR_TAB_NAME.format(tab_name)).click()

    def click_menu_button(self):
        self.click("//button[contains(@class, 'v-app-bar__nav-icon')]")

    def click_profile_button(self):
        self.click("//a[contains(@class, 'user-account__login')]")

    def is_block_clicable(self, block_name):
        return self.is_element_display(f"//span[contains(text(), '{block_name}')]/ancestor::div[contains(@class, 'col-md')]//a")

    def is_tab_display(self, tab_name):
        return self.is_element_display(LOCATOR_TAB_NAME.format(tab_name))
    
    def is_navigation_menu_open(self):
        return not self.is_element_display("//nav[contains(@class, 'mini-variant')]")

    def select_section_from_tab(self, tab_name, section_name):
        self.click_tab(tab_name)
        if self.is_element_display(LOCATOR_SECTION_NAME.format(tab_name, section_name)):
            self.click(LOCATOR_SECTION_NAME.format(tab_name, section_name))
        else:
            self.click_tab(tab_name)
            self.click(LOCATOR_SECTION_NAME.format(tab_name, section_name))
            self.wait_for_sceleton_not_dislpay()