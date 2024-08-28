import base64
from dotenv import load_dotenv
import os
import datetime
import pytest
from appium import webdriver
import time
import telebot
from appium.options.android import UiAutomator2Options
from selenium.common.exceptions import NoSuchElementException
from tests.click_func import click_element, swipe
import json
# from appium_flutter_finder.flutter_finder import FlutterFinder


# finder = FlutterFinder()

environment = "test"
MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 5
# Загрузите соответствующий конфигурационный файл
config_file = f"/Users/zhshayusupov/PycharmProjects/Autotests-mobile/config_{environment}.json"

with open(config_file, "r") as file:
    config = json.load(file)

# Используйте переменные из конфигурационного файла
app_package = config["appPackage"]
app_activity = config["appActivity"]


load_dotenv()
otp = '958536'
password = [9,5,8,5,3,6]

token = os.getenv('token')
chat_id = os.getenv('chat_id')
bot = telebot.TeleBot(token)


def get_current_date():
    now = datetime.datetime.now()
    return now.strftime("%d-%m-%Y_%H-%M-%S")

def send_video_to_telegram(video_path):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            video = open(video_path, 'rb')
            description = f"Video description: {os.path.basename(video_path)}"
            bot.send_message(chat_id, description)  # Отправляем описание
            bot.send_video(chat_id, video)  # Замените CHAT_ID на ID вашего чата или группы
            video.close()
            print("Видео успешно отправлено!")
            break  # Выход из цикла, если отправка прошла успешно
        except Exception as e:
            print(f"Ошибка при отправке видео (попытка {attempt}/{MAX_RETRIES}):", e)
            if attempt < MAX_RETRIES:
                print(f"Повторная попытка через {RETRY_DELAY_SECONDS} секунд...")
                time.sleep(RETRY_DELAY_SECONDS)
            else:
                print("Достигнуто максимальное количество попыток. Отправка не удалась.")




@pytest.fixture(scope='function')
def appium_driver_login(request):
    test_class_name = request.node.parent.name
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": app_package,
        "appActivity": app_activity,
        "appium:automationName": "UIAutomator2",
        "appium:noReset": False,
        "autoAcceptAlerts": True,
        "autoGrantPermissions": True,
        "newCommandTimeout": 300
    }
    options = UiAutomator2Options().load_capabilities(desired_caps)

    driver = None
    try:
        driver = webdriver.Remote("http://localhost:4723", options=options)
        driver.implicitly_wait(20)
        driver.start_recording_screen()
        yield driver
    except Exception as e:


        print("Ошибка при создании драйвера:", e)

        raise

    finally:
        if driver:
            recording_data = driver.stop_recording_screen()
            video_filename = f"{test_class_name}_{get_current_date()}.mp4"
            with open(video_filename, "wb") as file:
                file.write(base64.b64decode(recording_data))

            send_video_to_telegram(video_filename)
            os.remove(video_filename)
            print("Video deleted")

        driver.quit()




