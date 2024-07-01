import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from FinalProject.base.base import Base
from selenium.webdriver.common.action_chains import ActionChains


class Order_page(Base):

    #Locators
    add_to_cart = "//button[@title='Спиннинг Shimano BeastMaster FX Predator 210ML']"
    click_cart = "//button[@class='fa cart-add-ok-cart']"
    main_word_2 = "//b[contains(text(),'Спиннинг Shimano BeastMaster FX Predator 210ML')]"
    order_button = "//a[@class='button fa fa-chevron-right right']"

    #Getters
    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))

    def get_click_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.click_cart)))

    def get_main_word_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_2)))

    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_button)))


    #Actions
    # def click_add_to_cart(self):
    #     self.get_add_to_cart().click()
    #     print("Click add to cart")
    #     time.sleep(3)

    def move_to_element_and_click(self, by, value):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()


    def click_click_cart(self):
        self.get_click_cart().click()
        print("Click click cart")

    def click_order_button(self):
        self.get_order_button().click()
        print("Click order button")


    #Methods
    def add_item(self):
        # self.click_add_to_cart()
        self.move_to_element_and_click(By.XPATH, self.add_to_cart)
        self.click_click_cart()
        self.assert_url("https://fmagazin.ru/cart/#content")
        self.assert_word(self.get_main_word_2(), "Спиннинг Shimano BeastMaster FX Predator 210ML")
        self.click_order_button()
        self.assert_url("https://fmagazin.ru/order/")





