# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    # Test name: login
    # Step # | name | target | value
    # 1 | open | https://magento.softwaretestingboard.com/customer/account/login | 
    self.driver.get("https://magento.softwaretestingboard.com/customer/account/login")
    # 2 | setWindowSize | 1848x1053 | 
    self.driver.set_window_size(1848, 1053)
    # 3 | click | id=email | 
    self.driver.find_element(By.ID, "email").click()
    # 4 | type | id=email | khoa20082001@gmail.com
    self.driver.find_element(By.ID, "email").send_keys("khoa20082001@gmail.com")
    # 5 | type | id=pass | Khoa20082001
    self.driver.find_element(By.ID, "pass").send_keys("Khoa20082001")
    # 6 | sendKeys | id=pass | ${KEY_ENTER}
    self.driver.find_element(By.ID, "pass").send_keys(Keys.ENTER)
    # 7 | click | css=.header:nth-child(2) > .customer-welcome .action | 
    self.driver.find_element(By.CSS_SELECTOR, ".header:nth-child(2) > .customer-welcome .action").click()
    # 8 | click | linkText=Sign Out | 
    self.driver.find_element(By.LINK_TEXT, "Sign Out").click()
    # 9 | click | linkText=Sign In | 
    self.driver.find_element(By.LINK_TEXT, "Sign In").click()
    # 10 | click | id=email | 
    self.driver.find_element(By.ID, "email").click()
    # 11 | type | id=email | khoa20082001@gmail.com
    self.driver.find_element(By.ID, "email").send_keys("khoa20082001@gmail.com")
    # 12 | type | id=pass | khoa
    self.driver.find_element(By.ID, "pass").send_keys("khoa")
    # 13 | click | id=send2 | 
    self.driver.find_element(By.ID, "send2").click()
    # 14 | click | id=email | 
    self.driver.find_element(By.ID, "email").click()
    # 15 | type | id=email | khoa20082001gmail.com
    self.driver.find_element(By.ID, "email").send_keys("khoa20082001gmail.com")
    # 16 | click | id=pass | 
    self.driver.find_element(By.ID, "pass").click()
    # 17 | type | id=pass | khoa
    self.driver.find_element(By.ID, "pass").send_keys("khoa")
    # 18 | click | css=.primary:nth-child(1) > #send2 > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".primary:nth-child(1) > #send2 > span").click()
    # 19 | type | id=email | khoakhoa@gmail.com
    self.driver.find_element(By.ID, "email").send_keys("khoakhoa@gmail.com")
    # 20 | click | css=.page-wrapper | 
    self.driver.find_element(By.CSS_SELECTOR, ".page-wrapper").click()
    # 21 | click | css=.primary:nth-child(1) > #send2 > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".primary:nth-child(1) > #send2 > span").click()
    # 22 | close |  | 
    self.driver.close()
  
