import sys, time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select as Sel
import os
from datetime import datetime
from excelDriver import Excel 
from wishListUTC import TH1, TH2, TH3, TH4
from level0 import TestLogin

USER="jackson@gmail.com"
PASSWORD="donQuiote3"
ADDRESS="688 Main.st Saint Rows NJ USA"
LOGIN_URL='https://magento.softwaretestingboard.com/customer/account/login'
SIGNUP_URL="https://magento.softwaretestingboard.com/customer/account/create/"
ITEM_URL="https://magento.softwaretestingboard.com/phoebe-zipper-sweatshirt.html"
CART_URL="https://magento.softwaretestingboard.com/checkout/cart/"

# windows
PATH=".\chromedriver.exe"
# ubuntu
# PATH = "./chromedriver"
# mac
# PATH="./chromedriver"

class Selen:
  def __init__(self):
    self.driver = None
    self.options = Options()
    self.options.add_experimental_option("detach", True)
    self.options.add_argument('headless')
    self.options.add_argument('--ignore-certificate-errors')
    self.options.add_argument('--ignore-ssl-errors')
    self.options.add_argument('--window-size=1920,1080')
    self.service = Service(PATH)
    
  def setup(self):
    self.driver = webdriver.Chrome(service=self.service, chrome_options=self.options)
    
  def passwordStrengthDTT(self, id, i, o, result):
    self.setup()
    self.driver.get(SIGNUP_URL)
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
  
  def addItemToCart(self):
    self.setup()
    self.driver.get(ITEM_URL)
    time.sleep(4)
    self.driver.find_element(By.ID, "option-label-size-143-item-166").click()
    self.driver.find_element(By.ID, "option-label-color-93-item-52").click()
    self.driver.find_element(By.ID, "product-addtocart-button").click()

  def changeItemQty(self, id, input, output, result):
    self.addItemToCart()
    time.sleep(2)
    self.driver.get(CART_URL)
    time.sleep(2)

    try:
      qtyInput = self.driver.find_element(By.CSS_SELECTOR, "input.input-text.qty")
      qtyInput.clear()
      qtyInput.send_keys(input)
      self.driver.find_element(By.CSS_SELECTOR, "button.action.update").click()
      
      time.sleep(4)
      res = "Success"

      if self.driver.find_elements(By.CSS_SELECTOR, "div.mage-error") != []:
        res = self.driver.find_element(By.CSS_SELECTOR, "div.mage-error").text
      elif self.driver.find_elements(By.CSS_SELECTOR, "div.modal-inner-wrap .modal-title") != []:
        res = self.driver.find_elements(By.CSS_SELECTOR, "div.modal-inner-wrap .modal-content")[1].text
      result.append([id, output, res, res == output])
      print(res == output)
    except TimeoutException:
      print("Timeout!")

    self.driver.quit()

  def loginECT(self, id, e, p, o, result):
    self.setup()
    self.driver.get(LOGIN_URL)
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
          wait.until(lambda driver: driver.current_url != LOGIN_URL)

          if self.driver.current_url == 'https://magento.softwaretestingboard.com/customer/account/':
              got = 'login success'
          else:
              got = 'login failure'
      print(got == o)
      result.append([id, o, got, str(got == o)])
    except TimeoutException:
      print("Loading took too much time!")
    self.driver.quit()
  
  def nonFunctional(self, eta_time, result):
    self.setup()
    self.driver.get(LOGIN_URL)
    self.driver.find_element("id","email").send_keys(USER)
    self.driver.find_element("id","pass").send_keys(PASSWORD)
    self.driver.find_element("id","send2").click()
    try:
      time.sleep(1)
      self.driver.get("https://magento.softwaretestingboard.com/radiant-tee.html")
      # print('check_1')
      time.sleep(2)
      self.driver.find_element(By.ID,"option-label-size-143-item-166").click()
      self.driver.find_element(By.ID,"option-label-color-93-item-57").click()
      self.driver.find_element(By.ID,"product-addtocart-button").click()
      time.sleep(5)
      self.driver.find_element(By.CLASS_NAME,"minicart-wrapper").click()
      # print('check_2')
      time.sleep(2)
      self.driver.find_element(By.ID,"top-cart-btn-checkout").click()
      # print('check_3')
      
      time.sleep(5)
      if self.driver.find_elements(By.CLASS_NAME, "new-address-popup"):
        print(True)
        # self.driver.find_element(By.CLASS_NAME, "action action-show-popup").click()
      else:
        self.driver.find_element(By.NAME,"street[0]").send_keys(ADDRESS)
        # print('check_4')
        self.driver.find_element(By.NAME,"city").send_keys("New Jersey")
        # print('check_5')
        State = Sel(self.driver.find_element(By.NAME,"region_id"))
        # print('check_6')
        State.select_by_visible_text("New Jersey")
        # print('check_7')
        self.driver.find_element(By.NAME,"postcode").send_keys("02222222222")
        # print('check_8')
        self.driver.find_element(By.NAME,"telephone").send_keys("02222222222")
        # print('check_9')
      self.driver.find_element(By.NAME,"ko_unique_2").click()
      # print('check_10')      
      # self.driver.find_element(By.ID,"shipping-method-buttons-container").click()
      self.driver.find_element(By.CSS_SELECTOR,".button.action.continue.primary").click()
      # print('check_11')
      
      time.sleep(5)
      
      # self.driver.find_element(By.XPATH,"/html/body/div[3]/main/div[2]/div/div[2]/div[4]/ol/li[3]/div/form/fieldset/div[1]/div/div/div[2]/div[2]/div[4]/div/button").click()
      # if self.driver.find_elements(By.CLASS_NAME, "payment-method-content"):
      #   print("YES")
      # else:
      #   with open("page.html","w") as f:
      #     f.write(self.driver.find_element(By.TAG_NAME,"html").get_attribute("innerHTML"))
      start=datetime.now()
      self.driver.find_element(By.CLASS_NAME,"checkout").click()
      # self.driver.find_element(By.XPATH,"//button[@title='Place Order']").click()
      element_present = EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Thank you for your purchase!')]"))
      WebDriverWait(self.driver, eta_time).until(element_present)
      res = (datetime.now()-start)
      res = res.seconds
      if (res>eta_time ):
        result.append(["Slower", res, res-eta_time])
      else:
        result.append(["Faster", res, res-eta_time])

    except TimeoutException:
      print("connection timedout")
    except Exception as e:
      print("error occrured:",e)
    self.driver.quit()
      
  def wishListUCT(self, case, category, product, email, password):
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
  
  def runLevel0(self):
    instance = TestLogin()
    instance.setup_method(None)
    instance.test_login()
    instance.teardown_method(None)
  
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
      instance.loginECT(testcase[0], testcase[1], testcase[2], testcase[3], result)

    excel.writeData(result, "ECT")
  
  def runUCT(self):
    if os.path.exists('Output/UTC.xlsx'):
      os.remove('Output/UTC.xlsx')

    result = [['Testcase', 'Expected', 'Got', 'Result']]
    instance = Selen()
    excel = Excel("Input/UTC.xlsx")
    UCTdata = excel.readData("Input")
    for testcase in UCTdata:
      if(testcase[0] == ''):
        continue
      data = instance.wishListUCT(testcase[2], testcase[3], testcase[4], testcase[5], testcase[6])
      if data:
        result.append([testcase[0], 'True', 'True', 'Passed'])
      else:
        result.append([testcase[0], 'True', 'False', 'Failed'])
  
    excel.writeData(result, "UTC")
  
  def runNonFunc(self):
    if os.path.exists('Output/NF.xlsx'):
      os.remove('Output/NF.xlsx')
    result = [['Eval', 'Backend', 'Diff']]
    instance = Selen()
    excel = Excel("Input/NF.xlsx")
    NFdata = excel.readData("Input")
    print(NFdata)
    for testcase in NFdata:
      instance.nonFunctional(5, result)
    excel.writeData(result, "NF")
  
  def runBVT(self):
    if os.path.exists('Output/BVT.xlsx'):
      os.remove('Output/BVT.xlsx')

    result = [['Testcase', 'Expected', 'Got', 'Result']]
    instance = Selen()
    excel = Excel("Input/BVT.xlsx")
    BVTData = excel.readData("Input")

    for testcase in BVTData:
      instance.changeItemQty(testcase[0], testcase[1], testcase[2], result)
			# print(testcase)
    print(result)
    excel.writeData(result, "BVT")
    
def main():
  args = sys.argv[1:]
  if len(args) != 1:
    instance = RunTest()
    instance.runLevel0()
    return
  if args[0] in ['DTT', 'BVT', 'ECT', 'UCT', 'NF']:
    instance = RunTest()
    if args[0] == 'DTT':
      instance.runDTT()
    if args[0] == 'BVT':
      instance.runBVT()
    if args[0] == 'ECT':
      instance.runECT()
    if args[0] == 'UCT':
      instance.runUCT()
    if args[0] == 'NF':
      instance.runNonFunc()   
  return  

if __name__=="__main__": 
  main()





