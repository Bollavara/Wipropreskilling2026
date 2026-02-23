from selenium import webdriver
from Loginpage import login_page
import time
driver=webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)
login=login_page(driver)

login.enter_username("Admin")
login.enter_password("admin123")
login.click_login()
time.sleep(5)