#Отображение скелетона на главной странице
from pages.main_page import MainPage
from pages.login_page import LoginPage

def step_1(browser):
    login_page = LoginPage(browser)
    main_page = MainPage(browser)
    login_page.local_autorization()

    assert main_page.is_sceleton_display()
