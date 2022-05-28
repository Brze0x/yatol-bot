import pickle
from time import sleep
from modules.config import LOGIN, PASSWORD, URL, DRIVER_PATH
from modules.elements import Elements
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Login:
    def __init__(self):
        self.url = URL
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        self.options.add_experimental_option("useAutomationExtension", False)
        self.service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service, options=self.options)


    def get_cookies(self, name: str):
        cookies = self.driver.get_cookies()
        with open(f'./cookies/{name}.pickle', 'wb') as f:
            pickle.dump(cookies, f)


    def login(self):
        cookies_name = input('Type the name of the cookies:\n').lower()
        self.driver.get(self.url)
        self.driver.find_element(by=By.XPATH, value=Elements.login_btn).click()
        self.driver.find_element(by=By.ID, value=Elements.passp_field_login).send_keys(LOGIN)
        sleep(1)
        self.driver.find_element(by=By.ID, value=Elements.passp_sign_in).click()
        sleep(2)
        self.driver.find_element(by=By.ID, value=Elements.passp_field_passwd).send_keys(PASSWORD)
        sleep(2)
        self.driver.find_element(by=By.ID, value=Elements.passp_sign_in).click()
        sleep(3)
        self.get_cookies(name=cookies_name)
        self.driver.close()

