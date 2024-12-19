#Прикрепление согласия на обработку ПД
from pages.login_page import LoginPage
from pages.elements_pages.fields_page import FieldsPage
from pages.elements_pages.dropdown_page import DropdownPage
from pages.navigation_page import NavigationPage
from data.user_data import Data
from pages.list_of_employees_page import ListOfEmployees
from pages.elements_pages.modal_window_page import ModalWindow

def step_1(browser):
    login_page = LoginPage(browser)
    navigation_page = NavigationPage(browser)
    fields_page = FieldsPage(browser)
    list_of_employees = ListOfEmployees(browser)
    dropdown_page = DropdownPage(browser)
    login_page.local_autorization()
    navigation_page.click_tab("Администрирование")
    fields_page.set_value_in_field("Поиск", Data.LOGIN)
    list_of_employees.wait_for_table_loader_not_display()
    list_of_employees.click_edit_button_for_employee(Data.LOGIN)

    assert dropdown_page.is_dropdown_display("Наименование брокера*")
    assert dropdown_page.is_display_value_in_dropdown("Наименование брокера*", "Альфа-Инвестиции")
    assert fields_page.is_field_display("Брокерский счет/Счет депо*")

def step_2(browser):
    list_of_employees = ListOfEmployees(browser)
    modal_window = ModalWindow(browser)
    list_of_employees.click_button_with_text_in_field("Согласие на обработку персональных данных", "Прикрепить")

    assert modal_window.is_modal_window_display("Прикрепить документ")

def step_3(browser):
    fields_page = FieldsPage(browser)
    modal_window = ModalWindow(browser)
    list_of_employees = ListOfEmployees(browser)
    fields_page.set_file_in_field("Выберите файл*", "Согласие_на_обработку_персональных_данных.pdf")
    modal_window.click_button_in_modal_window("Сохранить")

    assert list_of_employees.is_allert_with_text_display("Успешно", "Данные успешно сохранены")
    