import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from FinalProject.base.base import Base


class Main_page(Base):

    url = 'https://fmagazin.ru/'

    #Locators
    select_product_1 = "(//a[contains(text(), 'Спиннинги')])[3]"

    #Getters
    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    #Actions
    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click product 1")

    #Methods
    def select_products_1(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_select_product_1()
        self.assert_url("https://fmagazin.ru/snasti/udilisha/spinningi/")

