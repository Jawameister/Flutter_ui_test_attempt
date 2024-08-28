from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
# from appium_flutter_finder.flutter_finder import FlutterFinder
from selenium.common.exceptions import StaleElementReferenceException

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait
import time
ignored_exceptions = StaleElementReferenceException

def click_element(driver, locator_value, locator_type="xpath"):
    try:
        if locator_type == "id":
            element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, locator_value)))
        elif locator_type == "xpath":
            element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, locator_value)))
        elif locator_type == "link text":
            element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.LINK_TEXT, locator_value)))
        elif locator_type == "partial link text":
            element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, locator_value)))
        elif locator_type == "name":
            element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.NAME, locator_value)))
        elif locator_type == "tag name":
            element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.TAG_NAME, locator_value)))
        elif locator_type == "class name":
            element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, locator_value)))
        elif locator_type == "css selector":
            element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator_value)))
        else:
            raise ValueError("Unsupported locator type")

        element.click()
    except StaleElementReferenceException:
        time.sleep(1)
        if locator_type == "id":
            element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, locator_value)))
        elif locator_type == "xpath":
            element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, locator_value)))
        elif locator_type == "link text":
            element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.LINK_TEXT, locator_value)))
        elif locator_type == "partial link text":
            element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, locator_value)))
        elif locator_type == "name":
            element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.NAME, locator_value)))
        elif locator_type == "tag name":
            element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.TAG_NAME, locator_value)))
        elif locator_type == "class name":
            element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, locator_value)))
        elif locator_type == "css selector":
            element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator_value)))
        else:
            raise ValueError("Unsupported locator type")

def swipe(driver, start_x, start_y, end_x, end_y):
    action = TouchAction(driver)
    action.long_press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()




