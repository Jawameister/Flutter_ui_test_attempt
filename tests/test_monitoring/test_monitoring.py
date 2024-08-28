from faker import Faker
from datetime import datetime
from tests.conftest import appium_driver

from tests.often_used_buttons import apply, button_continue
from tests.click_func import click_element, swipe
import time
current_date = datetime.now().strftime("%d-%m-%Y")

fake = Faker()

class Test_monitoring:
    def test_monitoring_connect_and_filtering(self, appium_driver):
        driver = appium_driver
        click_element(driver, "//*[@content-desc='Мониторинг']")
        # click_element(driver, "//*[@content-desc='Мониторинг карты']")
        swipe(driver, 1300, 1300, 145, 1300)
        click_element(driver, "//*[@content-desc='Подключить мониторинг']")
        click_element(driver, f"//*[contains(@content-desc, 'ILYAS')]")
        click_element(driver, "//*[@content-desc='Да']")
        click_element(driver, button_continue)
        swipe(driver, 175, 1800, 175, 800)
        swipe(driver, 175, 800, 175, 1800)
        click_element(driver, "//*[@content-desc='Поступления']")
        click_element(driver, "//*[@content-desc='Расходы']")
        click_element(driver, "//*[@content-desc='Добавить фильтры']")
        click_element(driver, "//*[contains(@content-desc, 'ILYAS')]")
        click_element(driver, "//*[contains(@content-desc, 'ILYAS')]")
        click_element(driver, "//*[@content-desc='Сегодня']")
        click_element(driver, f"//*[@content-desc='{current_date} - {current_date}']")
        swipe(driver, 250, 1500, 250, 2300)
        click_element(driver, apply)
        click_element(driver, apply)
        swipe(driver, 175, 1800, 175, 800)
        swipe(driver, 175, 800, 175, 1800)
        swipe(driver, 531, 204, 531, 2000)
        click_element(driver, "//*[@content-desc='Редактировать фильтры']")
        click_element(driver, "//*[@content-desc='С 1го числа']")
        click_element(driver, apply)
        click_element(driver, "//*[@content-desc='Поступления']")
        click_element(driver, "//*[@content-desc='Расходы']")
        click_element(driver, "//*[@content-desc='Редактировать фильтры']")
        click_element(driver, "//*[@content-desc='Неделя']")
        click_element(driver, apply)
        click_element(driver, "//*[@content-desc='Поступления']")
        click_element(driver, "//*[@content-desc='Расходы']")
        click_element(driver, "//*[@content-desc='Редактировать фильтры']")
        click_element(driver, "//*[@content-desc='Месяц']")
        click_element(driver, apply)
        click_element(driver, "//*[@content-desc='Поступления']")
        click_element(driver, "//*[@content-desc='Расходы']")
        click_element(driver, "//*[@content-desc='Редактировать фильтры']")
        click_element(driver, "//*[@content-desc='Все время']")
        click_element(driver, apply)
        time.sleep(5)
        click_element(driver, "//*[@content-desc='Поступления']")
        click_element(driver, "//*[@content-desc='Расходы']")
        swipe(driver, 175, 2500, 175, 200)
        click_element(driver, "//*[@content-desc='Главная']")
        click_element(driver, "//*[contains(@content-desc, 'ILYAS')]")
        click_element(driver, "//*[@content-desc='Подключить мониторинг']/android.widget.Switch")
        click_element(driver, "//*[@content-desc='Да']")
        click_element(driver, button_continue)











