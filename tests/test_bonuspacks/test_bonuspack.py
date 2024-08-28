import pytest
from tests.conftest import appium_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from tests.click_func import click_element


class Test_bonuspack:


    @pytest.mark.skip()
    def test_bonuspack_403(self, appium_driver):
        driver = appium_driver
        click_element(driver, "//*[contains(@content-desc, 'Обменять')]")
        click_element(driver, "//*[contains(@content-desc, '250 МБ')]")
        num_field= driver.find_element('xpath', "//android.widget.EditText")
        num_field.click()
        num_field.send_keys("\ue003" * len(num_field.text))
        click_element(driver, f"//*[contains(@content-desc, 'Мой баланс')]")
        num_field = driver.find_element('xpath', "//android.widget.EditText")
        num_field.click()
        num_field.send_keys('900510350')
        click_element(driver, "//android.widget.Button[@content-desc='Обменять']")
        wait_time = 30
        error = (By.XPATH, "//android.view.View[@content-desc='На выбранный номер невозможно подключить данную услугу']/android.view.View/android.view.View[2]")
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
    def test_bonuspack_ucell(self, appium_driver):
        driver = appium_driver
        num_field = driver.find_element('xpath', "//android.widget.EditText")
        num_field.click()
        num_field.send_keys("\ue003" * len(num_field.text))
        click_element(driver, f"//*[contains(@content-desc, 'Мой баланс')]")
        num_field = driver.find_element('xpath', "//android.widget.EditText")
        num_field.click()
        num_field.send_keys('942104343')
        click_element(driver, "//android.widget.Button[@content-desc='Обменять']")
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
    def test_bonuspack_buy(self, appium_driver):
        driver = appium_driver
        num_field = driver.find_element('xpath', "//android.widget.EditText")
        num_field.click()
        num_field.send_keys("\ue003" * len(num_field.text))
        click_element(driver, f"//*[contains(@content-desc, 'Мой баланс')]")
        num_field = driver.find_element('xpath', "//android.widget.EditText")
        num_field.click()
        num_field.send_keys('900389507')
        click_element(driver, "//*[@content-desc='Обменять']")
        click_element(driver, "//*[@content-desc='Детали операции']")
        click_element(driver, "//*[@content-desc='На главную']")



