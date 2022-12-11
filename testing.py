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

from excelDriver import Excel 

# windows
PATH=".\chromedriver.exe"

# ubuntu
# PATH = "./chromedriver"

class Selen:
  def __init__(self):
    self.driver = None
    self.options = Options()
    self.options.add_experimental_option("detach", True)
    self.options.add_argument('headless')
    self.options.add_argument('--ignore-certificate-errors')
    self.options.add_argument('--ignore-ssl-errors')
    self.service = Service(PATH)
    
  def setup(self):
    self.driver = webdriver.Chrome(service=self.service, chrome_options=self.options)
    
  def passwordStrengthDTT(self, id, i, o, result):
    self.setup()
    self.driver.get("https://magento.softwaretestingboard.com/customer/account/create/")
    passwordInput = self.driver.find_element(By.ID, "password")
    try:
      time.sleep(2)
      passwordStrength = self.driver.find_element(By.ID, 'password-strength-meter-label') 
      passwordInput.clear()
      passwordInput.send_keys(i)
      print(passwordStrength.text == o)
      result.append([id, o, passwordStrength.text, str(passwordStrength.text == o)])
    except TimeoutException:
      print("Loading took too much time!")
    self.driver.quit()

  def loginDTT(self, id, e, p, o, result):
    self.setup()
    loginUrl = 'https://magento.softwaretestingboard.com/customer/account/login'
    self.driver.get(loginUrl)
    emailInput = self.driver.find_element(By.ID, "email")
    passwordInput = self.driver.find_element(By.ID, "pass")
    submitButton = self.driver.find_element(By.ID, "send2")
    try:
      emailInput.clear()
      emailInput.send_keys(e)
      passwordInput.clear()
      passwordInput.send_keys(p)
      submitButton.click()

      got = None
      try:
          self.driver.find_element(By.ID, "email-error")
          got = 'invalid email'
      except NoSuchElementException:
          wait = WebDriverWait(self.driver, 10)
          wait.until(lambda driver: driver.current_url != loginUrl)

          if self.driver.current_url == 'https://magento.softwaretestingboard.com/customer/account/':
              got = 'login success'
          else:
              got = 'login failure'
      print(got == o)
      result.append([id, o, got, str(got == o)])
    except TimeoutException:
      print("Loading took too much time!")
    self.driver.quit()

class RunTest:
  def __init__(self):
    pass
  
  def runDTT(self):
    if os.path.exists('./Output/DTT.xlsx'):
      os.remove('./Output/DTT.xlsx')

    result = [['Testcase', 'Expected', 'Got', 'Result']]
    instance = Selen()
    excel = Excel("Input/DTT.xlsx")
    DTTdata = excel.readData("Input")

    for testcase in DTTdata:
      instance.passwordStrengthDTT(testcase[0], testcase[1], testcase[2], result)
  
    excel.writeData(result, "DTT")

  def runECT(self):
    if os.path.exists('./Output/ECT.xlsx'):
      os.remove('./Output/ECT.xlsx')

    result = [['Testcase', 'Expected', 'Got', 'Result']]
    instance = Selen()
    excel = Excel("Input/ECT.xlsx")
    ECTdata = excel.readData("Input")

    for testcase in ECTdata:
      instance.loginDTT(testcase[0], testcase[1], testcase[2], testcase[3], result)

    excel.writeData(result, "ECT")
    
instance = RunTest()
# instance.runDTT()
instance.runECT()





