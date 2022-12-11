import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

PATH = "./chromedriver"

options = Options()
options.add_experimental_option("detach", True)
# options.add_argument('headless')
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
service = Service(PATH)
driver = webdriver.Chrome(service=service, chrome_options=options)

loginUrl = 'https://magento.softwaretestingboard.com/customer/account/login'
driver.get(loginUrl)
emailInput = driver.find_element(By.ID, "email")
passwordInput = driver.find_element(By.ID, "pass")
submitButton = driver.find_element(By.ID, "send2")

emailInput.clear()
emailInput.send_keys("khoa20082001@gmail.com")

passwordInput.clear()
passwordInput.send_keys("Khoa20082001")

submitButton.click()

try:
    driver.find_element(By.ID, "email-error")
    print('true')
except NoSuchElementException:
    print('false')

wait = WebDriverWait(driver, 10)
wait.until(lambda driver: driver.current_url != loginUrl)

if driver.current_url == 'https://magento.softwaretestingboard.com/customer/account/':
    print('success')
else:
    print('failure')

driver.delete_all_cookies()