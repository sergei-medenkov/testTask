from html_object_list import Pages, PageObjects, tests_dir
from conftest import step_name
import pytest
import allure
from time import sleep


@pytest.mark.first
@allure.title('Login Netflix')
class TestLoginNetflix:

    @pytest.mark.parametrize("test_params", [
        {
            "email": "test148968984@gmail.com",
            "password": "PSw12!64",
            "plan": "Basic",
            "name": "John",
            "lastname": "Malkovich",
            "card number": "124412462724",
            "expiration": "03/25",
            "security code": "333"
        },
        {
            "email": "test24544544@gmail.com",
            "password": "PSw1t53",
            "plan": "Premium",
            "name": "John",
            "lastname": "Malkovich",
            "card number": "124412462724",
            "expiration": "03/25",
            "security code": "333"
        },
        {
            "email": "test348948984@gmail.com",
            "password": "PSwg4535",
            "plan": "Basic",
            "name": "John",
            "lastname": "Malkovich",
            "card number": "124412462724",
            "expiration": "03/25",
            "security code": "333"
        },
    ])
    def test_login_netflix(self, login_netflix_fixture, test_params, **optional):
        params_changed = test_params
        if "lastname" in optional:
            params_changed = optional["lastname"]

        login_netflix_fixture(params_changed)

    @pytest.fixture()
    def login_netflix_fixture(self, driver, clicker, inputer, pay_with_card):
        def __login_netflix_fixture(test_params):
            with step_name("Delete cookies"):
                driver.delete_all_cookies()

            with step_name("Open Netflix main page"):
                driver.get(Pages.netflix_main_page)

            with step_name("Click accept cookies button"):
                clicker(PageObjects.accept_cookies_button)

            with step_name("Click email or phone field"):
                clicker(PageObjects.main_page_email_or_phone_field)

            with step_name("Insert email"):
                inputer(test_params["email"])

            with step_name("Click get started button"):
                clicker(PageObjects.main_page_get_started_button)

            with step_name("Click password field"):
                clicker(PageObjects.reg_page_password_field)

            with step_name("Insert password"):
                inputer(test_params["password"])

            with step_name("Click Next button"):
                clicker(PageObjects.reg_page_next_button)

            with step_name("Click Next button on Choose plan window"):
                clicker(PageObjects.reg_page_choose_plan_next_button)

            with step_name("Click plan button to choose plan"):
                clicker(PageObjects.choose_plan_page_plan_buttons[test_params["plan"]])
                sleep(1)

            with step_name("Click Next button on after plan choosing page"):
                clicker(PageObjects.choose_plan_page_next_button)

            with step_name("Call pay with card function"):
                pay_with_card(test_params)

        return __login_netflix_fixture

    @pytest.fixture()
    def pay_with_card(self, driver, clicker, inputer):
        def __pay_with_card(test_params):
            with step_name("Click credit card button"):
                clicker(PageObjects.payment_page_credit_card_button)

            with step_name("Click name field"):
                clicker(PageObjects.setup_credit_card_page_name_field)

            with step_name("Input name"):
                inputer(test_params["name"])

            with step_name("Click lastname field"):
                clicker(PageObjects.setup_credit_card_page_lastname_field)

            with step_name("Input lastname"):
                inputer(test_params["lastname"])

            with step_name("Click card number field"):
                clicker(PageObjects.setup_credit_card_page_card_number_field)

            with step_name("Input card number"):
                inputer(test_params["card number"])

            with step_name("Click expiration field"):
                clicker(PageObjects.setup_credit_card_page_expiration_name_field)

            with step_name("Input expiration"):
                inputer(test_params["expiration"])

            with step_name("Click field"):
                clicker(PageObjects.setup_credit_card_page_security_code_field)

            with step_name("Input security code"):
                inputer(test_params["security code"])

        return __pay_with_card

