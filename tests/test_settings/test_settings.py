from selenium.webdriver.support import expected_conditions as EC
from tests.conftest import appium_driver
from selenium.webdriver.support.ui import WebDriverWait
from tests.often_used_buttons import apply, button_continue
import time
from shareable_functions import enter_pin, enter_otp, burger_menu, enter_finger
from faker import Faker
import random
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from tests.click_func import click_element, swipe

password = [8,8,8,8]

class TestSettings:


    def test_biometrics(self, appium_driver):
        driver = appium_driver
        burger_menu(driver)
        click_element(driver, "//*[@content-desc='Настройки приложения']")
        click_element(driver, "//*[@content-desc='Безопасность']")
        enter_pin(driver)
        click_element(driver, "//*[@content-desc='Использование биометрии']/android.widget.Switch")
        driver.back()
        click_element(driver, "//*[@content-desc='Безопасность']")
        enter_finger(driver)
        click_element(driver, "//*[@content-desc='Использование биометрии']/android.widget.Switch")
        driver.back()
        enter_pin(driver)

    def test_logout_all_devices(self, appium_driver):
        driver = appium_driver
        click_element(driver, "//*[@content-desc='Безопасность']")
        enter_pin(driver)
        click_element(driver, "//*[@content-desc='Управление сессиями']")
        click_element(driver, "//*[@content-desc='Завершить все сеансы кроме текущего ']")
        click_element(driver, "//*[@content-desc='Да']")
        click_element(driver, button_continue)




















