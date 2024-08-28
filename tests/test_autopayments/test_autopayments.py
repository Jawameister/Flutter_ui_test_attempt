from tests.conftest import appium_driver
from appium.webdriver.common.touch_action import TouchAction
import time
import logging
from faker import Faker
from selenium.webdriver.common.by import By
from tests.click_func import click_element, swipe
from .buttons_autopayments import apply, date_picker_period, \
    date_picker_time, date_picker_month, date_picker_week, date_picker_date,\
    button_continue, button_save, edit_button
from selenium.common.exceptions import NoSuchElementException
from shareable_functions import enter_pin, enter_otp, enter_login, burger_menu



otp = '958536'
fake = Faker()
logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Test_Autopayments:
    def test_autopayments_add(self, appium_driver):
        driver = appium_driver
        action = TouchAction(driver)
        action.long_press(x=516, y=1485).move_to(x=516, y=700).release().perform()
        autopays_widget = "//*[@content-desc='Автоплатежи']"
        click_element(driver, autopays_widget)
        click_element(driver, "//android.widget.Button[@content-desc='Добавить платёж']")
        click_element(driver, "//*[@content-desc='Интернет']")
        click_element(driver, "//*[@content-desc='Gals Telecom']")
        time.sleep(2)
        login_input = driver.find_element('xpath', "//android.widget.EditText[1]")
        amount_input = driver.find_element('xpath', "//android.widget.EditText[2]")
        login_input.send_keys('b-2-38-30-ucu')
        amount_input.click()
        amount_input.send_keys('1000')
        click_element(driver, "//*[@content-desc='Gals Telecom']")
        click_element(driver, "//*[@content-desc='Далее']")
        auto_name = driver.find_element(By.CLASS_NAME, "android.widget.EditText")
        auto_name.click()
        random_word = fake.word()
        auto_name.send_keys(random_word)
        screen_size = driver.get_window_size()
        screen_width = screen_size["width"]
        screen_height = screen_size["height"]
        # Координаты центра экрана
        center_x = screen_width // 2
        center_y = screen_height // 2
        # Выполнение тапа на пустое место
        action = TouchAction(driver)
        action.tap(x=center_x, y=center_y).perform()
        click_element(driver, date_picker_date)
        click_element(driver, apply)
        click_element(driver, date_picker_time)
        swipe(driver, 812, 1843, 812, 1439)
        # action = TouchAction(driver)
        # action.long_press(x=812, y=1843).move_to(x=812, y=1439).release().perform()
        time.sleep(3)
        click_element(driver, apply)
        click_element(driver, date_picker_period)
        swipe(driver, 812, 1843, 812, 1500)
        # action = TouchAction(driver)
        # action.long_press(x=812, y=1843).move_to(x=812, y=1500).release().perform()
        time.sleep(3)
        click_element(driver, apply)
        click_element(driver, date_picker_week)
        click_element(driver, date_picker_month)
        assert not driver.find_element('xpath', "//*[@content-desc='Сохранить']").is_enabled(), "Кнопка активна"
        click_element(driver, date_picker_week)
        click_element(driver, date_picker_date)

        click_element(driver, "//*[@content-desc='Воскресенье']")

        click_element(driver, date_picker_time)

        click_element(driver, apply)

        click_element(driver, button_save)
        enter_otp(driver)

        time.sleep(0.5)
        click_element(driver, button_continue)
        logging.info("All assertions passed and autopayment added successfully!")
    def test_autopayments_edit(self, appium_driver):
        driver = appium_driver
        try:
            driver.find_element('xpath', '(//*[contains(@content-desc, \'сум\')][1])').click()
        except NoSuchElementException:
            driver.find_element('xpath', '(//*[contains(@content-desc, \'сум\')])').click()
        click_element(driver, edit_button)
        click_element(driver, date_picker_month)
        click_element(driver, date_picker_week)
        click_element(driver, date_picker_date)
        click_element(driver, "//*[@content-desc='Понедельник']")
        driver.find_element('xpath', "//*[@content-desc='Время оплаты']").click()
        time.sleep(2)
        action = TouchAction(driver)
        action.long_press(x=812, y=1843).move_to(x=812, y=1500).release().perform()
        time.sleep(3)
        click_element(driver, apply)
        click_element(driver, date_picker_month)
        # assert driver.find_element('xpath', "//*[@content-desc='Сохранить']").is_displayed(), "Кнопка активна"
        click_element(driver, date_picker_week)
        click_element(driver, date_picker_date)
        time.sleep(2)
        driver.find_element('xpath', "//*[@content-desc='Воскресенье']").click()
        click_element(driver, date_picker_time)
        time.sleep(2)
        action = TouchAction(driver)
        action.long_press(x=812, y=1843).move_to(x=812, y=1500).release().perform()
        time.sleep(3)
        click_element(driver, apply)
        click_element(driver, button_save)
        enter_otp(driver)
        click_element(driver, button_continue)

        logging.info("Autopayment edited successfully")


    def test_autopayments_add_favorites(self, appium_driver):
        driver = appium_driver
        # click_element(driver, "//*[@content-desc='Автоплатежи']")
        click_element(driver, "//android.widget.Button[@content-desc='Добавить платёж']")
        click_element(driver, "//*[@content-desc='Из избранных']")
        click_element(driver, "//android.widget.Button[@content-desc='Добавить']")
        click_element(driver, date_picker_week)
        click_element(driver, date_picker_date)
        click_element(driver, "//*[@content-desc='Понедельник']")
        driver.find_element('xpath', "//*[@content-desc='Время оплаты']").click()
        time.sleep(2)
        action = TouchAction(driver)
        action.long_press(x=812, y=1843).move_to(x=812, y=1500).release().perform()
        time.sleep(3)
        click_element(driver, apply)
        click_element(driver, date_picker_month)
        assert driver.find_element('xpath', "//*[@content-desc='Сохранить']").is_displayed(), "Кнопка активна"
        click_element(driver, date_picker_week)
        click_element(driver, date_picker_date)
        time.sleep(2)
        driver.find_element('xpath', "//*[@content-desc='Воскресенье']").click()
        click_element(driver, date_picker_time)
        time.sleep(2)
        action = TouchAction(driver)
        action.long_press(x=812, y=1843).move_to(x=812, y=1500).release().perform()
        click_element(driver, apply)
        click_element(driver, button_save)
        enter_otp(driver)
        click_element(driver, button_continue)

        logging.info("Autopayment added from favorites successfully")

    def test_autopayments_delete(self, appium_driver):
        driver = appium_driver
        # click_element(driver, "//*[@content-desc='Автоплатежи']")
        # time.sleep(1.5)
        # click_element(driver, "//*[contains(@content-desc, 'Активный') or contains(@content-desc, 'На паузе')][1]/android.widget.Switch")
        try:
            click_element(driver, '(//*[contains(@content-desc, \'сум\')][1])')
        except NoSuchElementException:
            click_element(driver, '(//*[contains(@content-desc, \'сум\')])')
        click_element(driver, "//*[@content-desc, 'Активный']/android.widget.Switch")
        click_element(driver, "//*[@content-desc='Удалить']")
        click_element(driver, "//*[@content-desc='Нет']")
        click_element(driver, "//*[@content-desc='Удалить']")
        click_element(driver, "//*[@content-desc='Да']")
        click_element(driver, "//*[@content-desc='Продолжить']")
        logging.info("Autopayment deleted successfully")


    def test_set_autopay_favorites(self, appium_driver):
        driver = appium_driver
        driver.back()
        action = TouchAction(driver)
        action.press(x=812, y=1843).move_to(x=812, y=1439).release().perform()
        click_element(driver, "//*[@content-desc='Избранные']")
        click_element(driver, "(//*[contains(@content-desc, \'b-2-38-30-ucu\')]/android.widget.Button)")
        click_element(driver, "//*[@content-desc='Настроить автоплатеж']")
        click_element(driver, date_picker_date)
        click_element(driver, apply)
        click_element(driver, date_picker_time)
        click_element(driver, apply)
        date_picker_period = "//*[@content-desc='Интервал']"
        click_element(driver, date_picker_period)
        click_element(driver, apply)
        click_element(driver, date_picker_week)
        click_element(driver, date_picker_month)
        assert driver.find_element('xpath', "//*[@content-desc='Сохранить']").is_displayed(), "Кнопка активна"
        click_element(driver, date_picker_week)
        click_element(driver, date_picker_date)
        click_element(driver, "//*[@content-desc='Воскресенье']")
        click_element(driver, date_picker_time)
        click_element(driver, apply)
        click_element(driver, button_save)
        enter_otp(driver)
        click_element(driver, button_continue)
        logging.info("Autopayment set from favorites successfully")


