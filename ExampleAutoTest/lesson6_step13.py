from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"
    
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_css_selector('#answer')
input1.send_keys(y)

option1 = browser.find_element_by_css_selector("#robotCheckbox")
option1.click()

radiobutton = browser.find_element_by_css_selector("#robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
radiobutton.click()



option3 = browser.find_element_by_css_selector(".btn")
option3.click()

