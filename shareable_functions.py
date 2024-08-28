from tests.often_used_buttons import button_continue
from tests.test_login.conftest import appium_driver_login
from tests.click_func import swipe
from appium.webdriver.common.touch_action import TouchAction
import time
from faker import Faker
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from tests.click_func import click_element, swipe
from selenium.common.exceptions import NoSuchElementException


otp = '958536'
password = [8,8,8,8]
login = [9, 0, 0, 3, 3, 8, 4, 3, 7]

def enter_pin(driver):
    for p in password:
        try:
            driver.find_element('xpath', f"//android.view.View[@content-desc='{p}']").click()
            # WebDriverWait(driver, 5).until(
            #     EC.visibility_of_element_located((By.XPATH, f"//android.view.View[@content-desc='{p}']"))).click()
        except NoSuchElementException:
            pass
    try:
        driver.find_element('xpath', "//*[@content-desc='Нет']").click()
    except NoSuchElementException:
        pass

    try:
        driver.find_element('xpath', "//*[@content-desc='Пропустить']").click()
    except NoSuchElementException:
        pass
    print("enter_pin function completed successfully.")
    return 1

def enter_finger(driver):
    driver.finger_print(6666)


def enter_otp(driver):
    try:
        # driver.find_element('xpath', "//android.widget.EditText").send_keys(otp)
        digit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText")))
        digit.click()
        digit.send_keys(otp)
    except NoSuchElementException:
        pass

    return None
def enter_login(driver):
    click_element(driver, "//*[@content-desc='Русский']")
    assert not driver.find_element(By.XPATH, '//*[@content-desc="Продолжить"]').is_enabled()
    for i in login:
        driver.find_element('xpath', f"//android.view.View[@content-desc='{i}']").click()
    click_element(driver, button_continue)
    time.sleep(1)

    return None

def burger_menu(driver):
    click_element(driver, "//*[@content-desc='Еще']")
    click_element(driver, "//*[@content-desc='Настройки']")