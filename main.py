from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

with open('config.json') as f:
    config = json.load(f)

email = config['email']
password = config['password']

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)
driver.get('https://www.facebook.com')
try:
    cook = driver.find_element(By.XPATH, '//div[@aria-label="Decline optional cookies"]')
    cook.click()
except NoSuchElementException:
    pass
emailelement = driver.find_element(By.XPATH, '//*[@id="email"]')
emailelement.send_keys(email)
passelement = driver.find_element(By.XPATH, '//*[@id="pass"]')
passelement.send_keys(password)

elem = driver.find_element(By.XPATH, '//*[@name="login"]')
elem.click()

home = driver.find_element(By.XPATH,'//a[@aria-label="Home"]')
home.click()

statuselement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="What\'s on your mind, Alfiya?"]')))
statuselement.click()

input_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//p[@class="xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8"]')))
input_field.send_keys('Im new here')
post_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Post"]')))
post_button.click()

