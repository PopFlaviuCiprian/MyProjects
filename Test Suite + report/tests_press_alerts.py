import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep



class Alerts(unittest.TestCase):
    RESULT_MESSAGE = (By.ID, "result")
    ALLERT_BUTTON = (By.XPATH, '//button[text()= "Click for JS Alert"]')
    CONFIRM_BUTTON = (By.XPATH, '//button[text()= "Click for JS Confirm"]')
    PROMPT_BUTTON = (By.XPATH, '//button[text()= "Click for JS Prompt"]')


    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(4)
        self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")

    def tearDown(self):
        self.chrome.quit()

    def test_alert(self):
        self.chrome.find_element(*self.ALLERT_BUTTON).click()
        allert_obj = self.chrome.switch_to.alert
        print(f"Allert display the folowing text {allert_obj.text}")
        allert_obj.accept() # here we press ok on the alert obj
        result_text = self.chrome.find_element(*self.RESULT_MESSAGE).text
        self.assertEqual(result_text, "You successfully clicked an alert")



    def test_confirm_ok(self):
        self.chrome.find_element(*self.CONFIRM_BUTTON).click()
        obj = self.chrome.switch_to.alert
        print(f'Pressing ok confirms the following message: {obj.text}')
        obj.accept()
        result_message = self.chrome.find_element(*self.RESULT_MESSAGE).text
        self.assertEqual(result_message, 'You clicked: Ok')

    def test_confirm_cancel(self):
        self.chrome.find_element(*self.CONFIRM_BUTTON).click()
        obj = self.chrome.switch_to.alert
        obj.dismiss()
        result_dismiss = self.chrome.find_element(*self.RESULT_MESSAGE).text
        self.assertEqual(result_dismiss, 'You clicked: Cancel')


    def test_press_ok_prompt(self):
        self.chrome.find_element(*self.PROMPT_BUTTON).click()
        obj = self.chrome.switch_to.alert
        print(f'Pressing button shows: {obj.text} ')
        text = "This is a test example"
        obj.send_keys(text)
        obj.accept()
        result_text = self.chrome.find_element(*self.RESULT_MESSAGE).text
        self.assertEqual(result_text, f"You entered: {text}")


    def test_press_cancel_prompt(self):
        self.chrome.find_element(*self.PROMPT_BUTTON).click()
        obj = self.chrome.switch_to.alert
        obj.dismiss()
        result_text = self.chrome.find_element(*self.RESULT_MESSAGE).text
        self.assertEqual(result_text, f'You entered: null')
