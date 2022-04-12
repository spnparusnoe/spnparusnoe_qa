from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)


x = browser.find_element_by_css_selector('#num1')
x = x.text
y = browser.find_element_by_css_selector('#num2')
y = y.text
z = int(x) + int(y)
z = str(z)

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_css_selector("#dropdown"))
select.select_by_value(str(z))  # ищем элемент с текстом "Python"

browser.find_element_by_css_selector(".btn").click()


# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
