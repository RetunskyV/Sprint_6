class OrderPageLocators:
    NAME_INPUT = "//*[@id='root']/div/div[2]/div[2]/div[1]/input"
    SURNAME_INPUT = "//*[@id='root']/div/div[2]/div[2]/div[2]/input"
    ADDRESS_INPUT = "//*[@id='root']/div/div[2]/div[2]/div[3]/input"
    METRO_INPUT = "/html/body/div/div/div[2]/div[2]/div[4]/div/div[1]/input"
    METRO_OPTION_TEMPLATE = "/html/body/div/div/div[2]/div[2]/div[4]/div/div[2]/ul/li[{index}]/button"
    PHONE_INPUT = "//*[@id='root']/div/div[2]/div[2]/div[5]/input"
    NEXT_BUTTON = "//*[@id='root']/div/div[2]/div[3]/button"

    DATE_INPUT = "/html/body/div/div/div[2]/div[2]/div[1]/div[1]/div/input"
    RENTAL_PERIOD_DROPDOWN = "//*[@id='root']/div/div[2]/div[2]/div[2]/div[1]/div[2]/span"
    RENTAL_PERIOD_OPTION_TEMPLATE = "//*[@id='root']/div/div[2]/div[2]/div[2]/div[2]/div[{index}]"
    COLOR_TEMPLATE = "//*[@id='{color}']"
    COMMENT_INPUT = "//*[@id='root']/div/div[2]/div[2]/div[4]/input"
    ORDER_BUTTON = "//*[@id='root']/div/div[2]/div[3]/button[2]"

    CONFIRM_BUTTON = "//*[@id='root']/div/div[2]/div[5]/div[2]/button[2]"
    SUCCESS_MODAL = "//*[@id='root']/div/div[2]/div[5]"