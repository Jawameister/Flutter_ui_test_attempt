from appium.webdriver.common.touch_action import TouchAction
import time
from selenium.common.exceptions import NoSuchElementException
from faker import Faker
from tests.conftest import appium_driver
from tests.click_func import click_element, swipe

from tests.test_autopayments.buttons_autopayments import button_continue

otp = '958536'
fake = Faker()

class Test_payments:
    def test_payments(self, appium_driver):
        driver = appium_driver
        swipe(driver, 516, 1485, 516, 700)
        click_element(driver, "//*[@content-desc='Оплата']")
        time.sleep(1)
        swipe(driver, 516, 1485, 516, 700)
        click_element(driver, "//*[@content-desc='Интернет']")
        click_element(driver, "//*[@content-desc='Gals Telecom']")
        time.sleep(1)
        login_input = driver.find_element('xpath', "//android.view.View[4]/android.view.View/android.view.View/android.widget.EditText")
        # amount_input = driver.find_element('xpath', "//android.view.View[4]/android.view.View/android.view.View/android.view.View/android.widget.EditText")
        login_input.send_keys('b-2-38-30-ucu')
        click_element(driver, "//*[@content-desc='1200']").click()
        # amount_input.click()
        time.sleep(1)
        # amount_input.send_keys('1000')
        click_element(driver, "//*[@content-desc='Gals Telecom']")
        click_element(driver, button_continue)
        click_element(driver, "//*[@content-desc='Оплатить']")
        try:
            otp_input = driver.find_element('xpath', "//android.widget.EditText")
            otp_input.click()
            otp_input.send_keys(otp)
        except NoSuchElementException:
            pass
        click_element(driver, "(//*[contains(@content-desc, \'Подробнее о платеже\')]")
        try:
            assert driver.find_element('xpath', "(//*[contains(@content-desc, \'Баланс\')]")
        except NoSuchElementException:
            pass
        screen_size = driver.get_window_size()
        screen_width = screen_size["width"]
        screen_height = screen_size["height"]
        # Координаты центра экрана
        center_x = screen_width // 2
        center_y = screen_height // 2
        # Выполнение тапа на пустое место
        action = TouchAction(driver)
        action.tap(x=center_x, y=center_y).perform()
        click_element(driver, "//*[@content-desc='На главную']")

