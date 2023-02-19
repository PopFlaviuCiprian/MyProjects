import unittest
from time import sleep
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login(unittest.TestCase):

    USER = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")



    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(4)
        self.chrome.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.chrome.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")



    def tearDown(self):
        self.chrome.quit()

    def test_url(self):
        actual_url = self.chrome.current_url
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        assert actual_url == expected_url, f"Url nu este corect"

    def test_login(self):
        self.chrome.current_url
        self.chrome.find_element(*self.USER).send_keys("Admin")
        self.chrome.find_element(*self.PASSWORD).send_keys("admin123")
        self.chrome.find_element(*self.LOGIN).click()



    def test_another_type_login(self):
        self.chrome.get(f"https://{self.USER}:{self.PASSWORD}@opensource-demo.orangehrmlive.com/web/index.php/auth/login")

