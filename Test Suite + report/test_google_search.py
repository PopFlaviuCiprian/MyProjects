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

class Google_search(unittest.TestCase):
    COOKIE_ACCEPT = (By.ID, "L2AGLb")
    SEARCH_BAR = (By.NAME, "q")
    PRESS_SEARCH_BTN = (By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]")
    PRESS_FIRST_URL = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3')
    GO_TO_LINK = (By.LINK_TEXT, "Povești de Succes")



    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(10)
        self.chrome.get("https://www.google.ro/")
        self.chrome.find_element(*self.COOKIE_ACCEPT).click()




    def tearDown(self):
        self.chrome.quit()


    def test_search(self):
        self.chrome.find_element(*self.SEARCH_BAR).send_keys("it factory")
        self.chrome.find_element(*self.PRESS_SEARCH_BTN).click()
        self.chrome.find_element(*self.PRESS_FIRST_URL).click()
        self.chrome.find_element(*self.GO_TO_LINK).click()

        sleep(10)


