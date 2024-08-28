
from tests.conftest import appium_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from tests.click_func import click_element, swipe

class Test_packages:
    @pytest.mark.skip()
    def test_packages_403(self, appium_driver):
        driver = appium_driver
        click_element(driver, "(//*[@content-desc='Оплата'])[1]")
        click_element(driver, "//android.widget.ImageView[@content-desc='Пакеты Beeline']")
        click_element(driver, "//*[@content-desc='Купить за деньги']")
        swipe(driver, 123, 2600, 123, 500)
        click_element(driver, "//*[contains(@content-desc, '100 Mb')]")
        time.sleep(2)
        num_field = driver.find_element(By.CLASS_NAME, "android.widget.EditText")
        # num_field = driver.find_element('xpath', "//android.widget.EditText")
        num_field.click()
        num_field.send_keys("\ue003" * len(num_field.text))
        click_element(driver, f"//*[contains(@content-desc, 'Интернет-пакет Beeline')]")
        num_field = driver.find_element('xpath', "//android.widget.EditText")
        num_field.click()
        num_field.send_keys('900510350')
        click_element(driver, "//android.widget.Button[@content-desc='Оплатить']")
        wait_time = 30
        error = (By.XPATH,
                 "//android.view.View[@content-desc='На выбранный номер невозможно подключить данную услугу']/android.view.View/android.view.View[2]")
        try:
            element = WebDriverWait(driver, wait_time).until(
                EC.visibility_of_element_located(error)
            )
            # Элемент стал видимым, выполните assert
            assert element.is_displayed(), "Элемент не отображается на странице"
        except NoSuchElementException:
            assert False, "Элемент не найден"
        except TimeoutException:
            assert False, f"Элемент {error} не стал видимым после {wait_time} секунд ожидания"

    @pytest.mark.skip()
    def test_packages_ucell(self, appium_driver):
        driver = appium_driver
        click_element(driver, "(//*[@content-desc='Оплата'])[1]")
        click_element(driver, "//android.widget.ImageView[@content-desc='Пакеты Beeline']")
        click_element(driver, "//*[@content-desc='Купить за деньги']")
        swipe(driver, 123, 2600, 123, 500)
        time.sleep(2)
        click_element(driver, "//*[contains(@content-desc, '100 Mb')]")
        num_field = driver.find_element('xpath', "//android.widget.EditText")
        num_field.click()
        num_field.send_keys("\ue003" * len(num_field.text))
        click_element(driver, f"//*[contains(@content-desc, 'Интернет-пакет Beeline')]")
        num_field = driver.find_element('xpath', "//android.widget.EditText")
        num_field.click()
        num_field.send_keys('932104343')
        click_element(driver, "//android.widget.Button[@content-desc='Оплатить']")
        wait_time = 30
        error = (By.XPATH,
                 "//*[@content-desc='Введенный номер не является абонентом Beeline']//android.view.View[1]")
        try:
            element = WebDriverWait(driver, wait_time).until(
                EC.visibility_of_element_located(error)
            )
            # Элемент стал видимым, выполните assert
            assert element.is_displayed(), "Элемент не отображается на странице"
        except NoSuchElementException:
            assert False, "Элемент не найден"
        except TimeoutException:
            assert False, f"Элемент {error} не стал видимым после {wait_time} секунд ожидания"

    @pytest.mark.skip()
    def test_packages_buy(self, appium_driver):
        driver = appium_driver
        click_element(driver, "(//*[@content-desc='Оплата'])[1]")
        click_element(driver, "//android.widget.ImageView[@content-desc='Пакеты Beeline']")
        click_element(driver, "//*[@content-desc='Купить за деньги']")
        swipe(driver, 123, 2600, 123, 500)
        time.sleep(2)
        click_element(driver, "//*[contains(@content-desc, '100 Mb')]")
        num_field = driver.find_element('xpath', "//android.widget.EditText")
        num_field.click()
        num_field.send_keys("\ue003" * len(num_field.text))
        click_element(driver, f"//*[contains(@content-desc, 'Интернет-пакет Beeline')]")
        num_field = driver.find_element('xpath', "//android.widget.EditText")
        num_field.click()
        num_field.send_keys('900389507')
        click_element(driver, "//android.widget.Button[@content-desc='Оплатить']")
        click_element(driver, "//*[@content-desc='Детали операции']")
        click_element(driver, "//*[@content-desc='На главную']")
