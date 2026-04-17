class OrderPageLocators:
    NAME_INPUT = "//input[@placeholder='* Имя']"
    SURNAME_INPUT = "//input[@placeholder='* Фамилия']"
    ADDRESS_INPUT = "//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO_INPUT = "//input[@placeholder='* Станция метро']"
    METRO_OPTION_TEMPLATE = "//button[contains(@class, 'Order_SelectOption')]//div[contains(@class, 'Order_Text') and text()='{station}']"
    PHONE_INPUT = "//input[@placeholder='* Телефон: на него позвонит курьер']"
    NEXT_BUTTON = "//button[text()='Далее']"

    DATE_INPUT = "//input[@placeholder='* Когда привезти самокат']"
    RENTAL_PERIOD_DROPDOWN = "//div[text()='* Срок аренды']/following-sibling::div//span"
    RENTAL_PERIOD_OPTION_TEMPLATE = "//div[@class='Dropdown-option' and text()='{period}']"
    COLOR_TEMPLATE = "//label[contains(text(), '{color_text}')]"
    COMMENT_INPUT = "//input[@placeholder='Комментарий для курьера']"
    ORDER_BUTTON = "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']"

    CONFIRM_BUTTON = "//div[contains(@class, 'Order_Modal')]//button[text()='Да']"
    SUCCESS_MODAL = "//div[contains(@class, 'Order_Modal')]//div[text()='Заказ оформлен']"