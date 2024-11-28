#Переход в ЛК (Ссылка в меню слева)
from pages.navigation_page import NavigationPage

def step_1(browser):
    navigation_page = NavigationPage(browser)
    navigation_page.local_autorization()
    navigation_page.click_tab("Личный кабинет")

    assert navigation_page.url_is_open("https://stage-lti.softline.com/lk")