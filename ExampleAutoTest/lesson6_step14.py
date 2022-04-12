from selenium import webdriver
import time
import os
link = "http://suninjuly.github.io/file_input.html"
    
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_css_selector('[placeholder="Enter first name"]')
input1.send_keys("DYDYA")



input2 = browser.find_element_by_css_selector('[placeholder="Enter last name"]')
input2.send_keys("PETYA")



input3 = browser.find_element_by_css_selector('[placeholder="Enter email"]')
input3.send_keys("www")



current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file_example.txt"
file_path = os.path.join(current_dir, file_name)

element = browser.find_element_by_css_selector("#file")
element.send_keys(file_path)

browser.find_element_by_css_selector(".btn").click()

