#02.Добавление брокерского счета
from pages.list_of_employees_page import ListOfEmployees
from pages.elements_pages.dropdown_page import DropdownPage
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.personal_account_page import PersonalAccount
from pages.elements_pages.fields_page import FieldsPage
from data.user_data import Data

def step_1(browser):
    dropdown_page = DropdownPage(browser)
    fields_page = FieldsPage(browser)
    list_of_employees = ListOfEmployees(browser)
    login_page = LoginPage(browser)
    navigation_page = NavigationPage(browser)
    login_page.local_autorization()
    navigation_page.click_tab("Администрирование")
    fields_page.wait_for_table_loader_not_display()
    fields_page.send_keys_to_field("Поиск", Data.LOGIN)
    fields_page.wait_for_table_loader_not_display()
    list_of_employees.click_edit_button_for_employee(Data.LOGIN)
    list_of_employees.wait_for_sceleton_not_dislpay()
    
    assert dropdown_page.is_dropdown_display("Наименование брокера*")
    assert fields_page.is_field_display("Брокерский счет/Счет депо*")

def step_2(browser):
    dropdown_page = DropdownPage(browser)
    dropdown_page.select_value_in_dropdown("Наименование брокера*", "Альфа-Инвестиции")

    assert dropdown_page.is_display_value_in_dropdown("Наименование брокера*", "Альфа-Инвестиции")

def step_3(browser):
    fields_page = FieldsPage(browser)
    list_of_employees = ListOfEmployees(browser)
    fields_page.send_keys_to_field("Брокерский счет/Счет депо*", "1234567890")
    list_of_employees.click_save_button_for_broker()

    assert list_of_employees.is_allert_with_text_display("Успешно", "Данные успешно сохранены")

def step_4(browser):
    navigation_page = NavigationPage(browser)
    personal_account = PersonalAccount(browser)
    navigation_page.click_tab("Личный кабинет")
    navigation_page.wait_for_sceleton_not_dislpay()

    assert personal_account.is_display_broker_allert_with_text("Реквизиты брокера будут доступны после предоставления " +
                                                               "согласия на обработку персональных данных.")