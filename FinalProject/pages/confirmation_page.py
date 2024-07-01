import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from FinalProject.base.base import Base
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class confirmation_page(Base):  #создаем класс


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    fio = "//input[@name='User_Name']"
    telephone = "//input[@name='User_Phone']"
    mail = "//input[@name='User_Email']"
    main_word = "//tbody/tr/td/a[1]"

    #Getters
    def get_fio(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.fio)))

    def get_telephone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.telephone)))

    def get_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mail)))


    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    #Actions
    def enter_fio(self, fio):
        self.get_fio().send_keys(fio)
        print("FIO entered")
        time.sleep(1)

    def enter_telephone(self, telephone):
        self.get_telephone().send_keys(telephone)
        print("Telephone entered")

    def enter_mail(self, mail):
        self.get_mail().send_keys(mail)
        print("Mail entered")



    #Methods
    def confirmation(self):
        self.enter_fio("ivanov ivan ivanych")
        self.enter_telephone("9122343434")
        self.enter_mail("koka@yandex.ru")
        self.assert_url("https://fmagazin.ru/order/")
        self.assert_word(self.get_main_word(), "Спиннинг Shimano BeastMaster FX Predator 210ML")
        self.get_screenshot()