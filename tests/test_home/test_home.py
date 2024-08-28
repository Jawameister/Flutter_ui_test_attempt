from tests.conftest import appium_driver
from selenium.webdriver.common.by import By
from tests.often_used_buttons import apply, date_picker_time, date_picker_month, date_picker_week, date_picker_date, \
    otp
import time
from appium.webdriver.common.touch_action import TouchAction
from tests.often_used_buttons import button_continue, button_save
from selenium.common.exceptions import NoSuchElementException
from tests.click_func import click_element, swipe
from faker import Faker

fake = Faker()

class Test_home:
    def test_create_home_payment(self, appium_driver):
        driver = appium_driver
        swipe(driver, 516, 1485, 516, 700)

        click_element(driver, "//*[@content-desc='Мой дом']")
        click_element(driver, "//*[@content-desc='Добавить новый Дом']")
        time.sleep(1)
        try:
            home_name = driver.find_element('xpath', "//android.widget.EditText")
        except NoSuchElementException:
            home_name = driver.find_element(By.CLASS_NAME, "android.widget.EditText")
        home_name.click()
        home_name.send_keys('Dom_ui')
        click_element(driver, button_save)
        click_element(driver, "//*[contains(@content-desc, 'Dom_ui')]")
        time.sleep(1)
        # try:
        #     driver.find_element('xpath', "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]").click()
        # except NoSuchElementException:
        #     click_element(driver, "//*[@content-desc='Добавить платёж']")
        click_element(driver, "//*[@content-desc='Оплата']")
        click_element(driver, "//*[@content-desc='Интернет']")
        click_element(driver, "//*[@content-desc='Gals Telecom']")
        time.sleep(2)
        fav_name = driver.find_element('xpath', "//android.widget.EditText")
        fav_name.click()
        random_word = fake.word()
        fav_name.send_keys(random_word)
        screen_size = driver.get_window_size()
        screen_width = screen_size["width"]
        screen_height = screen_size["height"]
        # Координаты центра экрана
        center_x = screen_width // 2
        center_y = screen_height // 2
        # Выполнение тапа на пустое место
        action = TouchAction(driver)
        action.tap(x=center_x, y=center_y).perform()
        login_input = driver.find_element(By.XPATH, "(//*[@class='android.widget.EditText'])[2]")
        login_input.click()
        login_input.send_keys('b-2-38-30-ucu')
        amount_input = driver.find_element(By.XPATH, "(//*[@class='android.widget.EditText'])[3]")
        amount_input.click()
        amount_input.send_keys('1000')
        click_element(driver, "//*[@content-desc='Gals Telecom'][1]")
        click_element(driver, button_save)
        click_element(driver, button_continue)
    def test_add_payment_from_fav_home(self, appium_driver):
        driver = appium_driver
        time.sleep(1)
        # try:
        #     driver.find_element('xpath', "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]").click()
        # except NoSuchElementException:
        #     click_element(driver, "//*[@content-desc='Добавить платёж']")
        click_element(driver, "//*[@content-desc='Оплата']")
        click_element(driver, "//*[@content-desc='Из избранных']")
        click_element(driver, "//*[@content-desc='Добавить']")
        click_element(driver, button_continue)
    def test_add_payment_validation_error(self, appium_driver):
        driver = appium_driver
        time.sleep(1)
        # try:
        #     driver.find_element('xpath', "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]").click()
        #
        # except NoSuchElementException:
        #     click_element(driver, "//*[@content-desc='Добавить платёж']")
        click_element(driver, "//*[@content-desc='Оплата']")
        click_element(driver, "//*[@content-desc='Интернет']")
        click_element(driver, "//*[@content-desc='Gals Telecom']")
        time.sleep(2)
        fav_name = driver.find_element('xpath', "//android.widget.EditText")
        fav_name.click()
        random_word = fake.word()
        fav_name.send_keys(random_word)
        assert not driver.find_element(By.XPATH, button_save).is_enabled()
        screen_size = driver.get_window_size()
        screen_width = screen_size["width"]
        screen_height = screen_size["height"]
        # Координаты центра экрана
        center_x = screen_width // 2
        center_y = screen_height // 2
        # Выполнение тапа на пустое место
        action = TouchAction(driver)
        action.tap(x=center_x, y=center_y).perform()
        login_input = driver.find_element(By.XPATH, "(//*[@class='android.widget.EditText'])[2]")
        login_input.click()
        login_input.send_keys('b-2-38-30-ucu')
        time.sleep(0.5)
        assert not driver.find_element(By.XPATH, button_save).is_enabled()
        amount_input = driver.find_element(By.XPATH, "(//*[@class='android.widget.EditText'])[3]")
        amount_input.click()
        amount_input.send_keys('1000')
        click_element(driver, "//*[@content-desc='Gals Telecom'][1]")
        fav_name.click()
        fav_name.clear()
        time.sleep(0.5)
        assert not driver.find_element(By.XPATH, button_save).is_enabled()
        fav_name.click()
        fav_name.send_keys(random_word)
        login_input.click()
        login_input.clear()
        time.sleep(1)
        assert not driver.find_element(By.XPATH, button_save).is_enabled()
        login_input.click()
        login_input.send_keys('b-2-38-30-ucu')
        amount_input.click()
        amount_input.clear()
        time.sleep(0.5)
        assert not driver.find_element(By.XPATH, button_save).is_enabled()
        amount_input.click()
        amount_input.send_keys('1000')
        click_element(driver, button_save)
        click_element(driver, button_continue)

    def test_add_transfer_home(self, appium_driver):
        driver = appium_driver
        time.sleep(1)
        # try:
        #     driver.find_element('xpath', "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]").click()
        # except NoSuchElementException:
        #     click_element(driver, "//*[@content-desc='Добавить платёж']")
        click_element(driver, "//*[@content-desc='Перевод']")
        card_input = driver.find_element('xpath', "//android.widget.EditText[1]")
        fav_name = driver.find_element('xpath', "//android.widget.EditText[2]")
        amount_input = driver.find_element('xpath', "//android.widget.EditText[3]")
        card_input.click()
        card_input.send_keys('9860020101778536')
        fav_name.click()
        fav_name.send_keys('home_transfer')
        click_element(driver, "//*[@content-desc='Создать избранный']")
        assert not driver.find_element('xpath', "//*[@content-desc='Добавить']").is_enabled()
        amount_input.click()
        amount_input.send_keys('1000')
        click_element(driver, "//*[@content-desc='Создать избранный']")
        click_element(driver, "//*[@content-desc='Добавить']")
        click_element(driver, "//*[@content-desc='Продолжить']")

    def test_autopay_home(self, appium_driver):
        driver = appium_driver
        click_element(driver, "//*[contains(@content-desc, 'b-2-38-30-ucu')][2]")
        click_element(driver, "//*[@content-desc='Добавить автоплатёж']")
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
        try:
            otp_input = driver.find_element('xpath', "//android.widget.EditText")
            otp_input.click()
            otp_input.send_keys(otp)
        except NoSuchElementException:
            pass
        click_element(driver, button_continue)

    def test_delete_home(self, appium_driver):
        driver = appium_driver
        driver.back()
        click_element(driver, "//*[@content-desc='Мой дом']")
        # click_element(driver, "android.widget.ImageView[@content-desc='Dom_ui']/android.widget.Button")
        click_element(driver, "//*[@content-desc='Удалить']")
        click_element(driver, "//*[@content-desc='Да']")






