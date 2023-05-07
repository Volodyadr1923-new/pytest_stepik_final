# Создадим базовый класс
class BasePage():
    # конструктор — метод, который вызывается, когда мы создаем объект
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    # откроет нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)