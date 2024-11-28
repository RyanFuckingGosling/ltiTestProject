#01.Проверка данных ЛК пользователя перед заполнением брокерского счета
from pages.personal_account_page import PersonalAccount
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
import pytest

def step_1(browser):
    login_page = LoginPage(browser)
    navigation_page = NavigationPage(browser)
    personal_account = PersonalAccount(browser)
    login_page.local_autorization()
    navigation_page.click_profile_button()
    personal_account.wait_for_sceleton_not_dislpay()

    assert personal_account.url_is_open("https://stage-lti.softline.com/lk")
    assert personal_account.is_display_value_in_field("ФИО:")
    assert personal_account.is_display_value_in_field("Email:")
    assert personal_account.is_display_value_in_field("Подразделение:")
    assert personal_account.is_display_value_in_field("Стаж:")
    assert not personal_account.is_display_value_in_field("Брокер:")
    assert not personal_account.is_display_value_in_field("Счет:")
    assert not personal_account.is_display_value_in_field("ЛК Брокера:")
    assert personal_account.is_display_broker_allert_with_text("Реквизиты брокера будут доступны после " +
                                                               "предоставления согласия на обработку персональных данных.")
    assert personal_account.is_display_create_button_in_field("Согласие на обработку персональных данных")