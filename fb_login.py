from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# 1. Assign browser variable
browser  = webdriver.Chrome(executable_path="./chromedriver")


# 2. Open a webpage
browser.get("http://facebook.com")

username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")

username.send_keys("haoxray")
password.send_keys("Styleofme!@#")
password.send_keys(Keys.ENTER)

# 3. Sleep application for 5 seconds
sleep(50)


# 4. Close browser
browser.close()