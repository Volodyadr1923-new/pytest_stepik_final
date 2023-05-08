# обект класса будет соответствовать каждому объету класса PageObject:
from selenium.webdriver.common.by import By

# Определяет кнопку регистрации на странице
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

# теперь каждый селектор — это пара: как искать и что искать.

# Определяет наличие форм регистрации и формы для входа (точнее пару как искать и что искать)
class LoginPageLocators():
    R_FORM = (By.CSS_SELECTOR, "#register_form")
    L_FORM = (By.CSS_SELECTOR, "#login_form")
