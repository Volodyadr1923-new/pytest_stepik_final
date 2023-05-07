from .pages.main_page import MainPage
import time

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    time.sleep(3)
    #page.go_to_login_page()         # выполняем метод страницы — переходим на страницу логина
    page.should_be_login_link()      # метод, который будет проверять наличие ссылки
# class MainPage():
#
#     def test_guest_can_go_to_login_page(browser):
#         link = "http://selenium1py.pythonanywhere.com/"
#         browser.get(link)
#         time.sleep(3)
#         browser.implicitly_wait(1)
#
#         login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#         login_link.click()
#
#     def test_button_test_for_different_site_languages(browser):
#         link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#         browser.get(link)
#         time.sleep(3)
#         browser.implicitly_wait(1)
#         enter = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
#         assert len(enter) != 0, "The button is missing from the page!"