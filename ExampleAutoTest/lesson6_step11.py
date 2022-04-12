from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
    
browser = webdriver.Chrome()
browser.get(link)


x_element = browser.find_element_by_css_selector('#treasure')
x = x_element.get_attribute('valuex')
x = int(x)
y = calc(x)

input1 = browser.find_element_by_css_selector('#answer')
input1.send_keys(y)

option1 = browser.find_element_by_css_selector("#robotCheckbox")
option1.click()
option2 = browser.find_element_by_css_selector("#robotsRule")
option2.click()
option3 = browser.find_element_by_css_selector(".btn")
option3.click()


time.sleep(2)



# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
