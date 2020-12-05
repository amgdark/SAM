from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from unittest import TestCase

@fixture
def browser_chrome(context):
    context.driver = webdriver.Chrome()
    context.url = 'http://192.168.33.10:8000/'
    context.driver.implicitly_wait(5)
    context.keys = Keys
    context.test = TestCase()
    context.options = Options()
    context.extset = ['enable-automation', 'ignore-certificate-errors']
    
    # yield context.driver
    # context.driver.quit()

def before_all(context):
    use_fixture(browser_chrome, context)