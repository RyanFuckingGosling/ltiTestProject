#Отображение скелетона на главной странице
from core.base_page import BasePage

def step_1(browser):
    base_page = BasePage(browser)
    base_page.local_autorization()
    base_page.open_host()

    assert base_page.is_sceleton_display()

    #Не понимаю почему не ловит скелетон