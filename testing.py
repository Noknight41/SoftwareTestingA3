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
from wishListUTC import TH1, TH2, TH3, TH4

PATH=".\chromedriver.exe"
PATHFORMAC="./chromedriver"

class Selen:
  def __init__(self):
    self.driver = None
    self.options = Options()
    self.options.add_experimental_option("detach", True)
    self.options.add_argument('headless')
    self.options.add_argument('--ignore-certificate-errors')
    self.options.add_argument('--ignore-ssl-errors')
    self.service = Service(PATHFORMAC)
    
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
  
  def wishListUTC(self, case, category, product, email, password):
    self.setup()
    try:
      if case == 'TH1':
        return TH1(self.driver, category , product, email, password)
      if case == 'TH2':
        return TH2(self.driver, category , product, email, password)
      if case == 'TH3':
        return TH3(self.driver, category , product, email, password)
      if case == 'TH4':
        return TH4(self.driver, category , product, email, password)  
    except TimeoutException:
      print("Loading took too much time!")
    except:
      print("Something went wrong in wishListUTC")
        
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
    
  def runWishListUTC(self):
    if os.path.exists('Output/UTC.xlsx'):
      os.remove('Output/UTC.xlsx')

    result = [['Testcase', 'Expected', 'Got', 'Result']]
    instance = Selen()
    excel = Excel("Input/UTC.xlsx")
    UTCdata = excel.readData("Input")
    for testcase in UTCdata:
      if(testcase[0] == ''):
        continue
      data = instance.wishListUTC(testcase[2], testcase[3], testcase[4], testcase[5], testcase[6])
      if data:
        result.append([testcase[0], 'True', 'True', 'Passed'])
      else:
        result.append([testcase[0], 'True', 'False', 'Failed'])
  
    excel.writeData(result, "UTC")
    
instance = RunTest()
instance.runWishListUTC()





