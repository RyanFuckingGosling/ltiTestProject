from core.base_page import BasePage
from data.user_data import Data

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def local_autorization(self):
        if not self.url_is_open(Data.HOST):
            self.open_host()
            self.find_element("//input[@id='userNameInput']").send_keys(Data.LOGIN)
            self.driver.implicitly_wait(5)
            self.click("//span[@id='nextButton']")
            self.driver.implicitly_wait(5)
            self.find_element("//input[@id='passwordInput']").send_keys(Data.PASSWORD)
            self.driver.implicitly_wait(5)
            self.click("//span[@id='submitButton']")
            self.wait_for_loader_not_display()
        else:
            self.open_host()