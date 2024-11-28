import pytest
from core.base_page import BasePage
from pages.navigation_page import NavigationPage
from pages.elements_pages.fields_page import FieldsPage


def step_1(browser):
    base_page = BasePage(browser)
    navigation_page = NavigationPage(browser)
    fields_page = FieldsPage(browser)
    base_page.local_autorization()
    navigation_page.click_tab("Личный кабинет")
    navigation_page.select_section_from_tab("Программа долгосрочного партнерства", "Как это работает?")
    navigation_page.select_section_from_tab("Программа долгосрочного партнерства", "Калькулятор")
    fields_page.send_keys_to_field("Годовой фиксированный доход, руб", "10000")

    assert fields_page.is_display_field("Годовой фиксированный доход, руб"), "Что-то пошло не так"