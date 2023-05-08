from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    # заглушки для методов проверок
    def should_be_login_page(self):

        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес  помощью свойства driver.current_url
        # https://selenium-python.readthedocs.io/api.html#selenium.webdriver.remote.webdriver.WebDriver.current_url
        # https://stepik.org/lesson/36285/step/9?unit=162401
        #
        # конструкция 'Name' in s возвращает просто True или False, a find() возвращает индекс первого вхождения
        # подстроки в строку и -1, если подстрока не найдена. Обычно в автотестах достаточно использовать in,
        # потому что это более читабельный вариант
        #
        # проверка, что подстрока "login" есть в текущем url браузера
        assert "login" in self.browser.current_url, "Incorrect url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.L_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.R_FORM), "Register form is not presented"