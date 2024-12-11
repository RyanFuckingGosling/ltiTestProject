#Переход в ЛК (Ссылка на главном экране)
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data.user_data import Data

def step_1(browser):
    login_page = LoginPage(browser)
    main_page = MainPage(browser)
    login_page.local_autorization()
    main_page.click_block_with_name("Мои программы")

    assert main_page.url_is_open(Data.HOST + "lk")
