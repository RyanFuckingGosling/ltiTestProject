#Переход в ЛК (Ссылка в меню слева)
from pages.navigation_page import NavigationPage
from pages.login_page import LoginPage
from data.user_data import Data

def step_1(browser):
    navigation_page = NavigationPage(browser)
    login_page = LoginPage(browser)
    login_page.local_autorization()
    navigation_page.click_tab("Личный кабинет")

    assert navigation_page.url_is_open(Data.HOST + "lk")