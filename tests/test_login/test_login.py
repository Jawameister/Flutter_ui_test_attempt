from tests.test_login.conftest import appium_driver_login
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait
from tests.often_used_buttons import apply, button_continue
import time
from shareable_functions import enter_pin, enter_otp, enter_login, burger_menu
from faker import Faker
import random
from selenium.webdriver.common.by import By
from tests.click_func import click_element, swipe

password = [8,8,8,8]
new_password = [9, 9, 9, 9]


class Test_auth:
    def test_auth(self, appium_driver_login):
        driver = appium_driver_login
        enter_login(driver)
        enter_otp(driver)
        enter_pin(driver)
        time.sleep(2)
        burger_menu(driver)
        # click_element(driver, "//android.widget.ImageView[1]")
        time.sleep(1.5)
        phone_element = driver.find_element(By.XPATH,
                                            '//android.widget.ImageView[contains(@content-desc, "+998 90 033 84 37")]')

        # Получение текста из элемента
        actual_phone_number = phone_element.get_attribute("contentDescription")

        expected_phone_number = "+998 90 033 84 37"

        assert expected_phone_number in actual_phone_number, f"Expected phone text '{expected_phone_number}' not found in the element"
    def test_reset_pin(self, appium_driver_login):
        driver = appium_driver_login
        enter_login(driver)
        enter_otp(driver)
        click_element(driver, "//*[@content-desc='Забыли PIN-код?']")
        click_element(driver, "//android.view.View[@content-desc='Да']")
        time.sleep(1)
        enter_otp(driver)
        time.sleep(1)
        for l in range(2):
            enter_pin(driver)
        assert WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@content-desc, 'Новый PIN-код не должен совпадать с текущим')]//*")))
        time.sleep(2)
        for l in range(2):
            for p in new_password:
                click_element(driver, f"//android.view.View[@content-desc='{p}']")
            time.sleep(0.5)
        click_element(driver, "//*[@content-desc='Продолжить']")
        driver.implicitly_wait(0.1)
        for p in new_password:
            click_element(driver, f"//android.view.View[@content-desc='{p}']")
        click_element(driver, "//*[@content-desc='Нет']")
        click_element(driver, "//*[@content-desc='Пропустить']")
        time.sleep(0.5)
        burger_menu(driver)

        assert driver.find_element(By.XPATH,
                                            '//android.widget.ImageView[contains(@content-desc, "+998 90 033 84 37")]')

        click_element(driver, "//*[@content-desc='Настройки приложения']")
        click_element(driver, "//*[@content-desc='Безопасность']")
        driver.finger_print(1)
        for p in new_password:
            click_element(driver, f"//android.view.View[@content-desc='{p}']")
        click_element(driver, "//*[@content-desc='Сменить PIN-код']")
        for p in new_password:
            click_element(driver, f"//android.view.View[@content-desc='{p}']")
        time.sleep(0.5)
        for l in range(2):
            enter_pin(driver)
        time.sleep(0.5)
        click_element(driver, "//*[@content-desc='Продолжить']")
        enter_pin(driver)


    def test_pin_attempt_block(self, appium_driver_login):
        driver = appium_driver_login
        enter_login(driver)
        enter_otp(driver)
        for l in range(3):
            for p in random.sample(range(10), 4):
                driver.find_element('xpath', f"//android.view.View[@content-desc='{p}']").click()
            time.sleep(3)
        assert driver.find_element('xpath', "//*[contains(@content-desc, 'Пользователь временно заблокирован')]//*")


    def test_pin_attempt_otp_expired(self, appium_driver_login):
        driver = appium_driver_login
        enter_login(driver)
        enter_otp(driver)
        click_element(driver, "//*[@content-desc='Забыли PIN-код?']")
        click_element(driver, "//android.view.View[@content-desc='Да']")
        time.sleep(1)
        digit = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText")))
        WebDriverWait(driver, 65).until(EC.element_to_be_clickable((By.XPATH, "//*[@content-desc='Отправить заново']"))).click()
        digit.click()
        time.sleep(130)
        digit.send_keys(958536)
        assert driver.find_element('xpath', "//*[contains(@content-desc, 'Отп код просрочен запросите новую')]//*[2]")



    def test_public_agreement(self, appium_driver_login):
        """"
        Не работает, кнопка публичной оферты не кликабельна
        """

        driver = appium_driver_login
        click_element(driver, "//*[@content-desc='Русский']")
        # click_element(driver, "//*[contains(@content-desc, 'публичной оферты')]//*")
        # driver.find_elements(By.ID)
        click_element(driver, '//*[contains(@content-desc, "публичной оферты")]')












