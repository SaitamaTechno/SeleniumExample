from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException

import time
import json

options = Options()
#options.add_argument("user-data-dir=C:\\Users\\ENES\\AppData\\Local\\Google\\Chrome\\User Data") #Path to your chrome profile

#options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://facebook.com")
print(driver.title)
time.sleep(3)
actions = ActionChains(driver)

#driver.switch_to.window(driver.window_handles[1])
#link1=driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/div[1]/div[1]/div/div/input")
#link1.send_keys("mail")
#link1=driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/div[1]/div[2]/div/div/input")
#link1.send_keys("password")
#link1.send_keys(Keys.RETURN)

input("Please press enter")
