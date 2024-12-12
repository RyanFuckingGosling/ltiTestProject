from pages.navigation_page import NavigationPage
from pages.personal_account_page import PersonalAccount
from pages.login_page import LoginPage

def step_1(browser):
    login_page = LoginPage(browser)
    navigation_page = NavigationPage(browser)
    personal_account = PersonalAccount(browser)
    login_page.local_autorization()
    navigation_page.click_profile_button()
    navigation_page.wait_for_sceleton_not_dislpay()

    assert personal_account.is_display_broker_allert_with_text("Реквизиты брокера будут доступны после предоставления " +
                                                               "согласия на обработку персональных данных.")