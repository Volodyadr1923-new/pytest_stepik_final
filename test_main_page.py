from .pages.main_page import MainPage
import time

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    time.sleep(3)
    login_page = page.go_to_login_page()
    time.sleep(3)
    login_page.should_be_login_page()

# Плюсы такого подхода: (go_to_login_page(self) класса MainPage(BasePage) возвращает объект класса с текущим url)
#
# тест выглядит аккуратнее — не нужно инициализировать страницу в теле теста;
# явно возвращаем страницу — тип страницы ассоциирован с методом;
# не нужно каждый раз думать в разных тестах про инициализацию страницы — уменьшаем дублирование кода;
# минусы:
#
# если у нас копится большое количество страниц и переходов — образуется много перекрестных импортов;
# большая связность кода — при изменении логики придется менять возвращаемое значение;
# сложнее понимать код, так как страница инициализируется неявно;
# образуются циклические зависимости, что часто приводит к ошибкам.

from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page1(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    time.sleep(3)
    login_page.should_be_login_page()

# Плюсы: (go_to_login_page(self) класса MainPage(BasePage) НЕ возвращает объект класса с текущим url)
#
# меньше связность кода;
# меньше импортов, нет перекрестных импортов;
# больше гибкость;
# в тесте понятнее что происходит, т.к. явно инициализируем страницу.
# Минусы:
#
# появляется лишний шаг в тест-кейсе;
# каждый раз при написании теста нужно думать про корректные переходы;
# дублируется код.