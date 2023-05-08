from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    # # передаём не экземпляр браузера, а экземпляр класса
    def go_to_login_page(self):
        # Обратите внимание! При создании объекта мы обязательно передаем ему тот же самый объект
        # драйвера для работы с браузером, а в качестве url передаем текущий адрес.
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # возвращает объект класса с текущим url адресом страницы, для которого отработает конструктор
        # __init__(browser=self.browser, url=self.browser.current_url, timeout=10)
        return LoginPage(browser=self.browser, url=self.browser.current_url)