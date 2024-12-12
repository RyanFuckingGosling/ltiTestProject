from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from data.user_data import Data


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, poll_frequency=1)

    def is_allert_with_text_display(self, allert_title, allert_text):
        locator_allert = ("xpath", "//div[@class='v-alert__content']")
        self.wait.until(EC.presence_of_element_located(locator_allert))
        return self.is_element_display(f"//div[@class='v-alert__content']/h3[contains(text(), "
                                       f"'{allert_title}')]/../div[contains(text(), '{allert_text}')]")

    def open_host(self):
        self.driver.get(Data.HOST)

    def open_url(self, path_url):
        self.driver.get(path_url)

    def url_is_open(self, url):
        if url in self.driver.current_url:
            return True
        return False

    def find_element(self, locator):
        locator_tuple = ("xpath", locator)
        self.wait.until(EC.element_to_be_clickable(locator_tuple))
        return self.driver.find_element(By.XPATH, locator)

    def get_attribute_value(self, locator, attr):
        return self.find_element(locator).get_attribute(attr)

    def is_element_display(self, locator):
        try:
            self.wait.until(EC.visibility_of(self.find_element(locator)))
            return True
        except:
            return False
        
    def is_sceleton_display(self):
        return self.is_element_display("//div[contains(@class, 'skeleton-loader')]")

    def click(self, locator):
        self.scroll_to_element(locator)
        self.is_element_display(locator)
        self.find_element(locator).click()

    def scroll_to_element(self, locator):
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(self.find_element(locator)).perform()
        except:
            print("Элемент не найден")

    def get_elements_count(self, locator):
        list(self.driver.find_elements(By.XPATH, locator))
        return len(list)

    def get_text(self, locator):
        value = ""
        try:
            return self.find_element(locator).get_text()
        except:
            print("Элемент не найден")
        return value

    def wait_for_any_element_not_display(self, locator):
        locator_tuple = ("xpath", locator)
        try:
            self.wait.until(EC.invisibility_of_element_located(locator_tuple)).is_displayed()
        except:
            print("Ошибка. Элемент отображается!")

    def wait_for_loader_not_display(self):
        locator_loader = ("xpath", "//div[@role = 'progressbar']")
        self.wait.until_not(EC.presence_of_element_located(locator_loader))

    def wait_for_sceleton_not_dislpay(self):
        locator_sceleton = ("xpath", "//div[contains(@class, 'skeleton-loader')]")
        self.wait.until_not(EC.presence_of_element_located(locator_sceleton))

    def wait_for_table_loader_not_display(self):
        locator_table_loader = ("xpath", "//tr[@class = 'v-data-table__empty-wrapper']")
        self.wait.until_not(EC.presence_of_element_located(locator_table_loader))
