#Валидация полей главной страницы
from pages.navigation_page import NavigationPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


def step_1(browser):
    login_page = LoginPage(browser)
    main_page = MainPage(browser)
    navigation_page = NavigationPage(browser)
    login_page.local_autorization()

    assert not navigation_page.is_block_clicable("Программа долгосрочного партнерства")
    assert navigation_page.is_block_clicable("Мои программы")
    assert main_page.is_display_news_block()

def step_2(browser):
    main_page = MainPage(browser)

    assert main_page.is_display_title("Долгосрочное партнерство")

def step_3(browser):
    navigation_page = NavigationPage(browser)
    navigation_page.click_menu_button()

    assert not navigation_page.is_navigation_menu_open()
