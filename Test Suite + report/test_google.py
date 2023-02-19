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


class Google(unittest.TestCase):

    PRESS_BEFORE_BTN = (By.ID, "L2AGLb")
    SEARCH_BAR = (By.NAME, "q")
    PRESS_SEARCH_BTN = (By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]")
    GO_TO_FIRST_URL = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/video-voyager/div/div[1]/div[1]/div/a/h3')
    PRESS_COOKIE_BTN_SECOND_PAGE = (By.XPATH, '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')



    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(10)
        self.chrome.get("https://www.google.ro/")
        self.chrome.find_element(*self.PRESS_BEFORE_BTN).click()

    def tearDown(self):
        self.chrome.quit()


    def test_url(self):
        actual_url = self.chrome.current_url
        expected_url = "https://www.google.ro/"
        assert actual_url == expected_url, "Url incorect"

    def test_search_bar(self):
        self.chrome.find_element(*self.SEARCH_BAR).send_keys("qa automation testing youtube")
        self.chrome.find_element(*self.PRESS_SEARCH_BTN).click()
        self.chrome.find_element(*self.GO_TO_FIRST_URL).click()
        self.chrome.find_element(*self.PRESS_COOKIE_BTN_SECOND_PAGE).click()

        sleep(10)
