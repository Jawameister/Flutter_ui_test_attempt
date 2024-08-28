from tests.conftest import appium_driver
import time
from datetime import datetime
from faker import Faker
from tests.click_func import click_element, swipe
from tests.often_used_buttons import apply

current_date = datetime.now().strftime("%d-%m-%Y")

fake = Faker()

class Test_History:
    def test_history(self, appium_driver):
        driver = appium_driver

        click_element(driver, "//*[@content-desc='Мониторинг']")
        click_element(driver, "//*[@content-desc='Поступления']")
        click_element(driver, "//*[@content-desc='Расходы']")
        click_element(driver, "//*[@content-desc='Добавить фильтры']")
        click_element(driver, f"//*[contains(@content-desc, '{current_date}')]")
        swipe(driver, 175, 1500, 175, 1843)
        time.sleep(3)
        click_element(driver, apply)
        # click_element(driver, f"//*[contains(@content-desc, 'Добавить карту')]")
        # # click_element(driver, "//*[@content-desc='Добавить карту']")
        # click_element(driver, f"//*[contains(@content-desc, 'ILYAS')]")

        time.sleep(0.5)

        click_element(driver, apply)
        swipe(driver, 175, 1800, 175, 800)
        swipe(driver, 175, 800, 175, 1800)
        click_element(driver, "//*[@content-desc='Редактировать фильтры']")
        click_element(driver, "//*[@content-desc='С 1го числа']")
        click_element(driver, "//*[@content-desc='Оплаты']")
        click_element(driver, apply)
        time.sleep(0.5)
        click_element(driver, "//*[@content-desc='Редактировать фильтры']")
        time.sleep(0.3)
        click_element(driver, "//*[@content-desc='Переводы']")
        click_element(driver, apply)
        time.sleep(0.5)
        click_element(driver, "//*[@content-desc='Редактировать фильтры']")
        click_element(driver, "//*[@content-desc='Сегодня']")
        click_element(driver, apply)
        time.sleep(0.5)
        click_element(driver, "//*[@content-desc='Редактировать фильтры']")
        click_element(driver, "//*[@content-desc='3 дня']")
        click_element(driver, apply)
        time.sleep(0.5)
        click_element(driver, "//*[@content-desc='Редактировать фильтры']")
        click_element(driver, "//*[@content-desc='Неделя']")
        click_element(driver, apply)
        time.sleep(0.5)
        click_element(driver, "//*[@content-desc='Редактировать фильтры']")
        click_element(driver, "//*[@content-desc='Месяц']")
        click_element(driver, apply)
        time.sleep(0.5)
        click_element(driver, "//*[@content-desc='Редактировать фильтры']")
        click_element(driver, "//*[@content-desc='Все время']")
        click_element(driver, apply)
        swipe(driver, 175, 1800, 175, 800)
        swipe(driver, 175, 800, 175, 1800)
        #













