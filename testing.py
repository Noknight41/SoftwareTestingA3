import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import (AbstractEventListener, EventFiringWebDriver)

PATH=".\chromedriver.exe"

class CustomEventListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
      pass
    
    def after_navigate_to(self, url, driver):
      pass

    def before_find(self, by, value, driver):
      pass

    def after_find(self, by, value, driver):
      pass

    def before_quit(self, driver):
      pass

    def after_quit(self, driver):
      pass

class Selen:
  def __init__(self):
    pass
    
  def passwordStrengthDTT(self):
    global driver, event_firing_driver
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    service = Service(PATH)
    driver = webdriver.Chrome(service=service, chrome_options=options)
    driver.maximize_window()
    event_firing_driver = EventFiringWebDriver(driver, AbstractEventListener())
    
    event_firing_driver.get("https://magento.softwaretestingboard.com/customer/account/create/")
    passwordInput = event_firing_driver.find_element(By.ID, "password")
    try:
      time.sleep(1)
      passwordStrength = event_firing_driver.find_element(By.ID, 'password-strength-meter-label') 
      passwordInput.clear()
      passwordInput.send_keys("Hweqwello12")
      print(passwordStrength.text)
    except TimeoutException:
      print("Loading took too much time!")
    event_firing_driver.quit()
  
  
instance = Selen()
instance.passwordStrengthDTT()
instance.passwordStrengthDTT()
instance.passwordStrengthDTT()
instance.passwordStrengthDTT()
instance.passwordStrengthDTT()