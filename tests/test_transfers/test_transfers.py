from appium.webdriver.common.touch_action import TouchAction
import time
from selenium.common.exceptions import NoSuchElementException
from faker import Faker
from tests.click_func import click_element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.conftest import appium_driver
from tests.test_autopayments.buttons_autopayments import button_continue, button_save

otp = '958536'
fake = Faker()


class Test_transfers:
    def test_transfers_by_card_number(self, appium_driver):
        driver = appium_driver
        action = TouchAction(driver)
        action.long_press(x=516, y=1485).move_to(x=516, y=700).release().perform()
        click_element(driver, "//*[@content-desc='Перевести']")
        time.sleep(3)
        card_input = driver.find_element('xpath', "//android.widget.EditText")
        card_input.click()
        card_input.send_keys('9860020101778536')
        time.sleep(3)

        amount_input = driver.find_element('xpath', "//android.widget.EditText[1]")
        amount_input.click()
        amount_input.send_keys('1000')
        click_element(driver, "//*[@content-desc='Переводы']")
        comment_input = driver.find_element('xpath', "//android.widget.EditText[2]")
        comment = fake.word()
        comment_input.click()
        comment_input.send_keys(comment)
        click_element(driver, "//*[@content-desc='Переводы']")
        click_element(driver, button_continue)
        click_element(driver, "//*[@content-desc='Перевести средства']")
        try:
            otp_input = driver.find_element('xpath', "//android.widget.EditText")
            otp_input.click()
            otp_input.send_keys(otp)
        except NoSuchElementException:
            pass
        click_element(driver, "//*[@content-desc='Избранные']")
        time.sleep(0.5)
        name_input = driver.find_element('xpath', "//android.widget.EditText")
        name_input.click()
        name = fake.word()
        name_input.send_keys(name)
        click_element(driver, button_save)
        click_element(driver, button_continue)
        click_element(driver, "//*[@content-desc='На главную']")

    def test_transfers_by_phone_number(self, appium_driver):
        driver = appium_driver
        action = TouchAction(driver)
        action.long_press(x=516, y=1485).move_to(x=516, y=700).release().perform()
        click_element(driver, "//*[@content-desc='Перевести']")
        time.sleep(3)
        card_input = driver.find_element('xpath', "//android.widget.EditText")
        card_input.click()
        card_input.send_keys('998903541334')
        time.sleep(3)

        amount_input = driver.find_element('xpath', "//android.widget.EditText[1]")
        comment_input = driver.find_element('xpath', "//android.widget.EditText[2]")
        amount_input.send_keys('1000')

        comment_input.click()
        comment_input.send_keys('testtest')
        click_element(driver, "//*[@content-desc='Переводы']")
        click_element(driver, button_continue)
        click_element(driver, "//*[@content-desc='Перевести средства']")
        try:
            otp_input = driver.find_element('xpath', "//android.widget.EditText")
            otp_input.click()
            otp_input.send_keys(otp)
        except NoSuchElementException:
            pass
        click_element(driver, "//*[@content-desc='На главную']")

    def test_transfers_404(self, appium_driver):
        driver = appium_driver
        action = TouchAction(driver)
        action.long_press(x=516, y=1485).move_to(x=516, y=700).release().perform()
        click_element(driver, "//*[@content-desc='Перевести']")
        time.sleep(3)
        card_input = driver.find_element('xpath', "//android.widget.EditText")
        card_input.click()
        random_word = fake.random_number(digits=16)
        card_input.send_keys('9860020112345678')
        time.sleep(3)
        wait_time = 30
        error = (By.XPATH,
                 "//android.view.View[@content-desc='Карта получателя не найдена или не активна']")
        try:
            element = WebDriverWait(driver, wait_time).until(
                EC.visibility_of_element_located(error)
            )
            # Элемент стал видимым, выполните assert
            assert element.is_displayed(), "Элемент не отображается на странице"
        except NoSuchElementException:
            assert False, "Элемент не найден"


        click_element(driver, "//*[@content-desc='Переводы']")
        click_element(driver, "//*[@content-desc='Главная']")

    # def test_transfers_between_my_cards(self, appium_driver):
    #     driver = appium_driver
    #     click_element(driver, "//*[@content-desc='Перевести']")
    #     click_element(driver, "//*[@content-desc='Между моими картами']")
    def test_transfers_last_recepients(self, appium_driver):
        driver = appium_driver
        action = TouchAction(driver)
        action.long_press(x=516, y=1485).move_to(x=516, y=700).release().perform()
        click_element(driver, "//*[@content-desc='Перевести']")
        click_element(driver, "//*[@content-desc='Последние получатели']")
        click_element(driver, '(//*[contains(@content-desc, \'JAVOKHIR\')])')
        click_element(driver, "//*[@content-desc='Переводы']")
        amount_input = driver.find_element('xpath', "//android.widget.EditText[1]")
        comment_input = driver.find_element('xpath', "//android.widget.EditText[2]")
        amount_input.click()
        amount_input.send_keys('1000')
        comment = fake.word()
        comment_input.click()
        comment_input.send_keys(comment)
        click_element(driver, "//*[@content-desc='Переводы']")
        click_element(driver, button_continue)
        click_element(driver, "//*[@content-desc='Перевести средства']")
        try:
            otp_input = driver.find_element('xpath', "//android.widget.EditText")
            otp_input.click()
            otp_input.send_keys(otp)
        except NoSuchElementException:
            pass
        click_element(driver, "//*[@content-desc='На главную']")
    def test_transfers_add_favorites_widget(self, appium_driver):
        driver = appium_driver
        action = TouchAction(driver)
        action.long_press(x=516, y=1485).move_to(x=516, y=700).release().perform()
        click_element(driver, "//*[@content-desc='Перевести']")
        time.sleep(0.5)
        click_element(driver, "//*[@content-desc='Избранные']")
        click_element(driver, "//*[@content-desc='Добавить новый']")
        card_input = driver.find_element('xpath', "//android.widget.EditText[1]")
        fav_name = driver.find_element('xpath', "//android.widget.EditText[2]")
        amount_input = driver.find_element('xpath', "//android.widget.EditText[3]")
        card_input.click()
        card_input.send_keys('9860020101778536')
        fav_name.click()
        name = fake.word()
        fav_name.send_keys(name)
        click_element(driver, "//*[@content-desc='Создать избранный']")
        amount_input.click()
        amount_input.send_keys('1000')
        click_element(driver, "//*[@content-desc='Создать избранный']")
        click_element(driver, "//*[@content-desc='Добавить']")
        click_element(driver, button_continue)

        assert driver.find_element('xpath', f'(//*[contains(@content-desc, \'{name}\')])').is_displayed()
