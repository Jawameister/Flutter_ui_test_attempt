import time
from tests.conftest import appium_driver
from selenium.common.exceptions import NoSuchElementException
from faker import Faker
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from tests.click_func import click_element
from tests.often_used_buttons import button_continue, button_save
fake = Faker()


class Test_favorites:
    def test_favorites_add_payment(self, appium_driver):
        driver = appium_driver
        action = TouchAction(driver)
        action.long_press(x=516, y=1485).move_to(x=516, y=700).release().perform()
        click_element(driver, "//*[@content-desc='Избранные']")
        click_element(driver, "//*[@content-desc='Добавить в избранные']")
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
        # login_input = driver.find_element('xpath', "//android.widget.EditText[1]")
        # login_input = click_element(driver, "//android.widget.EditText[1]")
        login_input = driver.find_element('xpath', "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[5]/android.view.View/android.view.View/android.widget.EditText[1]")
        login_input.click()
        login_input.send_keys('b-2-38-30-ucu')

        amount_input = driver.find_element('xpath', "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[5]/android.view.View/android.view.View/android.widget.EditText[2]")
        amount_input.click()
        amount_input.send_keys('1000')
        click_element(driver, "//*[@content-desc='Gals Telecom'][1]")
        click_element(driver, "//*[@content-desc='Сохранить']")
        click_element(driver, "//*[@content-desc='Продолжить']")
    def test_favorites_add_transfer(self, appium_driver):
        driver = appium_driver
        action = TouchAction(driver)
        action.long_press(x=516, y=1485).move_to(x=516, y=700).release().perform()
        click_element(driver, "//*[@content-desc='Избранные']")
        click_element(driver, "//*[@content-desc='Добавить в избранные']")
        click_element(driver, "//*[@content-desc='Перевод']")
        card_input = driver.find_element('xpath', "//android.widget.EditText[1]")
        fav_name = driver.find_element('xpath', "//android.widget.EditText[2]")
        amount_input = driver.find_element('xpath', "//android.widget.EditText[3]")
        card_input.click()
        card_input.send_keys('9860020101778536')
        fav_name.click()
        fav_name.send_keys('fav_transfer')
        click_element(driver, "//*[@content-desc='Создать избранный']")
        assert not driver.find_element('xpath', "//*[@content-desc='Добавить']").is_enabled()
        amount_input.click()
        amount_input.send_keys('1000')
        click_element(driver, "//*[@content-desc='Создать избранный']")
        click_element(driver, "//*[@content-desc='Добавить']")
        click_element(driver, "//*[@content-desc='Продолжить']")

    def test_favorites_edit_payment(self, appium_driver):
        driver = appium_driver
        click_element(driver, "(//*[contains(@content-desc, \'b-2-38-30-ucu\')][1]/android.widget.Button)")
        click_element(driver, "//*[@content-desc='Редактировать']")
        random_word = fake.word()
        fav_name = driver.find_element('xpath', "//android.widget.EditText[1]")
        fav_name.click()
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
        click_element(driver, button_save)
        click_element(driver, button_continue)
    def test_favorites_edit_transfer(self, appium_driver):
        driver = appium_driver
        click_element(driver, "(//*[contains(@content-desc, \'**\')][1]/android.widget.Button)")
        click_element(driver, "//*[@content-desc='Редактировать']")
        random_word = fake.word()
        fav_name = driver.find_element('xpath', "//android.widget.EditText[2]")
        fav_name.click()
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
        click_element(driver, button_save)
        click_element(driver, button_continue)
    def test_favorites_delete(self, appium_driver):
        driver = appium_driver
        click_element(driver, "(//*[contains(@content-desc, \'**\')][1]/android.widget.Button)")
        click_element(driver, "//*[@content-desc='Удалить']")
        click_element(driver, "//*[@content-desc='Нет']")
        click_element(driver, "(//*[contains(@content-desc, \'**\')][1]/android.widget.Button)")
        click_element(driver, "//*[@content-desc='Удалить']")
        click_element(driver, "//*[@content-desc='Да']")

    def test_favorites_to_folder(self, appium_driver):
        driver = appium_driver
        click_element(driver, "(//*[contains(@content-desc, \'**\')][1]/android.widget.Button)")
        click_element(driver, "//*[@content-desc='Добавить в дом']")
        click_element(driver, "//*[@content-desc='Добавить новый Дом']")
        random_word = fake.word()
        try:
            home_name = driver.find_element('xpath', "//android.widget.EditText")
        except NoSuchElementException:
            home_name = driver.find_element(By.CLASS_NAME, "android.widget.EditText")
        home_name.click()
        home_name.send_keys(random_word)
        click_element(driver, button_save)
        click_element(driver, f"//*[@content-desc='{random_word}']")





