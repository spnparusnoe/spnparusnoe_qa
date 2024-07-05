import time
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from kolesa.base.Base import Base


class Main_page(Base):

    url = 'https://kolesa.kz/'

    #Locators
    passenger_car = "//span[@data-id='2']"
    body_type = "(//span[@title='Легковые'])[2]"
    city = "(//span[@class ='FilterItem__label'])[2]"
    brand = "//span[normalize-space()='Toyota']"
    item_car = "//span[normalize-space()='Camry']"
    checkbox = "//label[@for='_sys-hasphoto-checkbox-0']"
    year = "//input[@id='year[from]']"
    price = "//input[@id='price[to]']"
    submit_button = "//button[@type='submit']"
    car = "//div[@id='advert-172766373']//a[@class='a-card__link'][normalize-space()='Toyota Camry']"
    main_word = "//span[@itemprop='brand']"


    #Getters
    def get_passenger_car(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.passenger_car)))

    def get_body_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.body_type)))

    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand)))

    def get_item_car(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_car)))

    def get_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox)))

    def get_year(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.year)))

    def get_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_submit_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.submit_button)))

    def get_car(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.car)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    #Actions
    def click_passenger_car(self):
        self.get_passenger_car().click()
        print("Click passenger car")

    def click_body_type(self):
        self.get_body_type().click()
        print("Click body type")

    def click_city(self):
        self.get_city().click()
        print("Click city")

    def click_brand(self):
        self.get_brand().click()
        print("Click brand")

    def click_item_car(self):
        self.get_item_car().click()
        print("Click item car")

    def click_checkbox(self):
        self.get_checkbox().click()
        print("Click checkbox")

    def input_year(self, year):
        self.get_year().send_keys(year)
        print("Input year")

    def input_price(self, price):
        self.get_price().send_keys(price)
        print("Input price to")

    def click_submit_button(self):
        self.get_submit_button().click()
        print("Click submit button")

    def click_car(self):
        self.get_car().click()
        print("Click car")

    def switch_and_assert(self):
        windows_1 = self.driver.window_handles[0]
        windows_2 = self.driver.window_handles[1]
        self.driver.switch_to.window(windows_2)
        text = self.get_main_word().text
        assert text == "Toyota Camry", "WRONG SELECTED ITEM"
        print("GOOD SELECTED ITEM")




    #Methods
    def select_car(self):
        with allure.step("select car"):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.assert_url("https://kolesa.kz/")
            self.click_passenger_car()
            self.click_body_type()
            self.click_city()
            self.click_brand()
            self.click_item_car()
            self.click_checkbox()
            self.input_year("2014")
            self.input_price("10000000")
            self.click_submit_button()
            self.assert_url("https://kolesa.kz/cars/toyota/camry/almaty/?auto-car-grbody=1&_sys-hasphoto=2&year%5Bfrom%5D=2014&price%5Bto%5D=10000000")
            self.click_car()
            self.switch_and_assert()
            time.sleep(3)


