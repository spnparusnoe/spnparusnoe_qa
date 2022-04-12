from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/alert_accept.html"
    
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_css_selector('.btn').click()

confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
x = int(x)
y = calc(x)

input1 = browser.find_element_by_css_selector('#answer')
input1.send_keys(y)

browser.find_element_by_css_selector(".btn").click()
