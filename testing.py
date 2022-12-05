import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

from excelDriver import Excel 

PATH=".\chromedriver.exe"

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
      result.append([id, o, passwordStrength.text, passwordStrength.text == o])
    except TimeoutException:
      print("Loading took too much time!")
    self.driver.quit()

class RunTest:
  def __init__(self):
    pass
  
  def runDTT(self):
    if os.path.exists('Output/DTT.xlsx'):
      os.remove('Output/DTT.xlsx')

    result = [['Testcase', 'Expected', 'Got', 'Result']]
    instance = Selen()
    excel = Excel("Input/DTT.xlsx")
    DTTdata = excel.readData("Input")

    for testcase in DTTdata:
      instance.passwordStrengthDTT(testcase[0], testcase[1], testcase[2], result)
  
    excel.writeData(result, "DTT")
    
instance = RunTest()
instance.runDTT()





