#Переход в ЛК (Ссылка на главном экране)
from pages.main_page import MainPage

def step_1(browser):
    main_page = MainPage(browser)
    main_page.local_autorization()
    main_page.click_block_with_name("Мои программы")

    assert main_page.url_is_open("https://stage-lti.softline.com/lk")
