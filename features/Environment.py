import time

from selenium import webdriver
from selenium.webdriver import chrome
from configparser import ConfigParser
import constants

config = ConfigParser()
config.read("./inputs/Config.cfg")

def before_all(context):
    context.driver = webdriver.Chrome(constants.WEBDRIVER_PATH)
    context.driver.get(config.get("Environments", "url"))
    time.sleep(5)
    context.driver.find_element_by_css_selector(constants.USERNAME).send_keys(config.get("Logincredentials", "username"))
    time.sleep(5)
    context.driver.find_element_by_xpath(constants.SUBMITBUTON).click()
    time.sleep(5)
    context.driver.find_element_by_css_selector(constants.PASSWORD).send_keys(config.get("Logincredentials", "password"))
    time.sleep(5)
    context.driver.find_element_by_xpath(constants.SUBMITBUTON).click()
    time.sleep(15)



def after_all(context):
   context.browser.close()

