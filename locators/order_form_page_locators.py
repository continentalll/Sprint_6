from selenium.webdriver.common.by import By


class TestOrderFormPageLocators:

    FIRST_NAME_FIELD = By.XPATH, "//input[@placeholder='* Имя']"

    LAST_NAME_FIELD = By.XPATH, "//input[@placeholder='* Фамилия']"

    ADDRESS_FIELD = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"

    METRO_STATION_FIELD = By.XPATH, "//input[@placeholder='* Станция метро']"

    METRO_STATION_LIST = By.CLASS_NAME, 'select-search__select'

    SELECTED_STATION = (By.XPATH, ".//li[@class='select-search__row']")

    PHONE_NUMBER_FIELD = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"

    CONTINUE_BUTTON = By.XPATH, '//button[text()="Далее"]'

    TITLE_ABOUT_RENT_FORM = By.CLASS_NAME, 'Order_Header__BZXOb'

    RENTAL_DATE_FIELD = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"

    CALENDAR = By.CSS_SELECTOR, ".react-datepicker"

    RENTAL_DURATION_FIELD = By.CLASS_NAME, 'Dropdown-placeholder'

    TODAY_DATE_CALENDAR = By.CSS_SELECTOR, ".react-datepicker__day--today"

    TOMORROW_DATE_CALENDAR = (
        By.XPATH,
        "//div[contains(@class,'react-datepicker__day--today')]"
        "/following::div[contains(@class,'react-datepicker__day--')][1]"
    )

    RENTAL_DURATION_LIST = By.CLASS_NAME, 'Dropdown-menu'

    DROPDOWN_ITEM_RENTAL_PERIOD = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='трое суток']")

    RENTAL_DURATION_AFTER_INPUT = By.CLASS_NAME, 'Dropdown-placeholder is-selected'

    CHOOSE_COLOR_FIELD = By.XPATH, '//div[text()="Цвет самоката"]'

    CHECKBOX_GREY = By.ID, 'grey'

    COMMENT_FIELD = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'

    ORDER_BUTTON = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]'

    POP_UP_CONFIRM_ORDER = By.CLASS_NAME, 'Order_ModalHeader__3FDaJ'

    YES_BUTTON_POP_UP_CONFIRM_ORDER = By.XPATH, '//button[text()="Да"]'

    POP_UP_COMPLETE_ORDER = By.CLASS_NAME, 'Order_ModalHeader__3FDaJ'