import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from FinalProject.pages.main_page import Main_page
from FinalProject.pages.main_page_2 import Main_page_2
from FinalProject.pages.order_page import Order_page
from FinalProject.pages.confirmation_page import Confirmation_page



def test_buy_product_1():
    Chrome_options = webdriver.ChromeOptions()
    Chrome_options.add_experimental_option("detach", True)
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=Chrome_options)
    driver.maximize_window()

    print("Start test")

    mp = Main_page(driver)
    mp.select_products_1()

    mp2 = Main_page_2(driver)
    mp2.select_products_2()

    op = Order_page(driver)
    op.add_item()

    cf = Confirmation_page(driver)
    cf.confirmation()

    print("Finish test")
    driver.quit()

