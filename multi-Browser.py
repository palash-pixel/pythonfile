from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(
    executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("https://www.google.com/")

time.sleep(5)
driver.back()
time.sleep(5)
print(driver.title)
time.sleep(5)
driver.forward()
print(driver.title)

driver.get("https://www.yahoo.com/")
time.sleep(5)

# driver.find_element_by_xpath(
# "/html/body/div[2]/div/main/div[6]/div/ul/li[2]/div/div[1]/div[1]/div/div[2]/a/u").click()

print(driver.title)

print(driver.current_url)
time.sleep(5)
# driver.close()
driver.quit()
