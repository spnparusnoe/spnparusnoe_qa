import time
import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from kolesa.pages.Main_page import Main_page




def test_select_car():
    Chrome_options = webdriver.ChromeOptions()
    Chrome_options.add_experimental_option("detach", True)
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=Chrome_options)
    driver.maximize_window()

    print("Start test")

    mp = Main_page(driver)
    mp.select_car()



    print("Finish test")
    driver.quit()

