import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from FinalProject.base.base import Base
from selenium.webdriver.common.action_chains import ActionChains


class main_page_2(Base):  #создаем класс


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    checkbox = "//input[@value='11']"
    dropdown = "//select[@name='val']"
    item_dropdown = "//option[@value='Stat_Views']"
    spinning = "//*[@id='productsShowcase']/section[1]"
    main_word = "//h1"

    #Getters
    def get_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox)))

    def get_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dropdown)))

    def get_item(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_dropdown)))

    def get_spinning(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.spinning)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    #Actions
    # def click_checkbox(self):
    #     self.get_checkbox().click()
    #     print("Click checkbox")
    #     time.sleep(5)

    def move_to_element_and_click(self, by, value):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        time.sleep(6)

    def click_dropdown(self):
        self.get_dropdown().click()
        print("Click dropdown")
        time.sleep(1)

    def click_item(self):
        self.get_item().click()
        print("Click item")
        time.sleep(3)

    def click_spinning(self):
        self.get_spinning().click()
        print("Click spinning")

    #Methods
    def select_products_2(self):
        # self.click_checkbox()
        self.move_to_element_and_click(By.XPATH, self.checkbox)
        self.click_dropdown()
        self.click_item()
        self.click_spinning()
        self.assert_word(self.get_main_word(), "Спиннинг Shimano BeastMaster FX Predator")



