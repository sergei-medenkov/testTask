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
            "do not email": False,
            "optional": {
                "fields": {
                        "name": "John",
                        "lastname": "",
                        "card number": "124412462724",
                        "expiration": "03/25",
                        "security code": "333",
                            },
                "checkboxes": []
                         }
        },
        {
            "email": "test24544544@gmail.com",
            "password": "PSw1t53",
            "plan": "Premium",
            "do not email": False,
            "optional": {
                "fields": {
                    "name": "John",
                    "lastname": "Smith",
                    "card number": "124412462724",
                    "expiration": "03/25",
                    "security code": "333"
                            },
                "checkboxes": []
            }
        },
        {
            "email": "test348948984@gmail.com",
            "password": "PSwg4535",
            "plan": "Basic",
            "name": "John",
            "do not email": False,
            "optional": {
                "fields": {
                    "lastname": "Brown",
                    "card number": "124412462724",
                    "expiration": "03/25",
                    "security code": "333",
                    },
                "checkboxes": ["DoNotEmail"]
            }
        },
    ])
    def test_login_netflix(self, driver, clicker, inputer, pay_with_card, test_params):
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

    @pytest.fixture()
    def pay_with_card(self, driver, clicker, inputer):
        def __pay_with_card(test_params):
            with step_name("Click credit card button"):
                clicker(PageObjects.payment_page_credit_card_button)

            for field_name in test_params["optional"]["fields"]:
                with step_name(f"Click {field_name} field"):
                    clicker(PageObjects.setup_credit_card_page_fields[field_name])

                with step_name(f"Input {field_name}"):
                    inputer(test_params[field_name])

            for checkbox in test_params["optional"]["checkboxes"]:
                with step_name(f"Click {checkbox} field"):
                    clicker(PageObjects.setup_credit_card_page_checkboxes[checkbox])

        return __pay_with_card

