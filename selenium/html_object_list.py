import os

tests_dir = os.path.dirname(__file__)


class Pages:
    netflix_main_page = "https://www.netflix.com/"


class PageObjects:
    accept_cookies_button = '[data-uia="cookie-disclosure-button-accept"]'

    main_page_email_or_phone_field = '[data-uia="field-email"]'
    main_page_get_started_button = '[data-uia="our-story-cta-hero_fuji"]'

    reg_page_password_field = '[data-uia="field-password"]'
    reg_page_next_button = '[data-uia="cta-registration"]'
    reg_page_choose_plan_next_button = '[data-uia="continue-button"]'

    choose_plan_page_next_button = '[data-uia="cta-plan-selection"]'
    choose_plan_page_plan_buttons = {
        "Basic": '[data-uia="plan-grid-plan-selector+input-text_1_stream_name"]',
        "Standard": '[data-uia="plan-grid-plan-selector+label-text_2_stream_name"]',
        "Premium": '[data-uia="plan-grid-plan-selector+input-text_4_stream_name"]'}

    payment_page_credit_card_button = '[data-uia="payment-choice+creditOrDebitOption"]'

    setup_credit_card_page_fields = {
        "name": '[data-uia="field-firstName+container"]',
        "lastname": '[data-uia="field-lastName"]',
        "card number": '[data-uia="field-creditCardNumber"]',
        "expiration date": '[data-uia="field-creditCardNumber"]',
        "security code": '[data-uia="field-creditCardSecurityCode"]'
                                    }

    setup_credit_card_page_checkboxes = {
        "DoNotEmail": "something"
    }
