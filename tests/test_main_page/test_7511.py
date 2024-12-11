#Переключение на компактный вид меню
from pages.navigation_page import NavigationPage
from pages.login_page import LoginPage

def step_1(browser):
    login_page = LoginPage(browser)
    navigation_page = NavigationPage(browser)
    login_page.local_autorization()

    assert navigation_page.is_navigation_menu_open()

def step_2(browser):
    navigation_page = NavigationPage(browser)
    navigation_page.click_menu_button()

    assert not navigation_page.is_navigation_menu_open()

def step_3(browser):
    navigation_page = NavigationPage(browser)
    navigation_page.click_tab("Личный кабинет")

    assert navigation_page.url_is_open("https://stage-lti.softline.com/lk")

def step_4(browser):
    navigation_page = NavigationPage(browser)
    navigation_page.click_menu_button()

    assert navigation_page.is_navigation_menu_open()