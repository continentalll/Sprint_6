from selenium.webdriver.common.by import By


class TestHomePageLocators:

    ORDER_BUTTON_HEADER = By.CLASS_NAME, 'Button_Button__ra12g'

    ORDER_BUTTON_BODY = By.CLASS_NAME, 'Button_Middle__1CSJM'

    HOW_IT_WORKS_BLOCK = By.XPATH, '//div[text()="Как это работает"]'

    ACCEPT_COOKIE_BUTTON = By.ID, 'rcc-confirm-button'

    ACCORDION_BUTTON_FAQ_1 = By.ID, 'accordion__heading-0'

    ANSWER_FAQ_1 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-0"]:not([hidden]) p'
    
    ACCORDION_BUTTON_FAQ_2 = By.ID, 'accordion__heading-1'

    ANSWER_FAQ_2 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-1"]:not([hidden]) p'

    ACCORDION_BUTTON_FAQ_3 = By.ID, 'accordion__heading-2'

    ANSWER_FAQ_3 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-2"]:not([hidden]) p'

    ACCORDION_BUTTON_FAQ_4 = By.ID, 'accordion__heading-3'

    ANSWER_FAQ_4 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-3"]:not([hidden]) p'

    ACCORDION_BUTTON_FAQ_5 = By.ID, 'accordion__heading-4'

    ANSWER_FAQ_5 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-4"]:not([hidden]) p'

    ACCORDION_BUTTON_FAQ_6 = By.ID, 'accordion__heading-5'

    ANSWER_FAQ_6 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-5"]:not([hidden]) p'

    ACCORDION_BUTTON_FAQ_7 = By.ID, 'accordion__heading-6'

    ANSWER_FAQ_7 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-6"]:not([hidden]) p'
    
    ACCORDION_BUTTON_FAQ_8 = By.ID, 'accordion__heading-7'

    ANSWER_FAQ_8 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-7"]:not([hidden]) p'

    LOGO_YANDEX = By.CLASS_NAME, "Header_LogoYandex__3TSOI"

    LOGO_SAMOKAT = By.CLASS_NAME, "Header_LogoScooter__3lsAR"