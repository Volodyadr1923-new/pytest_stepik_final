from selenium.webdriver.common.by import By
import time

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    time.sleep(3)
    browser.implicitly_wait(1)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def test_button_test_for_different_site_languages(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(3)
    browser.implicitly_wait(1)
    enter = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(enter) != 0, "The button is missing from the page!"