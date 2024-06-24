import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
driver.maximize_window()
time.sleep(2)
# Login
driver.find_element(By.NAME, "user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
time.sleep(2)
# Add to Cart
driver.execute_script('window.scrollBy(0, 300)')
driver.find_element(By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
time.sleep(5)
# ShoppingCart
driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').click()
time.sleep(2)
# CheckOut
driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
time.sleep(2)
# Details
driver.find_element(By.NAME, "firstName").send_keys("Jake")
time.sleep(2)
driver.find_element(By.NAME, "lastName").send_keys("Othniel")
time.sleep(2)
driver.find_element(By.NAME, "postalCode").send_keys("+234")
time.sleep(2)
driver.execute_script('window.scrollBy(0, 300)')
# Continue
driver.find_element(By.XPATH, '//*[@id="continue"]').click()
time.sleep(2)
# Finish
driver.find_element(By.XPATH, '//*[@id="finish"]').click()
time.sleep(2)
# Home
driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
time.sleep(2)

# ITEM TWO
# Add to Cart
driver.execute_script('window.scrollBy(0, 300)')
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
time.sleep(5)
# ShoppingCart
driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
time.sleep(2)
# CheckOut
driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
time.sleep(2)
# Details
driver.find_element(By.NAME, "firstName").send_keys("Dan")
time.sleep(2)
driver.find_element(By.NAME, "lastName").send_keys("May")
time.sleep(2)
driver.find_element(By.NAME, "postalCode").send_keys("001")
time.sleep(2)
driver.execute_script('window.scrollBy(0, 300)')
# Continue
driver.find_element(By.XPATH, '//*[@id="continue"]').click()
time.sleep(2)
# Finish
driver.find_element(By.XPATH, '//*[@id="finish"]').click()
time.sleep(2)
# Logout
driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
time.sleep(2)

# EDGE BROWSER
driver = webdriver.Edge()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)
# Login
driver.find_element(By.NAME, "user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
time.sleep(2)
# Add to Cart
driver.execute_script('window.scrollBy(0, 300)')
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]').click()
time.sleep(5)
# ShoppingCart
driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
time.sleep(2)
# CheckOut
driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
time.sleep(2)
# Details
driver.find_element(By.NAME, "firstName").send_keys("Shanny")
time.sleep(2)
driver.find_element(By.NAME, "lastName").send_keys("Sophie")
time.sleep(2)
driver.find_element(By.NAME, "postalCode").send_keys("01234")
time.sleep(2)
driver.execute_script('window.scrollBy(0, 300)')
# Continue
driver.find_element(By.XPATH, '//*[@id="continue"]').click()
time.sleep(2)
# Finish
driver.find_element(By.XPATH, '//*[@id="finish"]').click()
time.sleep(2)
# Home
driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
time.sleep(2)

# Second Item
# Add to Cart
driver.execute_script('window.scrollBy(0, 300)')
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
time.sleep(5)
# ShoppingCart
driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
time.sleep(2)
# CheckOut
driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
time.sleep(2)
# Details
driver.find_element(By.NAME, "firstName").send_keys("Mike")
time.sleep(2)
driver.find_element(By.NAME, "lastName").send_keys("Vicker")
time.sleep(2)
driver.find_element(By.NAME, "postalCode").send_keys("234")
time.sleep(2)
driver.execute_script('window.scrollBy(0, 300)')
# Continue
driver.find_element(By.XPATH, '//*[@id="continue"]').click()
time.sleep(2)
# Finish
driver.find_element(By.XPATH, '//*[@id="finish"]').click()
time.sleep(2)
# Logout
driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
time.sleep(2)

# FIRE FOX
driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)
# Login
driver.find_element(By.NAME, "user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
time.sleep(2)
# Add to Cart
driver.execute_script('window.scrollBy(0, 300)')
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
time.sleep(5)
# ShoppingCart
driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[3]/a/span').click()
time.sleep(2)
# CheckOut
driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
time.sleep(2)
# Details
driver.find_element(By.NAME, "firstName").send_keys("David")
time.sleep(2)
driver.find_element(By.NAME, "lastName").send_keys("Deal")
time.sleep(2)
driver.find_element(By.NAME, "postalCode").send_keys("234")
time.sleep(2)
driver.execute_script('window.scrollBy(0, 300)')
# Continue
driver.find_element(By.XPATH, '//*[@id="continue"]').click()
time.sleep(2)
# Finish
driver.find_element(By.XPATH, '//*[@id="finish"]').click()
time.sleep(2)
# Home
driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
time.sleep(2)

# Second Item
# Add to Cart
driver.execute_script('window.scrollBy(0, 300)')
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
time.sleep(5)
# ShoppingCart
driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[3]/a').click()
time.sleep(2)
# CheckOut
driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
time.sleep(2)
# Details
driver.find_element(By.NAME, "firstName").send_keys("Pinky")
time.sleep(2)
driver.find_element(By.NAME, "lastName").send_keys("Bluey")
time.sleep(2)
driver.find_element(By.NAME, "postalCode").send_keys("234")
time.sleep(2)
driver.execute_script('window.scrollBy(0, 300)')
# Continue
driver.find_element(By.XPATH, '//*[@id="continue"]').click()
time.sleep(2)
# Finish
driver.find_element(By.XPATH, '//*[@id="finish"]').click()
time.sleep(2)
# Logout
driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
time.sleep(2)
