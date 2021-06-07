
class User:
    """we are only storing name birthdady and age. but soon we add more"""

    def __init__(self, full_name, birthday,age):
        self.name = full_name
        self.birthday = birthday
        self.age = age
help(User)


user = User("palash", "19851024","55")
print(user.name)
print(user.birthday)
print(user.age)
print(user.birthday)

full_name = "palash k. mohajon"
name_peace = full_name.split(" ")
print(name_peace[0])
print(name_peace[1])
print(name_peace[-1])

from selenium import webdriver
import time

driver = webdriver.Chrome("C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get("https://www.google.com/")

print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("iphone 12")
time.sleep(5)
driver.find_element_by_class_name("gNO89b").click()
print(driver.title)
value = driver.find_element_by_xpath("//*[@id='result-stats']").text

print(value)
splited_value = value.split(" ")
print(splited_value[1])

driver.quit()





