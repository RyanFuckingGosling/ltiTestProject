from core.base_page import BasePage

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def is_block_with_name_clickable(self, block_name):
        return self.is_element_clickable(f"//span[contains(text(), '{block_name}')]/../..")
    
    def is_display_news_block(self):
        return self.is_element_display("//h2[contains(text(), 'Новости')]/..")
    
    def is_display_title(self, title):
        return self.is_element_display(f"//div[contains(@class, 'v-toolbar__title')][contains(text(), '{title}')]")