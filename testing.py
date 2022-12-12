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

PATH="./chromedriver.exe"

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

	def addItemToCart(self):
		self.setup()
		self.driver.get("https://magento.softwaretestingboard.com/phoebe-zipper-sweatshirt.html")
		time.sleep(4)
		self.driver.find_element(By.ID, "option-label-size-143-item-166").click()
		self.driver.find_element(By.ID, "option-label-color-93-item-52").click()
		self.driver.find_element(By.ID, "product-addtocart-button").click()

	def changeItemQty(self, 
		id, 
		input, 
		output, 
		result
	):
		self.addItemToCart()
		time.sleep(2)
		self.driver.get("https://magento.softwaretestingboard.com/checkout/cart/")
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

class RunTest:
	def __init__(self):
		pass

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
    
instance = RunTest()
instance.runBVT()





