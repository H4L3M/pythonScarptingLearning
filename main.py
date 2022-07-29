from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.flaticon.com/"
chrome = webdriver.Chrome()
chrome.get(url)

email = "br4yn3@gmail.com"
passwd = "Tonowi3758"

login = chrome.find_element(By.CLASS_NAME, "header--menu__login")
time.sleep(1)
print(login.screenshot_as_png)
print("logging.")
login.click()
time.sleep(1)
email_login = chrome.find_element(By.XPATH, "//button[@class][3]")
time.sleep(1)
email_login.click()
email_field = chrome.find_element(By.XPATH, "//input[@name='email']")
passwd_field = chrome.find_element(By.XPATH, "//input[@name='password']")
print("email and passwd putted on.")
email_field.send_keys(email)
passwd_field.send_keys(passwd)
time.sleep(1)
submit = chrome.find_element(By.XPATH, '//button[@type="submit"]')
time.sleep(1)
submit.click()
print("logged in..")
time.sleep(5)
chrome.get("https://www.flaticon.com/packs/human-anatomy-18")
print("navigate to pack.")
time.sleep(2)
icon = chrome.find_element(By.XPATH, '//a[@href]//img[@width="64"]')
print("select first icon from pack.")
time.sleep(2)
icon.click()
edit = chrome.find_element(By.XPATH, '//i[@class="icon--edit-alt"]')

print("edit clicked..")
time.sleep(2)
edit.click()

time.sleep(1)
# svg = chrome.find_element(By.XPATH, '//*[name()="svg" and @class=""]')
svg = chrome.find_element(By.XPATH, '//div[@class="detail__editor__icon-holder icon-holder"]')
print("svg element : v")
print(svg.text)
time.sleep(2)
with open('brain.svg', 'w') as f:
    f.write(svg.text)



# search = chrome.find_element(By.XPATH, '//input[@name="word"]')  #//input[@name="word"]
# time.sleep(1)
# search.send_keys("flags")
# time.sleep(1)
# search_button = chrome.find_element(By.XPATH, '//button[@type="submit"]')
# time.sleep(1)
# search_button.click()
