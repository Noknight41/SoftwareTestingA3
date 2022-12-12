import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def TH1(driver, category, product, email, password):
    driver.get("https://magento.softwaretestingboard.com/")
    time.sleep(3)
    products = driver.find_elements(By.CSS_SELECTOR, ".block-products-list .product-item")
    if (len(products) <= 0):
        driver.quit()
        return False
    navbars = driver.find_elements(By.CSS_SELECTOR, ".level0.ui-menu-item")
    for i in navbars:
        link = i.find_element(By.CSS_SELECTOR, "a[role='menuitem']")
        if link.text == category:
            link.click()
            break
    time.sleep(3)
    productsName = driver.find_elements(By.CSS_SELECTOR, ".block-products-list .product-item")
    for i in productsName:
        title = i.find_element(By.CSS_SELECTOR, "a.product-item-link")
        if title.text == product:
            ActionChains(driver).move_to_element(i).perform()
            time.sleep(3)
            addToWishList = i.find_element(By.CSS_SELECTOR, "a[title='Add to Wish List']")
    addToWishList.click()
    time.sleep(3)
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.ID, "send2").click()
    time.sleep(3)
    a = driver.find_elements(By.CSS_SELECTOR, ".products-grid.wishlist strong.product-item-name")
    for i in a:
        if i.text == product:
            driver.quit()
            return True
    driver.quit()
    return False

def TH2(driver, category, product, email, password):
    driver.get("https://magento.softwaretestingboard.com/customer/account/login/")
    time.sleep(3)
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.ID, "send2").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "a.logo").click()
    time.sleep(3)
    products = driver.find_elements(By.CSS_SELECTOR, ".block-products-list .product-item")
    if (len(products) <= 0):
        driver.quit()
        return False
    navbars = driver.find_elements(By.CSS_SELECTOR, ".level0.ui-menu-item")
    for i in navbars:
        link = i.find_element(By.CSS_SELECTOR, "a[role='menuitem']")
        if link.text == category:
            link.click()
            break
    time.sleep(3)
    productsName = driver.find_elements(By.CSS_SELECTOR, ".block-products-list .product-item")
    for i in productsName:
        title = i.find_element(By.CSS_SELECTOR, "a.product-item-link")
        if title.text == product:
            ActionChains(driver).move_to_element(i).perform()
            time.sleep(3)
            addToWishList = i.find_element(By.CSS_SELECTOR, "a[title='Add to Wish List']")
    addToWishList.click()
    time.sleep(3)
    a = driver.find_elements(By.CSS_SELECTOR, ".products-grid.wishlist strong.product-item-name")
    for i in a:
        if i.text == product:
            driver.quit()
            return True
    driver.quit()
    return False

def TH3(driver, categories, product, email, password):
    category1 = categories.split("/")[0]
    category2 = categories.split("/")[1]
    driver.get("https://magento.softwaretestingboard.com/customer/account/login/")
    time.sleep(3)
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.ID, "send2").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "a.logo").click()
    time.sleep(3)
    products = driver.find_elements(By.CSS_SELECTOR, ".block-products-list .product-item")
    if (len(products) <= 0):
        driver.quit()
        return False
    navbars = driver.find_elements(By.CSS_SELECTOR, ".level0.ui-menu-item")
    for i in navbars:
        link = i.find_element(By.CSS_SELECTOR, "a[role='menuitem']")
        if link.text == category1:
            link.click()
            break
    time.sleep(3)
    navbars = driver.find_elements(By.CSS_SELECTOR, ".level0.ui-menu-item")
    for i in navbars:
        link = i.find_element(By.CSS_SELECTOR, "a[role='menuitem']")
        if link.text == category2:
            link.click()
            break
    time.sleep(3)
    productsName = driver.find_elements(By.CSS_SELECTOR, ".block-products-list .product-item")
    for i in productsName:
        title = i.find_element(By.CSS_SELECTOR, "a.product-item-link")
        if title.text == product:
            ActionChains(driver).move_to_element(i).perform()
            time.sleep(3)
            addToWishList = i.find_element(By.CSS_SELECTOR, "a[title='Add to Wish List']")
    addToWishList.click()
    time.sleep(3)
    a = driver.find_elements(By.CSS_SELECTOR, ".products-grid.wishlist strong.product-item-name")
    for i in a:
        if i.text == product:
            driver.quit()
            return True
    driver.quit()
    return False

def TH4(driver, category, product, email, password):
    driver.get("https://magento.softwaretestingboard.com/customer/account/login/")
    time.sleep(3)
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.ID, "send2").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "a.logo").click()
    time.sleep(3)
    products = driver.find_elements(By.CSS_SELECTOR, ".block-products-list .product-item")
    if (len(products) <= 0):
        driver.quit()
        return False
    productsName = driver.find_elements(By.CSS_SELECTOR, ".block-products-list .product-item")
    for i in productsName:
        title = i.find_element(By.CSS_SELECTOR, "a.product-item-link")
        if title.text == product:
            ActionChains(driver).move_to_element(i).perform()
            time.sleep(3)
            addToWishList = i.find_element(By.CSS_SELECTOR, "a[title='Add to Wish List']")
    addToWishList.click()
    time.sleep(3)
    a = driver.find_elements(By.CSS_SELECTOR, ".products-grid.wishlist strong.product-item-name")
    for i in a:
        if i.text == product:
            driver.quit()
            return True
    driver.quit()
    return False