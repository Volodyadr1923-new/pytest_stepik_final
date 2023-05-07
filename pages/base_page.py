from selenium.common.exceptions import NoSuchElementException
# Создадим базовый класс
class BasePage():
    # конструктор — метод, который вызывается, когда мы создаем объект
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    # откроет нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)
    # реализуем метод is_element_present, в котором будем перехватывать исключение
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True